import csv
import Basic_Functions as bfs
import pymongo

# client = pymongo.MongoClient("mongodb://lancewang:lancewang@datascience-shard-00-00-v3ugi.mongodb.net:27017,datascience-shard-00-01-v3ugi.mongodb.net:27017,datascience-shard-00-02-v3ugi.mongodb.net:27017/test?ssl=true&replicaSet=DataScience-shard-0&authSource=admin&retryWrites=true&w=majority")
client = pymongo.MongoClient("localhost", 27017)
db = client["data5000"]
collection = db["raw_data"]

with open('data/raw_data.csv', newline='') as csvfile:
    index = 0
    rows = csv.reader(csvfile)
    features = None
    batch = []
    batch_count = 0
    for row in rows:
        if index == 0:
            features = row
        if index != 0:
            data = {}
            for i in range(0, len(row)):
                data[features[i]] = row[i]
            batch.append(data)
            batch_count += 1

        if batch_count == 100000:
            print(batch)
            collection.insert_many(batch)
            batch_count = 0
            batch = []
        index += 1

    if len(batch) != 0:
        print(batch)
        collection.insert_many(batch)
        batch_count = 0
        batch = []

    print("Insert Job Complete!")

