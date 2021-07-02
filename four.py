# Write a Python program to remove duplicates from a list.
def removeDuplicate(a):
    itemlist = []

    for i in a:
        if i not in itemlist:
            itemlist.append(i)
    return itemlist

a = [2, 3, 4, 4, 6, 7, 8, 9, 9, 2]

print(removeDuplicate(a))
