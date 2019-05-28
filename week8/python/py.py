def readthrough(array):
    newArray = []
    for i in range(0,len(array)):
        newArray.append(array[i])
    return newArray

print(readthrough("123"))

def func(n):
    if (n <= 1):
        return 1
    else:
        return 1 + (func(n - 1))

print(func(10))

def another(n):
    if (n <= 1):
        return 1
    else:
        return n + another(n - 1)

print(another(5))