import pymongo
import csv

client = pymongo.MongoClient("localhost", 27017)
db = client["data5000"]

collection_data = db['national_clean_v2']
collection_data_v3 = db['national_clean_v3.5']

collisions = collection_data.find()

datas = []

for collision in collisions:
    id = collision["_id"]
    case_id = collision["C_CASE"]
    collision_obj = collision
    master_collisions = collection_data.find({"C_CASE": case_id, "P_PSN3": 1, "V_ID": 1, "P_ID": 1})
    for master_collision in master_collisions:
        # print(master_collision)
        collision_obj["CAR_AGE_MASTER"] = master_collision["CAR_AGE"]
        collision_obj["P_SEX_MASTER"] = master_collision["P_SEX"]
        collision_obj["P_AGE_MASTER"] = master_collision["P_AGE"]
        datas.append(collision_obj)
    # print("=================================================")

collection_data_v3.insert_many(datas)