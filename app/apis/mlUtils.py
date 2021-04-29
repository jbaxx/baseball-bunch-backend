import numpy as np
import configparser
# import mysql.connector

# def connect_to_mysql(ihost,iuser,ipassword,idatabase):
#     conn = mysql.connector.connect(
#         host=ihost,
#         user=iuser,
#         password=ipassword,
#         database=idatabase)  
#     return conn
    

def dict_to_numpyarr_extractFeature( idict, ifeaturelist):
    """ this function reads the input dictionary, extracts the features supplied via input 
        and outputs a mxn numpy array 
            where m is the number of keys in the dictionary and
                  n in the number of features                  
    """

    result_list = []
        
    for key in sorted(idict.keys()):
        tmp_list = []
        for feature in ifeaturelist:
            value = idict[key][feature]
            tmp_list.append( float(value) )

        # Add the value to the result array
        output = True
        # Exclude the first feature, if the feature is a classification label
        if ifeaturelist[0] == 'champs':
            test_list = tmp_list[1:]
        else:
            test_list = tmp_list
      
        if output:
            result_list.append( np.array(tmp_list) )

    return np.array(result_list)

def extract_class_label_from_data( inumpydataset ):
    """ 
        input: dataset in the form of numpy array
        ouput: 
               labels: list containing the classification labels
               features: list containing all the features
    """

    labels = []
    features = []
    for item in inumpydataset:
        labels.append( item[0] )
        features.append( item[1:] )

    return labels, features
