# Python program to find largest
# number in a list

number = [2, 4, 3, 6, 8, 20, 9]
print("Largest number is:", max(number))    # First method using build in function

print("*" * 25)

max = number[0]
for i in number:
    if i > max:
        max = i
print("Largest number is:", max)            # Second method without build in function
