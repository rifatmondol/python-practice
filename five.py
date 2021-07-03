# Write a Python function that takes two lists and returns True if they have at least one common member.
a = [1, 2, 3, 4, 5, 6, 7,8]
b = [7, 8, 9, 10, 15]

result = False

for i in a:
    for j in b:
        if i == j:
            result = True
print(result)

