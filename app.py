import csv
with open("./Output/weather_data.csv") as r:
    y = csv.reader(r)
    temperatures = []
    for row in y:
        if row[1] != "temp":
            x = temperatures.append(row[1])
    print(temperatures)












