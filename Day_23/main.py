import pandas, csv
RED = "Cinnamon"
GRAY = "Gray"
BLACK = "Black"
data = pandas.read_csv("4. 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrel_count = len(data[data["Primary Fur Color"] == GRAY])
red_squirrel_count = len(data[data["Primary Fur Color"] == RED])
black_squirrel_count = len(data[data["Primary Fur Color"] == BLACK])


#now i manged to get the data i need it is time to construct data frame
#First i have to turn it into dictionary
data_dict =  {"Fur Color" : [GRAY, RED, BLACK],
              "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]}

#Then we can create our dataframe
DATA_FRAME = pandas.DataFrame(data_dict)

#When i create the DataFrame i can easily create csv file or whatever by the methods of pandas
DATA_FRAME.to_csv("squirrel_count.csv")