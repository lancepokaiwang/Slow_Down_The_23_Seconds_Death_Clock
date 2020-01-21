import pymongo
import matplotlib.pyplot as plt
import numpy as np

client = pymongo.MongoClient("localhost", 27017)
db = client["data5000"]
collection = db["raw_data"]

results = []
years = []

prev = 0
for i in range(1999, 2018):
    result = collection.count_documents({"C_YEAR": "{}".format(i)})

    years.append(str(i))
    results.append(result)

    progress = 0
    if prev != 0:
        progress = ((result - prev) / prev) * 100
        progress = round(progress, 2)
    print("{}: {} ({}%)".format(i, result, progress))
    prev = result

plt.plot(years, results)
plt.ylabel('Collision Number')
plt.xlabel('Year')
plt.xticks(rotation=40)
plt.show()
