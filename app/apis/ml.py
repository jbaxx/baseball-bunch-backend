import urllib.parse
from flask import g
from flask import abort
from flask_restplus import Namespace
from flask_restplus import Resource
from flask_restplus import fields as rest_fields
from marshmallow import Schema
from marshmallow import fields
from MySQLdb import ProgrammingError
import MySQLdb.cursors

import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import StratifiedShuffleSplit
from .mlUtils import dict_to_numpyarr_extractFeature
from .mlUtils import extract_class_label_from_data
from .mlClassModel import classifier_model
from .mlFeatures import engineer_ml_dataset_features

from .. import db
from .. import token_auth
from .fantasy_team import FantasyTeamModel
from .fantasy_team_lineup import FantasyTeamLineupModel


api = Namespace('api/predict/', description= 'The players')

def parse_url(url):
    return urllib.parse.unquote(url)



def get_prediction(fantasy_team_id):
    query_team_baseline, query_fant_team_field_stat, query_fant_team_batting_stat, query_fant_team_pitching_stat =\
        engineer_ml_dataset_features()

    cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)

    """
    # Get the training data from MYSQL server
    # This is the Teams batting,pitching & fielding stat at yearly grain.
    # Stats are obtained at player level who played for the Team and averaged across the players for the Team state
    # Stats are normalized by calculating them at per_game
    # Teams who have played atleast 150 games in a given year since year 2000 are considered
    # 600 datapoints overall
    """

    query_team_baseline, query_fant_team_field_stat, query_fant_team_batting_stat, query_fant_team_pitching_stat =\
        engineer_ml_dataset_features()

    try:
        cursor.execute(query_team_baseline)
    except ProgrammingError as err:
        raise err
    vteam_training_data = cursor.fetchall()
    cols_training_data_features = [i[0] for i in cursor.description]
    teams_df = pd.DataFrame(vteam_training_data,columns=cols_training_data_features).set_index('yearteamid')
    train_dataset = teams_df.to_dict('index')

    """
    # Get the data for predicting the championship outcome for User selected Fantasy Team from MYSQL server
    # This is the drafted players batting,pitching & fielding stat from their historical performance.
    # Stats are obtained at player level who are drafted in the Fantasy Team and averaged across the players for the Fantasy Team
    # Stats are normalized by calculating them at per_game
    """

    # fielding stat
    try:
        cursor.execute(query_fant_team_field_stat, {'fantasy_team_id': fantasy_team_id})
    except ProgrammingError as err:
        raise err
    vfantasyteam_fs = cursor.fetchall()
    cols_fant_team_fs = [i[0] for i in cursor.description]

    # batting stat
    try:
        cursor.execute(query_fant_team_batting_stat, {'fantasy_team_id': fantasy_team_id})
    except ProgrammingError as err:
        raise err
    vfantasyteam_bs = cursor.fetchall()
    cols_fant_team_bs = [i[0] for i in cursor.description]

    # pitching stat
    try:
        cursor.execute(query_fant_team_pitching_stat, {'fantasy_team_id': fantasy_team_id})
    except ProgrammingError as err:
        raise err
    vfantasyteam_ps = cursor.fetchall()
    cols_fant_team_ps = [i[0] for i in cursor.description]

    # merge the stat
    fant_teams_fs_df = pd.DataFrame(vfantasyteam_fs,columns=cols_fant_team_fs).set_index('teamname')
    fant_teams_bs_df= pd.DataFrame(vfantasyteam_bs,columns=cols_fant_team_bs).set_index('teamname')
    fant_teams_ps_df= pd.DataFrame(vfantasyteam_ps,columns=cols_fant_team_ps).set_index('teamname')

    fant_team_stat = pd.concat([fant_teams_bs_df.iloc[:,1:], fant_teams_ps_df.iloc[:,1:]], axis=1, join='inner')
    fant_team_stat = pd.concat([fant_team_stat, fant_teams_fs_df.iloc[:,1:]], axis=1, join='inner')

    fantasy_team_dataset = fant_team_stat.to_dict('index')

    features_list_org_all =[ 'champs',
            'r_per_game','ab_per_game','h_per_game','b2_per_game','b3_per_game','hr_per_game','rbi_per_game',
            'sb_per_game','cs_per_game','bb_per_game','so_per_game','hbp_per_game','pitching_h_per_game',
        'er_per_game', 'pitching_hr_per_game','pitching_bb_per_game','pitching_so_per_game', 'era_per_game',
    'ibb_per_game','pitching_r_per_game','po_per_game','a_per_game','e_per_game','dp_per_game']


    # Convert the training data dictionary into numpy array
    data = dict_to_numpyarr_extractFeature(train_dataset, features_list_org_all)

    # Extract class label from features from training data set
    labels, features = extract_class_label_from_data(data)

    # Convert the dataset to be predicted i.e. fantasy team stat that user has selected via the applicatio
    pred_nump_data = dict_to_numpyarr_extractFeature(fantasy_team_dataset, fant_team_stat.columns)


    # Using StratifiedShuffleSplit for test_size of 0.5
    #sss = StratifiedShuffleSplit(n_splits=5, test_size=0.5, random_state=0)
    sss = StratifiedShuffleSplit(n_splits=20, test_size=0.5, random_state=42)

    #clf_list = [LinearSVC(),GaussianNB(),KMeans(init='random',n_clusters=3, max_iter=300, random_state=42)]
    #clf_key_list = ['LinearSVC','GaussianNB','KMeans']
    #clf_list = [LinearSVC(max_iter=1000,dual=False),GaussianNB(),KMeans(init='random',n_clusters=3, random_state=42)]
    #clf_key_list = ['LinearSVC','GaussianNB','KMeans']
    clf_list = [LinearSVC(max_iter=1000),GaussianNB(),KNeighborsClassifier()]
    clf_key_list = ['LinearSVC','GaussianNB','KNeighbors']


    for key in fantasy_team_dataset.keys():
        fant_team_name = key


    classifier_pred_result={}
    for clf in range(len(clf_list)):
        clf_name= clf_key_list[clf]
        classifier_pred_result[clf_name] = classifier_model(clf_list[clf],sss,fant_team_name,labels,features,pred_nump_data)

    print ('**************************************')
    print ('prediction results')
    print ('***************************************')
    print(classifier_pred_result)

    print ('**************************************')
    print ('Fantasy Team normalized stat')
    print ('***************************************')
    print (fantasy_team_dataset)

    print ('**************************************')
    print ('***************************************')

    team_stats = {}
    for f in fantasy_team_dataset:
        for k in fantasy_team_dataset[f]:
            print(float(fantasy_team_dataset[f][k]))
            team_stats[k] = float(fantasy_team_dataset[f][k])

    classifier_team_output = classifier_pred_result
    classifier_team_output['fantasy_team_stats'] = team_stats
    print(classifier_team_output)


    # return classifier_pred_result
    return classifier_team_output


@api.route('/<fantasy_team_id>')
class Predict(Resource):
    @api.doc(security='Bearer Auth')
    @api.response(200, 'Success')  # Api documentation
    @api.response(401, 'Unauthorized Access')  # Api documentation
    @api.response(500, 'Query error')  # Api documentation
    @token_auth.login_required
    def get(self, fantasy_team_id):

        fantasy_team_id = parse_url(fantasy_team_id)

        user_id = g.user.get('userid')
        try:
            fantasy_team = FantasyTeamModel().get_by_userid_teamid(user_id, fantasy_team_id)
        except ProgrammingError:
            abort(500)

        if not fantasy_team:
            abort(409, 'Fantasy Team could not be found')

        try:
            fantasy_team_lineup_result = FantasyTeamLineupModel().get_by_team_id(fantasy_team_id)
        except ProgrammingError:
            abort(500)

        if len(fantasy_team_lineup_result) == 0:
            abort(409, description='Fantasy Team does not have lineup')

        predictions = get_prediction(fantasy_team_id)
        return predictions

