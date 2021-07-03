# 1. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return the empty string.
string = input("Enter string:")
count = 0

if len(string) < 2:
    print("Empty String")
else:
    for i in string:
        print(i)            # Just for understanding loop
        count = count + 1

    new = string[0:2] + string[count - 2:count]
    print("New string is:", new)
