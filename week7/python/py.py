def indexOf(array,value): #Take an array, and a value to search for
    try:
        return array.index(value) #Try to return the index
    except:
        return -1 #If that fails, return -1


print(indexOf(["1","2","3"],"3"))

print(indexOf(["1","2","3"],"4"))