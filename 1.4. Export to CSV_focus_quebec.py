import random
import pandas as pd
import pymongo
import csv
import numpy as np


def random_index(rate):
    """随机变量的概率函数"""
    #
    # 参数rate为list<int>
    # 返回概率事件的下标索引
    start = 0
    index = 0
    randnum = random.randint(1, sum(rate))

    for index, scope in enumerate(rate):
        start += scope
        if randnum <= start:
            break
    return index


client = pymongo.MongoClient("localhost", 27017)
db = client["data5000"]
collection_clean_data = db["quebec"]

df = pd.read_csv('data/quebec/rapports-accident-2017.csv', header=0)

datas = []
with open('data/quebec/data_clean_quebec_focus_v5.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([
        "C_MNTH", "C_SEV", "C_RCFG", "C_WTHR", "C_RSUR",
        "C_RALN", "C_TRAF", "V_TYPE", "P_SEX", "P_AGE", "P_PSN", "P_ISEV",
        "P_SAFE", "CAR_AGE"
    ])

    for index, row in df.iterrows():
        data = {}
        C_YEAR = int(row['DT_ACCDN'][0:4])
        # C_MNTH
        data["C_MNTH"] = int(row['DT_ACCDN'][5:7])
        # C_SEV
        if row["gravite"] == "Mortel" or row["gravite"] == "Grave" or row["gravite"] == "Léger":
            data["C_SEV"] = 1
        else:
            data["C_SEV"] = 2
        # C_RCFG
        if row["TP_REPRR_ACCDN"] == 1:
            data["C_RCFG"] = 2
        else:
            data["C_RCFG"] = 1
        # C_WTHR
        print(row["CD_COND_METEO"])
        if row["CD_COND_METEO"].is_integer():
            data["C_WTHR"] = int(row["CD_COND_METEO"])
        else:
            data["C_WTHR"] = None
        # C_RSUR
        if row["CD_ETAT_SURFC"] == 11:
            data["C_RSUR"] = 1
        elif row["CD_ETAT_SURFC"] == 12:
            data["C_RSUR"] = 2
        elif row["CD_ETAT_SURFC"] == 13:
            data["C_RSUR"] = 9
        elif row["CD_ETAT_SURFC"] == 14:
            data["C_RSUR"] = 6
        elif row["CD_ETAT_SURFC"] == 15:
            data["C_RSUR"] = 4
        elif row["CD_ETAT_SURFC"] == 16:
            data["C_RSUR"] = 3
        elif row["CD_ETAT_SURFC"] == 17:
            data["C_RSUR"] = 5
        elif row["CD_ETAT_SURFC"] == 18:
            data["C_RSUR"] = 5
        elif row["CD_ETAT_SURFC"] == 19:
            data["C_RSUR"] = 6
        elif row["CD_ETAT_SURFC"] == 20:
            data["C_RSUR"] = 8
        else:
            data["C_RSUR"] = None
        # C_RALN
        if row["CD_ASPCT_ROUTE"] == 11:
            data["C_RALN"] = 1
        elif row["CD_ASPCT_ROUTE"] == 12:
            data["C_RALN"] = 2
        elif row["CD_ASPCT_ROUTE"] == 13:
            data["C_RALN"] = 2
        elif row["CD_ASPCT_ROUTE"] == 14:
            data["C_RALN"] = 2
        elif row["CD_ASPCT_ROUTE"] == 21:
            data["C_RALN"] = 3
        elif row["CD_ASPCT_ROUTE"] == 22:
            data["C_RALN"] = 4
        elif row["CD_ASPCT_ROUTE"] == 23:
            data["C_RALN"] = 4
        elif row["CD_ASPCT_ROUTE"] == 24:
            data["C_RALN"] = 4
        else:
            data["C_RALN"] = None
        # C_TRAF
        arr = [18, 1, 3]
        rate = [55, 32, 13]
        data["C_TRAF"] = arr[random_index(rate)]
        # V_TYPE
        if int(row["nb_automobile_camion_leger"]) > 0:
            data["V_TYPE"] = 1
        else:
            data["V_TYPE"] = None
        # P_SEX
        arr = [1, 0]
        rate = [54, 46]
        data["P_SEX"] = arr[random_index(rate)]
        # P_AGE
        data["P_AGE"] = 37
        # P_PSN
        data["P_PSN"] = 1
        # P_ISEV
        if row["gravite"] == 'Mortel':
            data["P_ISEV"] = 3
        elif row["gravite"] == 'Serious':
            data["P_ISEV"] = 2
        elif row["gravite"] == 'Léger':
            data["P_ISEV"] = 2
        elif row["gravite"] == 'Dommages matériels seulement':
            data["P_ISEV"] = 1
        elif row["gravite"] == 'Dommages matériels inférieurs au seuil de rapportage':
            data["P_ISEV"] = 1
        else:
            data["P_ISEV"] = None
        # P_SAFE
        data["P_SAFE"] = 2
        # CAR_AGE
        data["CAR_AGE"] = 7

        if data["P_ISEV"] is not None and data["V_TYPE"] is not None and data["C_WTHR"] is not None and data["C_RSUR"] is not None and data["C_RALN"] is not None and data["V_TYPE"] is not None:
            datas.append(data)
            writer.writerow([
                data['C_MNTH'], data['C_SEV'],
                data['C_RCFG'], data['C_WTHR'], data['C_RSUR'],
                data['C_RALN'], data['C_TRAF'], data['V_TYPE'],
                data['P_SEX'], data['P_AGE'], data['P_PSN'], data['P_ISEV'],
                data['P_SAFE'], data['CAR_AGE']
            ])


collection_clean_data.insert_many(datas)
print("job complete!")
