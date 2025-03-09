import csv
import pandas
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []                          #this will read the data from weather_data.csv
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print (temperatures)                               #this will print the data



data = pandas.read_csv("weather_data.csv")          # This is the same but it is more easier to use pandas to deal with csv files
# temp_list = data["temp"].to_list()                                 # This will print the temp col
#                                                     # so to print out any col we just write the name of the column
# total_temp = 0
# for temp_degree in temp_list:
#     total_temp += temp_degree

# average_degree = total_temp / len(temp_list)
# print(average_degree)

print(data[data.temp == data["temp"].max()])

#explaining this line : "data.temp = data["temp"]" because pandas make trans it to attribute "data["temp"].max()"
#is a method used to hold the max of series in pandas and i can also write it like that "data.temp.max()"
#now retrieve the data from "data variable" and print it




#now how to create a data frame from scratch

#lets try to create data frame from this dictionary
data_dict = {"students": ["Amy", "James", "Angela"],
             "scores": [76, 56, 65] 
             }

#thats how we done this task
new_data = pandas.DataFrame(data_dict)
print(new_data)

#i can also convert it to csv file after that
new_data.to_csv("MY_STUDENTS.csv")
