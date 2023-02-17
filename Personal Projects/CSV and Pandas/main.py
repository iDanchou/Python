# with open("Personal Projects\CSV and Pandas\weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv

# with open("Personal Projects\CSV and Pandas\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     print(data)
#     for row in data:
#         # print(row)
#         # print(row[1])  # WILL PRINT EVERYTHING WITHIN THE TEMPERATURE ROW
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas  # Better formatting and easier to use

data = pandas.read_csv("weather_data.csv")
# # print(data)
# # print(data["temp"])
#
# # data_dict = data.to_dict()
# # print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# # average = sum(temp_list) / len(temp_list)
# # print(average)
#
# print(data["temp"].mean())
#
# print(data["temp"].max())  # BOTH COMMANDS ARE THE SAME
# print(data.temp.max())
#
# # GET DATA IN COLUMNS
print(data.condition)

# HOW TO GET DATA IN THE ROWS
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
print(monday.day)
print(monday.temp)


def ctof(temp):
    new_temp = temp * 1.8 + 32
    return new_temp


print(ctof(int(monday.temp)))

# CREATE A DATAFRAME FROM SCRATCH
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
