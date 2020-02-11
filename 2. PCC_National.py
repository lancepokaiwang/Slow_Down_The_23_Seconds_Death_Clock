# importing libraries
import csv
from sklearn.datasets import load_boston
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
from sklearn.linear_model import RidgeCV, LassoCV, Ridge, Lasso  # Loading the dataset

features = None
data = []
with open('data/data_clean_v2.csv', newline='') as csvfile:
    index = 0
    rows = csv.reader(csvfile)
    for row in rows:
        if index == 0:
            features = row
        if index != 0:
            for i in range(0, len(row)):
                if row[i].isdigit():
                    row[i] = int(row[i])
            #     if row[i] == 'M':
            #         row[i] = int(1)
            #     elif row[i] == 'F':
            #         row[i] = int(0)
            data.append(row)
        index += 1

df = pd.DataFrame(data, columns=features)
df = df.drop("C_YEAR", 1)
df = df.drop("V_ID", 1)
df = df.drop("P_ID", 1)
df = df.drop("C_CASE", 1)
# X = df.drop("C_SEV", 1)  # Feature Matrix
# y = df["C_SEV"]  # Target Variable
print(df)


# Using Pearson Correlation
plt.figure(figsize=(20, 20))
cor = df.corr()
sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
plt.show()

# Correlation with output variable
cor_target = abs(cor["C_SEV"])  # Selecting highly correlated features
relevant_features = cor_target[cor_target > 0.4]
print(relevant_features)
