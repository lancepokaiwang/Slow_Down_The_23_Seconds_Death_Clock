import pymongo
import csv

client = pymongo.MongoClient("localhost", 27017)
db = client["data5000"]
collection_clean_data = db["data_clean"]

collection_national_v3 = db['national_clean_v5_match']

with open('data/data_clean_focus_v5.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([
        "C_YEAR", "C_MNTH", "C_WDAY", "C_HOUR", "C_SEV", "C_VEHS", "C_CONF", "C_RCFG", "C_WTHR", "C_RSUR",
        "C_RALN", "C_TRAF", "V_ID", "V_TYPE", "V_YEAR", "V_AGE", "P_ID", "P_SEX", "P_AGE", "P_PSN1", "P_PSN2", "P_PSN3", "P_PSN4",
        "P_ISEV", "P_SAFE", "P_USER", "C_CASE", "M_V_TYPE", "M_V_AGE", "M_P_AGE", "M_P_SEX", "M_P_ISEV", "M_P_SAFE"
    ])

    # for data in collection_national_v3.find({'P_ISEV': {'$in': [2, 3]}}):
    for data in collection_national_v3.find():
        # Write data to CSV
        writer.writerow([
            int(data["C_YEAR"]), int(data["C_MNTH"]), int(data["C_WDAY"]), int(data["C_HOUR"]),
            int(data["C_SEV"]), int(data["C_VEHS"]), int(data["C_CONF"]), int(data["C_RCFG"]),
            int(data["C_WTHR"]), int(data["C_RSUR"]), int(data["C_RALN"]), int(data["C_TRAF"]),
            int(data["V_ID"]), int(data["V_TYPE"]), int(data["V_YEAR"]), int(data["V_AGE"]),
            int(data["P_ID"]), int(data["P_SEX"]), int(data["P_AGE"]), int(data["P_PSN1"]),
            int(data["P_PSN2"]), int(data["P_PSN3"]), int(data["P_PSN4"]), int(data["P_ISEV"]),
            int(data["P_SAFE"]), int(data["P_USER"]), int(data["C_CASE"]), int(data["M_V_TYPE"]),
            int(data["M_V_AGE"]), int(data["M_P_AGE"]), int(data["M_P_SEX"]), int(data["M_P_ISEV"]), int(data["M_P_SAFE"])
        ])

    print("job complete!")
