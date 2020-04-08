# importing libraries
import csv
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing

features = None
genders = []
types = []
combines = {}
with open('data/data_clean_v2.csv', newline='') as csvfile:
    index = 0
    rows = csv.reader(csvfile)
    for row in rows:
        if index == 0:
            features = row
        if index != 0:
            types.append(int(row[13]))
            genders.append(int(row[16]))

            # if (int(row[13])) not in types:
            #     types.append(int(row[13]))
            #
            # if (int(row[16])) not in genders:
            #     genders.append(int(row[16]))

            if (int(row[13]), int(row[16])) not in combines:
                combines[(int(row[13]), int(row[16]))] = 1
            else:
                combines[(int(row[13]), int(row[16]))] += 1
        index += 1

genders = np.array(genders)
types = np.array(types)
print(genders)
print(types)

rng = np.random.RandomState(0)

print(combines)
print(len(combines))

size = []
x = []
y = []
color = []



# for type in types:
#     for gender in genders:
#         x.append(type)
#         y.append(gender)
#         size.append(combines[(type, gender)] / 100)
#         color.append(np.random.rand(3,))
#
# labels = [x,y]
#
# # size = np.log2(size)
#
# print(size)
#
# plt.scatter(x, y, s=size, c=color, alpha=0.2)
# plt.xlabel("Types")
# plt.ylabel("Gender")
#
# plt.savefig('bubble_chart_national.png')
# plt.show()



plt.plot(types, genders, 'o', color='black')
plt.savefig('scatter_chart_national.png')
plt.show()
