# Irupe Canet
# Control Flow.
# Weekly task number 4.
# Program that ask the user imput an integer
# and output values of a calculation.

n = int (input("Please enter a positive integer:"))

# number = n

# check if n is even
while n != 1:
    if n % 2 == 0:
        n = int (n / 2)
        print(n)
    
    else:
        n = int ((n * 3) + 1)
        print(n)
        

    