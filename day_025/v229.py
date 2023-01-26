import pandas

data = pandas.read_csv("squirrel_data.csv")

# print(data["Primary Fur Color"].unique())

grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

squirrel_fur = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [
        grey_squirrel_count,
        red_squirrel_count,
        black_squirrel_count
    ],
}

squirrel_fur = pandas.DataFrame(squirrel_fur)
squirrel_fur.to_csv("squirrel_fur.csv")