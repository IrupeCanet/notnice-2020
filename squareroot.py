#Irupe Canet
# Weekly task number 6.
# Write a program that takes a positve floating 
# number as imput and outputs an aproximation of its square root.

import numpy as np
import cmath as cm
import sys

#get number from user

try:
    number = float (input("Please enter a number: "))
    

if number < 0:
    # c_number = complex number
    c_number = cm.sqrt(complex(number, 0))
    print(c_number)
    # r_number = rounded number
    r_number = np.around(c_number, decimals=1)
    print ("Aproximation of square root is: ", r_number, "Because is a complex number")

else:
    number = np.sqrt(number)
    print("Square root of provided number is: ", number)

