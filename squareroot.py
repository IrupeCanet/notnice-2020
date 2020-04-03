#Irupe Canet
# Weekly task number 6.
# Write a program that takes a positve floating 
# number as imput and outputs an aproximation of its square root.

import numpy as np
import math as mt
import cmath as cm
import sys

#get number from user

if number < 0:
    c number = cm.sqrt(complex(number, 0))
    print(c number)
    r number = np.around(c number, decimals=1)
    print ("Aproximation of square root is: ", r number)
else:
    number = mt.sqrt(number)
    print("Square root of provided number is: ", number)
    
        