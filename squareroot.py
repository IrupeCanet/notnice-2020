#Irupe Canet
# Weekly task number 6.
# Write a program that takes a positve floating 
# number as imput and outputs an aproximation of its square root.

import numpy as np
import cmath as cm
import sys

#get number from user

try:
    number = float (input("Please enter number; "))

if  number < 0:
    # c number = complex number
    c number = cm.sqrt(complex(number, 0))
    print(c number)
    # r number = rounded number
    r number = np.around(c number, decimals=1)
    print ("Aproximation of square root is: ", r number, "Because is a complex number")

else:
    number = np.sqrt(number)
    print("Square root of provided number is: ", number)

