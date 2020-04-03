#Irupe Canet
# Weekly task number 7
# Write a program that reads the file "moby-dick.txt"
# and outputs the number of e's it contains.

with open ('mobydick.txt', 'r') as f:
    string = f.read()
    count = string.count("e")
print(count)



