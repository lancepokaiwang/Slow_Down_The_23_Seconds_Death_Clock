import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

features = None

df = pd.read_csv('data/quebec/data_clean_quebec_focus_v5.csv', header=0)
df = df.drop("P_SAFE", 1)
df = df.drop("P_PSN", 1)
df = df.drop("P_SEX", 1)
df = df.drop("P_AGE", 1)
df = df.drop("V_AGE", 1)
df = df.drop("C_TRAF", 1)
df = df.drop("V_TYPE", 1)
# df = df.drop("nb_camionLourd_tractRoutier", 1)
# df = df.drop("nb_outil_equipement", 1)
# df = df.drop("nb_tous_autobus_minibus", 1)
# df = df.drop("nb_bicyclette", 1)
# df = df.drop("nb_cyclomoteur", 1)
# df = df.drop("nb_motocyclette", 1)
# df = df.drop("nb_taxi", 1)
# df = df.drop("nb_urgence", 1)
# df = df.drop("nb_motoneige", 1)
# df = df.drop("nb_VHR", 1)
# df = df.drop("nb_autres_types", 1)
# df = df.drop("nb_veh_non_precise", 1)


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
plt.savefig('focus_correlation_quebec.png')
plt.show()

# Correlation with output variable
cor_target = abs(cor["P_ISEV"])  # Selecting highly correlated features
relevant_features = cor_target[cor_target > 0.1]
print(relevant_features)
