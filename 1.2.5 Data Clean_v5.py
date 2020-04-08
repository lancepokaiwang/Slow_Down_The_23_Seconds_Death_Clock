import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client["data5000"]
collection_raw_data = db["raw_data"]
collection_clean_data = db["national_clean_v5"]


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

    if data['P_SEX'] == 'M':
        data['P_SEX'] = '1'
    elif data['P_SEX'] == 'F':
        data['P_SEX'] = '0'

    if data['V_TYPE'] == 'NN':
        data['V_TYPE'] = '24'

    validObject = True
    for features, value in data.items():
        if not checkValid(value): validObject = False
    if validObject:
        # C_YEAR
        data['C_YEAR'] = int(data['C_YEAR'])
        # C_MNTH
        data['C_MNTH'] = int(data['C_MNTH'])
        if data['C_YEAR'] == 12 or data['C_YEAR'] == 1 or data['C_YEAR'] == 2:
            data['C_YEAR'] = 1
        elif data['C_YEAR'] == 3 or data['C_YEAR'] == 4 or data['C_YEAR'] == 5:
            data['C_YEAR'] = 2
        elif data['C_YEAR'] == 6 or data['C_YEAR'] == 7 or data['C_YEAR'] == 8:
            data['C_YEAR'] = 3
        elif data['C_YEAR'] == 9 or data['C_YEAR'] == 10 or data['C_YEAR'] == 11:
            data['C_YEAR'] = 4
        # C_WDAY
        data['C_WDAY'] = int(data['C_WDAY'])
        if data['C_WDAY'] <= 4:
            data['C_WDAY'] = 1
        elif data['C_WDAY'] >= 5:
            data['C_WDAY'] = 2
        # C_HOUR
        data['C_HOUR'] = int(data['C_HOUR'])
        if data['C_HOUR'] < 6:
            data['C_HOUR'] = 1
        elif 6 <= data['C_HOUR'] < 12:
            data['C_HOUR'] = 2
        elif 12 <= data['C_HOUR'] < 18:
            data['C_HOUR'] = 3
        elif 18 <= data['C_HOUR'] < 24:
            data['C_HOUR'] = 4
        # C_SEV
        data['C_SEV'] = int(data['C_SEV'])
        # C_VEHS
        data['C_VEHS'] = int(data['C_VEHS'])
        if data['C_VEHS'] <= 10:
            data['C_VEHS'] = 1
        elif 10 < data['C_VEHS'] <= 30:
            data['C_VEHS'] = 2
        elif 30 < data['C_VEHS'] <= 70:
            data['C_VEHS'] = 3
        elif 70 < data['C_VEHS']:
            data['C_VEHS'] = 4
        # C_CONF
        data['C_CONF'] = int(data['C_CONF'])
        if data['C_CONF'] <= 6:
            data['C_CONF'] = 1
        elif 20 < data['C_CONF'] <= 30:
            data['C_CONF'] = 2
        elif 30 < data['C_CONF'] <= 40:
            data['C_CONF'] = 3
        elif 40 < data['C_CONF']:
            data['C_CONF'] = 4
        # C_RCFG
        data['C_RCFG'] = int(data['C_RCFG'])
        if data['C_RCFG'] == 1:
            data['C_RCFG'] = 1
        elif data['C_RCFG'] == 2 or data['C_RCFG'] == 3:
            data['C_RCFG'] = 2
        elif data['C_RCFG'] == 4:
            data['C_RCFG'] = 3
        elif data['C_RCFG'] == 5:
            data['C_RCFG'] = 4
        elif data['C_RCFG'] == 6:
            data['C_RCFG'] = 5
        elif data['C_RCFG'] == 7:
            data['C_RCFG'] = 6
        elif data['C_RCFG'] == 8:
            data['C_RCFG'] = 7
        elif data['C_RCFG'] == 9:
            data['C_RCFG'] = 8
        elif data['C_RCFG'] == 10 or data['C_RCFG'] == 11 or data['C_RCFG'] == 12:
            data['C_RCFG'] = 9
        # C_WTHR
        data['C_WTHR'] = int(data['C_WTHR'])
        # C_RSUR
        data['C_RSUR'] = int(data['C_RSUR'])
        # C_RALN
        data['C_RALN'] = int(data['C_RALN'])
        if data['C_RALN'] == 1 or data['C_RALN'] == 2:
            data['C_RALN'] = 1
        elif data['C_RALN'] == 3 or data['C_RALN'] == 4:
            data['C_RALN'] = 2
        elif data['C_RALN'] == 5 or data['C_RALN'] == 6:
            data['C_RALN'] = 3
        # C_TRAF
        data['C_TRAF'] = int(data['C_TRAF'])
        # V_ID
        data['V_ID'] = int(data['V_ID'])
        # V_TYPE
        data['V_TYPE'] = int(data['V_TYPE'])
        # V_YEAR
        data['V_YEAR'] = int(data['V_YEAR'])
        # V_AGE
        data['V_AGE'] = data['C_YEAR'] - data['V_YEAR']
        if data['V_AGE'] < 0: data['V_AGE'] = 0
        if data['V_AGE'] <= 4:
            data['V_AGE'] = 1
        elif 5 <= data['V_AGE'] <= 12:
            data['V_AGE'] = 2
        elif 13 <= data['V_AGE']:
            data['V_AGE'] = 3
        # P_ID
        data['P_ID'] = int(data['P_ID'])
        # P_SEX
        data['P_SEX'] = int(data['P_SEX'])
        # P_AGE
        data['P_AGE'] = int(data['P_AGE'])
        if data['P_AGE'] <= 25:
            data['P_AGE'] = 1
        elif 25 < data['P_AGE'] <= 46:
            data['P_AGE'] = 2
        elif data['P_AGE'] > 46:
            data['P_AGE'] = 3
        # P_PSN1
        data['P_PSN'] = int(data['P_PSN'])

        data['P_PSN1'] = 0
        if data['P_PSN'] == 11:
            data['P_PSN1'] = 1
        elif 11 < data['P_PSN'] <= 33:
            data['P_PSN1'] = 2
        elif 96 <= data['P_PSN'] <= 98:
            data['P_PSN1'] = 3
        elif data['P_PSN'] == 99:
            data['P_PSN1'] = 4
        # P_PSN2
        data['P_PSN2'] = 0
        if data['P_PSN'] == 11:
            data['P_PSN2'] = 1
        elif 11 < data['P_PSN'] <= 13:
            data['P_PSN2'] = 2
        elif 21 <= data['P_PSN'] <= 33:
            data['P_PSN2'] = 3
        elif 96 <= data['P_PSN'] <= 98:
            data['P_PSN2'] = 4
        elif data['P_PSN'] == 99:
            data['P_PSN2'] = 5
        # P_PSN3
        data['P_PSN3'] = 0
        if 11 <= data['P_PSN'] <= 13:
            data['P_PSN3'] = 1
        elif 21 <= data['P_PSN'] <= 33:
            data['P_PSN3'] = 2
        elif 96 <= data['P_PSN'] <= 98:
            data['P_PSN3'] = 3
        elif data['P_PSN'] == 99:
            data['P_PSN3'] = 4
        # P_PSN4
        data['P_PSN4'] = 0
        if data['P_PSN'] == 11 or data['P_PSN'] == 21 or data['P_PSN'] == 31:
            data['P_PSN4'] = 1
        elif data['P_PSN'] == 12 or data['P_PSN'] == 22 or data['P_PSN'] == 32:
            data['P_PSN4'] = 2
        elif data['P_PSN'] == 13 or data['P_PSN'] == 23 or data['P_PSN'] == 33:
            data['P_PSN4'] = 3
        elif 96 <= data['P_PSN'] <= 98:
            data['P_PSN4'] = 4
        elif data['P_PSN'] == 99:
            data['P_PSN4'] = 5

        del data['P_PSN']
        # P_ISEV
        data['P_ISEV'] = int(data['P_ISEV'])
        # P_SAFE
        data['P_SAFE'] = int(data['P_SAFE'])
        if data['P_SAFE'] == 1:
            data['P_SAFE'] = 1
        elif 2 <= data['P_SAFE'] <= 12:
            data['P_SAFE'] = 2
        elif data['P_SAFE'] == 13:
            data['P_SAFE'] = 3
        # P_USER
        data['P_USER'] = int(data['P_USER'])
        if data['P_USER'] == 1 or data['P_USER'] == 2:
            data['P_USER'] = 1
        elif data['P_USER'] == 3:
            data['P_USER'] = 2
        elif data['P_USER'] == 4:
            data['P_USER'] = 3
        elif data['P_USER'] == 5:
            data['P_USER'] = 4
        # C_CASE
        data['C_CASE'] = int(data['C_CASE'])

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
