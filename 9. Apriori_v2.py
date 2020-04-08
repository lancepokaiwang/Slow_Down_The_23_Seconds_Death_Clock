from apyori import apriori
import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client["data5000"]
collection_data = db['national_clean_v5_match']

def loadDataSet():
    row_data = collection_data.find()
    return_data = []
    for data in row_data:
        arr = [
            "C_YEAR" + str(data['C_YEAR']), "C_MNTH" + str(data['C_MNTH']), "C_WDAY" + str(data['C_WDAY']),
            "C_HOUR" + str(data['C_HOUR']), "C_WTHR" + str(data['C_WTHR']), "C_RSUR" + str(data['C_RSUR']),
            "C_RALN" + str(data['C_RALN']), "C_TRAF" + str(data['C_TRAF']), "V_TYPE" + str(data['V_TYPE']),
            "P_SEX" + str(data['P_SEX']), "P_AGE" + str(data['P_AGE']), "P_PSN1" + str(data['P_PSN1']),
            "P_PSN2" + str(data['P_PSN2']), "P_PSN3" + str(data['P_PSN3']), "P_PSN4" + str(data['P_PSN4']),
            "P_SAFE" + str(data['P_SAFE']), "P_ISEV" + str(data['P_ISEV']), "V_AGE" + str(data['V_AGE']),
            "M_V_AGE" + str(data['M_V_AGE']),
            "M_P_SEX" + str(data['M_P_SEX']), "M_P_AGE" + str(data['M_P_AGE']),
            "M_P_ISEV" + str(data['M_P_ISEV'])
        ]
        return_data.append(arr)

    return return_data


data = loadDataSet()

association_rules = apriori(data, min_support=0.16, min_confidence=0.2, min_lift=3, max_length=2)
association_results = list(association_rules)

for item in association_results:
    pair = item[0]
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])
    print("Support: " + str(item[1]))
    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")
