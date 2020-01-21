import pymongo
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import date2num

client = pymongo.MongoClient("localhost", 27017)
db = client["data5000"]
collection = db["raw_data"]

results = []
years = []

prev = 0

types = ["01", "11", "17", "23"]

# 公交、斯加、bike


numbers = []

pub = []
pri = []
bik = []
stcar = []

years = []

for year in range(1999, 2018):
    years.append(year)
    # pri.append(collection.count_documents({"V_TYPE": "01", "C_YEAR": "{}".format(year)}))
    # pub.append(collection.count_documents({"V_TYPE": "11", "C_YEAR": "{}".format(year)}))
    # bik.append(collection.count_documents({"V_TYPE": "17", "C_YEAR": "{}".format(year)}))
    stcar.append(collection.count_documents({"V_TYPE": "23", "C_YEAR": "{}".format(year)}))

    print(year)

print(pub)
print(pri)
print(bik)

# plt.bar(years, pri)
# plt.title("PRIVATE")
# plt.show()
#
# plt.bar(years, pub)
# plt.title("PUBLIC")
# plt.show()
#
# plt.bar(years, bik)
# plt.title("BIKE")
# plt.show()

plt.bar(years, stcar)
plt.title("Street Car")
plt.show()

# x = date2num(years)
#
# ax = plt.subplot(111)
# ax.bar(x-0.2, pri, width=0.2, color='b', align='center')
# ax.bar(x, pub, width=0.2, color='g', align='center')
# ax.bar(x+0.2, bik, width=0.2, color='r', align='center')
# ax.xaxis_date()
#
# plt.show()
