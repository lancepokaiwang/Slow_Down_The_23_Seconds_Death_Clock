import pymongo
import matplotlib.pyplot as plt
import numpy as np

client = pymongo.MongoClient("localhost", 27017)
db = client["data5000"]
collection = db["raw_data"]

results = []
years = []

prev = 0

types = ["01", "05", "06", "07", "08", "09", "10", "11", "14",
         "16", "17", "18", "19", "20", "21", "22", "23"]

numbers = []

for i in types:
    number = collection.count_documents({"V_TYPE": i})
    numbers.append(number)
    print("{}: {}".format(i, number))

# for i in range(1999, 2018):
#     result = collection.count_documents()
#
#     years.append(str(i))
#     results.append(result)
#
#     progress = 0
#     if prev != 0:
#         progress = ((result - prev) / prev) * 100
#         progress = round(progress, 2)
#     print("{}: {} ({}%)".format(i, result, progress))
#     prev = result

plt.bar(types, numbers)
plt.title("Collision of Vehicle Type (1999 - 2017)")
plt.xlabel("Vehicle Type No.")
plt.ylabel("Collision Number")
plt.show()

# plt.plot(years, results)
# plt.ylabel('Collision Number')
# plt.xlabel('Year')
# plt.xticks(rotation=40)
# plt.show()
