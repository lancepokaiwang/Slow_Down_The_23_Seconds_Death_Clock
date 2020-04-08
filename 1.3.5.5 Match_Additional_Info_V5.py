import pymongo
import csv

client = pymongo.MongoClient("localhost", 27017)
db = client["data5000"]

collection_data = db['national_clean_v5']
collection_data_v5 = db['national_clean_v5_match']

collisions = collection_data.find()

datas = []

for collision in collisions:
    del collision['_id']
    case_id = collision["C_CASE"]
    collision_obj = collision
    master_collisions = collection_data.find({"C_CASE": case_id, "P_PSN1": 1, "V_ID": 1, "P_ID": 1}, {'_id': 0})
    for master_collision in master_collisions:
        collision_obj['M_V_TYPE'] = master_collision["V_TYPE"]
        collision_obj['M_V_AGE'] = master_collision["V_AGE"]
        collision_obj['M_P_AGE'] = master_collision["P_AGE"]
        collision_obj['M_P_SEX'] = master_collision["P_SEX"]
        collision_obj['M_P_ISEV'] = master_collision["P_ISEV"]
        collision_obj['M_P_SAFE'] = master_collision["P_SAFE"]

        # print(master_collision)
        datas.append(collision_obj)

collection_data_v5.insert_many(datas)
