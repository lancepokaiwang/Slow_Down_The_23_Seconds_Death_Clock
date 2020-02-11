import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.model_selection import cross_val_score
from pprint import pprint

features = [
    "C_YEAR", "C_MNTH", "C_WDAY", "C_HOUR", "C_SEV", "C_VEHS", "C_CONF", "C_RCFG", "C_WTHR", "C_RSUR",
    "C_RALN", "C_TRAF", "V_ID", "V_TYPE", "V_YEAR", "P_ID", "P_SEX", "P_AGE", "P_PSN", "P_ISEV",
    "P_SAFE", "P_USER", "C_CASE"
]

df = pd.read_csv('data/data_clean_v2.csv', header=1, names=features)
# df['class'] = df['class'].map({'g':0,'h':1})

x = df[features[:-1]]
y = df['C_SEV']

# x_train,x_test,y_train,y_test = cross_validation.train_test_split(x,y,test_size=0.4,random_state=0)
depth = []
for i in range(3, 20):
    print("i = {}".format(i))
    clf = tree.DecisionTreeClassifier(max_depth=i)
    # Perform 7-fold cross validation
    scores = cross_val_score(estimator=clf, X=x, y=y, cv=7, n_jobs=4)
    depth.append((i, scores.mean()))
print(depth)
