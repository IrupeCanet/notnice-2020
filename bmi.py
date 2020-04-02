# This program will calculate your Body Mass Index
# based on your weight and height.

weight = float (input("Enter your weight in Kg:"))
height = float (input("Enter your heigh in metres:"))

# weight = 65.0
# height = 180.0

bmi = (weight / (height**2)) *10000

print("Your Body Mass Index is:", round (bmi, 2))

