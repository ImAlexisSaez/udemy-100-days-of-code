import pandas

data = pandas.read_csv("weather_data.csv")

print(type(data))
print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
avg_temp = sum(temp_list) / len(temp_list)
print(avg_temp)

# Mean with pandas
print(data["temp"].mean())

# Max
print(data["temp"].max())

# Get the columns with pandas
print(data.day)
print(data.temp)
print(data.condition)

# Get the data in a row
print(data[data.day == "Monday"])

# Get the row with max temp
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

print(monday.temp * 1.8 + 32)

# Create a dataframe from scratch
new_data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 66, 65],
}
new_data = pandas.DataFrame(new_data_dict)
print(new_data)
new_data.to_csv("new_data.csv")

