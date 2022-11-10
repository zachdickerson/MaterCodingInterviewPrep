def palindromeNum(x):

    y = str(x)

    if y == y[::-1]:
        return True
    else:
        False

print(palindromeNum(10))
print(palindromeNum(121))
print(palindromeNum(-121))