import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

features = None

df = pd.read_csv('data/data_clean_focus_v5.csv', header=0)
df = df.drop("C_YEAR", 1)
df = df.drop("V_ID", 1)
df = df.drop("P_ID", 1)
features = df.columns
print(features)


# from sklearn import preprocessing
# x = df.values #returns a numpy array
# min_max_scaler = preprocessing.MinMaxScaler()
# x_scaled = min_max_scaler.fit_transform(x)
# df = pd.DataFrame(x_scaled, columns=features)
#
# print(df)


# Using Pearson Correlation
plt.figure(figsize=(20, 20))
cor = df.corr()
sns.heatmap(cor, annot=True, center=0.0)
plt.savefig('focus_correlation_national.png')
plt.show()

# Correlation with output variable
cor_target = abs(cor["P_ISEV"])  # Selecting highly correlated features
relevant_features = cor_target[cor_target > 0.1]
print(relevant_features)
