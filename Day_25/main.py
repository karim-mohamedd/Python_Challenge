import pandas

# There are 2 concepts called  "Dictionary Comprehension and list Comprehension" they allows you to create new list or dictionary 
# from an existing list or dictionary

# list = [1,2,3,4]
# new_list = [item*2 for item in list if condition]

# How to loop through dictionary
student_dict = {
    "student": ["karim", "mohamed", "ahmed"],
    "score" : [76, 80, 90]
}

print(student_dict.items())
for (key, value) in student_dict.items():
    print(key)

student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)

# #loop through dataframe
# for (key, value) in student_dataframe.items():
#     print(key)
#     print(value)

# This way is not useful so that pandas has it's own built in function called "iterrows()" that is much better

for (index, row) in student_dataframe.iterrows():
    print(row) #each of the rows is a panda series