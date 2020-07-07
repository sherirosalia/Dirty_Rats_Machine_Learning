import pandas as pd 
import numpy as np 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt 
from sklearn import tree
# this is sequel to ml_prep.py next file is chart.py
data=pd.read_csv('csv_files/prep_w_cols_removed.csv')
print(data.head())

#split rat code F023 off and drop from dataframe for ML
target=data['F023']
data.drop(['F023', 'id', 'name'], axis=1, inplace=True)
X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=42)
# print(X_test)
# exit()
rf = RandomForestClassifier(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)
probabilities=rf.predict_proba(X_test)
#score of forest
print(rf.score(X_test, y_test))
print(probabilities)

#get important features
# print(rf.feature_importances_)
#probabilities=[x[1] for x in probabilities]

## commenting out below, ran once. It works. Plot made.
probabilities=[y for x, y in probabilities]
# print(probabilities)

# fpr, tpr, thresholds = metrics.roc_curve(y_test, probabilities)

# plt.plot(fpr, tpr)
# plt.show()

## end of comment out
X_test['prob']=probabilities
X_test.to_csv('csv_files/testing_predictions.csv')
exit()
tree_to_print=rf.estimators_[0]
tree.export_graphviz(tree_to_print, 'images/random_forest_print.dot')

exit()
#zip names and feature importance scores
f_imp=rf.feature_importances_
f_name=data.columns
features=zip(f_name, f_imp)
# print(features)
# features into a datafame
f_df=pd.DataFrame(list(features))
print(f_df.head())


f_df.to_csv('csv_files/imp_feat.csv', index=False)


