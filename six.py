# Create a custom count function using for loop
x = [1, 2, 3, 2, 4, 2]
count = 0
for i in x:
    if i == 2:
        count += 1
print("Result:", count)