import pymongo
from sqlalchemy import *

host = "localhost"  # 輸入自己的 AWS RDS Enpoint 位址
port = 3306
dbname = "ns"  # 輸入自己設定的資料庫名稱
user = "root"  # 輸入自己設定的使用者名稱
password = ""  # 輸入自己設定的使用者密碼

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["data5000"]
mycol = mydb["ns_row"]


def checkValid(content):
    content = content.strip()
    if content is None: return False
    if content == '0': return False
    if content == 'Q': return False
    if content == 'U': return False
    if content == 'N': return False
    return True


# 連接資料庫
engine = create_engine('mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}' \
                       .format(user=user, password=password, host=host, port=port, dbname=dbname))
conn = engine.connect()
metadata = MetaData(engine)
# 選擇查詢的資料表
table = Table('row', metadata, autoload=True)
s = select([table])
result = conn.execute(s)
for row in result:
    valid_data = true
    data = {
        "C_YEAR": "20" + row[0][6:8],
        "C_MNTH": row[0][0:2],
        "light_condition": row[2].split(".")[0],
        "road_classification": row[3].split(".")[0],
        "severity": row[4].split(".")[0],
        "weather": row[5].split(".")[0],
        "road_surface": row[6].split(".")[0],
        "collision_config": row[7].split(".")[0]
    }

    for key, value in data.items():
        valid_data = checkValid(value)
        if valid_data:
            data[key] = int(data[key])
        else:
            break

    if valid_data:
        mycol.insert_one(data)
result.close()
