print("------------- I am Your BMI ---------------")
weight = float(input("Enter your weight in kg\n"))
height = float(input("Enter your Height in meters\n"))

BMI = weight / height ** 2

print("Your BMI is " + str(BMI))