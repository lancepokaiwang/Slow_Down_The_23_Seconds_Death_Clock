import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client["data5000"]
collection_raw_data = db["raw_data"]
collection_clean_data = db["data_clean"]


def checkValid(content):
    content = content.strip()
    if content is None: return False
    if content == 'U': return False
    if content == 'UU': return False
    if content == 'UUUU': return False
    if content == 'X': return False
    if content == 'XX': return False
    if content == 'XXXX': return False
    if content == 'Q': return False
    if content == 'QQ': return False
    if content == 'N': return False
    if content == 'NN': return False
    if content == 'NNNN': return False
    return True


batch = []
batch_count = 0
for data in collection_raw_data.find():
    # print(data)
    del data['_id']

    if data['P_PSN'] == '99':
        data['C_RCFG'] = '0'
        data['V_TYPE'] = '0'
        data['V_YEAR'] = '0000'
        if data['P_SAFE'] == 'NN' or data['P_SAFE'] == 'QQ' or data['P_SAFE'] == 'UU' or data['P_SAFE'] == 'XX':
            data['P_SAFE'] = '0'

    validObject = True
    for features, value in data.items():
        if not checkValid(value): validObject = False
    if validObject:
        batch.append(data)
        batch_count += 1

    if batch_count == 100000:
        print("Insert 1 batch...")
        collection_clean_data.insert_many(batch)
        batch_count = 0
        batch = []

if len(batch) != 0:
    print(batch)
    collection_clean_data.insert_many(batch)
    batch_count = 0
    batch = []

print("Insert Job Complete!")
