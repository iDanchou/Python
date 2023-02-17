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

import pandas

pandas.read_csv(weather_data.csv)
