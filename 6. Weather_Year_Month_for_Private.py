import pymongo
import numpy as np
import matplotlib.pyplot as plt

client = pymongo.MongoClient("localhost", 27017)
db = client["data5000"]
collection = db["raw_data"]

weather_types = ["1", "2", "3", "4", "5", "6", "7"]

for year in range(2016, 2018):
    year_result = []
    for month in range(1, 13):
        query = {"V_TYPE": "01", "C_YEAR": "{}".format(year), "C_MNTH": "{}".format(month).zfill(2)}
        # print(query)
        result = collection.find(query)

        weathers = {}
        for data in result:
            if data["C_WTHR"] not in weathers:
                weathers[data["C_WTHR"]] = 1
            else:
                weathers[data["C_WTHR"]] += 1
        print(weathers)
        year_result.append(weathers)

    print(year_result)

    weather_results = []
    for object in year_result:
        object_result = []
        for w_type in weather_types:
            if w_type in object:
                object_result.append(object[w_type])
        weather_results.append(object_result)

    # data = [
    #     [5., 25., 50., 20.],
    #     [4., 23., 51., 17.],
    #     [6., 22., 52., 19.]
    # ]

    color_list = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12']
    gap = .8 / len(weather_results)
    for i, row in enumerate(weather_results):
        X = np.arange(len(row))
        plt.bar(
            X + i * gap,
            row,
            width=gap,
            color=color_list[i % len(color_list)]
        )
    plt.xlabel("Weather Type")
    y_pos = np.arange(len(weather_types))
    plt.xticks(y_pos, weather_types)
    plt.title("{}".format(year))
    plt.show()