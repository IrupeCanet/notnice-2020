# Irupe Canet
# Weekly task number 7
# Write a program that reads in a text file
# and outputs the number of e's it contains.

with open ('mobydick.txt', 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter == e):
                    e = e + 1
print(e)                    



