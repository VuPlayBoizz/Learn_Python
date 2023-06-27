#Step 1
with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)
#Step 2
import csv
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))
    print(temperature)
#Step 3
import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])
print(type(data)) # DataFrame
print(type(data["temp"])) #Series
#DataFrame
data_dict = data.to_dict()
print(data_dict)
#Series
temp_list = data["temp"].to_list()
print(temp_list)

print(data["temp"].mean())
print(data["temp"].max())

#Get Data in Columns
print(data["condition"]) # Series
print(data.condition) #DataFrames

#Get Data in Row
print(data[data.day == "Monday"])

#Get row with max temp
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

#Create a dataFrame from scratch

data_list = {
    "student" : ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}

list = pandas.DataFrame(data_list)
list.to_csv("new_data.csv")
print(list)