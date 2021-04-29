def classifier_model(clf,cv,fant_team_name,labels,features,fant_team_perf_for_pred):
    """
    
    input:
        clf: supervised classification classifier
                
        cv: deals with the training dataset for the model
            The class labels shuffled > pertains to the historical actual teams performance stat i.e. our baseline data
            Strategy used is StratifiedShuffleSplit for cross validation 
         
        fant_team_name:  name of the users fantasy team that whose shot at championshiop is being predicted 
        
        fant_team_perf_for_pred: deals with the dataset that is to be predicted
                        i.e. dataset used here pertains to the performance stat of the players drafted in user's fantasy team
                        
    output:
       classifier_pred_res: dictionary logging the prediction result along with the model metrics
                        
    """
    classifier_pred_res = {}
    true_negatives = 0
    false_negatives = 0
    true_positives = 0
    false_positives = 0
    
    for train_idx, test_idx in cv.split(features,labels):
        features_train = []
        features_test  = []
        labels_train   = []
        labels_test    = []
        for i in train_idx:
            features_train.append( features[i] )
            labels_train.append( labels[i] )
        for j in test_idx:
            features_test.append( features[j] )
            labels_test.append( labels[j] )
        
        #Using the training set to fit the model
        clf.fit(features_train, labels_train)
        
        # Testing on the test set
        predictions = clf.predict(features_test)
        
        # Comparing the predicted label with the actual label from dataset
        
        for prediction, truth in zip(predictions, labels_test):
            if prediction == 0 and truth == 0:
                true_negatives = true_negatives + 1
            elif prediction == 0 and truth == 1:
                false_negatives = false_negatives + 1
            elif prediction == 1 and truth == 0:
                false_positives = false_positives + 1
            elif prediction == 1 and truth == 1:
                true_positives = true_positives + 1
    
    # Calculating the metrics
    
    total_predictions = true_negatives + false_negatives + false_positives + true_positives
    accuracy = 1.0*(true_positives + true_negatives)/total_predictions
    precision = 1.0*true_positives/(true_positives+false_positives)
    recall = 1.0*true_positives/(true_positives+false_negatives)
    f1 = 2.0 * true_positives/(2*true_positives + false_positives+false_negatives)
    f2 = (1+2.0*2.0) * precision*recall/(4*precision + recall)
    
    # Now, the time for prediction based on user's fantasy team performance data
    user_fantasy_team_perf_pred = clf.predict(fant_team_perf_for_pred)
    #print(user_fantasy_team_perf_pred)
    
    if user_fantasy_team_perf_pred[0] == 0:
        championship_prediction = 'No'
    else:
        championship_prediction = 'Yes'
    
    classifier_pred_res = {
                       
                       "predicted fantasy team name":fant_team_name,
                       "predicted to be champion?":championship_prediction,   
                       #"classifier implemented":clf, 
                       "accuracy":accuracy, 
                       "precision":precision, 
                       "recall":recall,
                       "f1":f1,
                       "f2":f2,
                        "total predictions":total_predictions,
                        "true positives":true_positives,
                        "false positives":false_positives,
                        "false_negatives":false_negatives,
                        "true negatives":true_negatives
                     }
    #print(classifier_pred_res)
    
    return classifier_pred_res
