# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string,
# if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
# Return the resulting string.
def not_poor(a):
    isNot = a.find('not')
    isPoor = a.find('poor')

    if isPoor > isNot and isNot > 0 and isPoor > 0:
        a = a.replace(a[isNot:(isPoor + 4)], 'good')
        return a
    else:
        return a


print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))








