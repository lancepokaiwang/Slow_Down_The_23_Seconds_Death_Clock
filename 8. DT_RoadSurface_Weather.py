import pandas as pd
import numpy as np

# Read dataset
df = pd.read_csv('data/ns/data_clean_ns_focus.csv', header=0)

df = df.drop('C_RSUR', axis=1)
df = df.drop('C_WTHR', axis=1)

# quebec
# df = df.drop("P_SAFE", 1)
# df = df.drop("P_PSN", 1)
# df = df.drop("P_SEX", 1)
# df = df.drop("P_AGE", 1)
# df = df.drop("V_AGE", 1)
# df = df.drop("C_TRAF", 1)
# df = df.drop("V_TYPE", 1)

# National
# df = df.drop('C_YEAR', axis=1)
# df = df.drop('V_ID', axis=1)
# df = df.drop('P_ID', axis=1)
# df = df.drop('C_CASE', axis=1)
#
# df = df.drop('M_V_TYPE', axis=1)
# df = df.drop('M_V_AGE', axis=1)
# df = df.drop('M_P_AGE', axis=1)
# df = df.drop('M_P_SEX', axis=1)
# df = df.drop('M_P_ISEV', axis=1)
# df = df.drop('M_P_SAFE', axis=1)

# Experiment: Drop Correlated Features:
# df = df.drop('C_TRAF', axis=1)
# df = df.drop('C_RALN', axis=1)
# df = df.drop('C_RSUR', axis=1)

# Display example observations
print(df.head())

print(df['P_ISEV'].value_counts())

# Data Balancing
from sklearn.utils import resample

# Separate majority and minority classes
df_1 = df[df.P_ISEV == 1]
df_2 = df[df.P_ISEV == 2]
df_3 = df[df.P_ISEV == 3]
# NS
df_4 = df[df.P_ISEV == 4]


# ns
# Upsample minority class
df_minority_upsampled_2 = resample(df_2,
                                   replace=True,  # sample with replacement
                                   n_samples=78668,  # to match majority class
                                   random_state=123)  # reproducible results

# Combine majority class with upsampled minority class
df_upsampled = pd.concat([df_1, df_minority_upsampled_2])

# Upsample minority class
df_minority_upsampled_3 = resample(df_3,
                                   replace=True,  # sample with replacement
                                   n_samples=78668,  # to match majority class
                                   random_state=123)  # reproducible results

# Combine majority class with upsampled minority class
df_upsampled = pd.concat([df_upsampled, df_minority_upsampled_3])

# Upsample minority class
df_minority_upsampled_4 = resample(df_4,
                                   replace=True,  # sample with replacement
                                   n_samples=78668,  # to match majority class
                                   random_state=123)  # reproducible results

# Combine majority class with upsampled minority class
df_upsampled = pd.concat([df_upsampled, df_minority_upsampled_4])


# quebec
# # Upsample minority class
# df_minority_upsampled_2 = resample(df_2,
#                                    replace=True,  # sample with replacement
#                                    n_samples=111734,  # to match majority class
#                                    random_state=123)  # reproducible results
#
# # Combine majority class with upsampled minority class
# df_upsampled = pd.concat([df_1, df_minority_upsampled_2])
#
# # Upsample minority class
# df_minority_upsampled_3 = resample(df_3,
#                                    replace=True,  # sample with replacement
#                                    n_samples=111734,  # to match majority class
#                                    random_state=123)  # reproducible results
#
# # Combine majority class with upsampled minority class
# df_upsampled = pd.concat([df_upsampled, df_minority_upsampled_3])

# National
# # Upsample minority class
# df_minority_upsampled_1 = resample(df_1,
#                                    replace=True,  # sample with replacement
#                                    n_samples=1871219,  # to match majority class
#                                    random_state=123)  # reproducible results
#
# # Combine majority class with upsampled minority class
# df_upsampled = pd.concat([df_2, df_minority_upsampled_1])
#
# # Upsample minority class
# df_minority_upsampled_3 = resample(df_3,
#                                    replace=True,  # sample with replacement
#                                    n_samples=1871219,  # to match majority class
#                                    random_state=123)  # reproducible results
#
# # Combine majority class with upsampled minority class
# df_upsampled = pd.concat([df_upsampled, df_minority_upsampled_3])

# Display new class counts
print(df_upsampled.P_ISEV.value_counts())

labels = df_upsampled.P_ISEV
data = df_upsampled.drop('P_ISEV', axis=1)

from sklearn.preprocessing import normalize

data = normalize(data)

print(data)

# Split Data
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    data, labels, test_size=0.4, random_state=30)

# ====================================================
# df_que = pd.read_csv('data/quebec/data_clean_quebec_focus.csv', header=0)
# df_que = df_que.drop('C_SEV', axis=1)
# df_que = df_que.where(pd.notna(df_que), df_que.mean(), axis='columns')
# print(df_que.head())
# y_test = df_que.P_ISEV;
# X_test = df_que.drop('P_ISEV', axis=1)

# ====================================================


# ======================================Machine Learning===============================
# Decision Tree
from sklearn import tree

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)

predict = clf.predict(X_test)

from sklearn.metrics import accuracy_score

print("Decision Tree Accuracy: {}".format(accuracy_score(y_test, predict)))

# Naive Bayes
from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()
y_pred = gnb.fit(X_train, y_train).predict(X_test)
print("Naive Bayes Accuracy: {}".format(accuracy_score(y_test, y_pred)))

# KNN
from sklearn.neighbors import KNeighborsClassifier

neigh = KNeighborsClassifier(n_neighbors=5, weights='distance')
neigh.fit(X_train, y_train)
knn_pred = neigh.predict(X_test)
print("KNN Accuracy: {}".format(accuracy_score(y_test, knn_pred)))
