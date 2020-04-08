import random
import pandas as pd
import pymongo
import csv


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
collection_clean_data = db["ns_row"]

results = collection_clean_data.find({}, {'_id': 0})

datas = []
with open('data/ns/data_clean_ns_focus.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([
        "C_YEAR", "C_MNTH", "LightCondition", "RoadClassification", "P_ISEV", "C_WTHR", "C_RSUR",
        "C_CFIG"
    ])

    for row in results:
        writer.writerow([
            row['C_YEAR'], row['C_MNTH'], row['light_condition'],
            row['road_classification'], row['severity'],
            row['weather'], row['road_surface'], row['collision_config']
        ])


# collection_clean_data.insert_many(datas)
print("job complete!")
