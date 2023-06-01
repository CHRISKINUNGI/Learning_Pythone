#convert the tuple into a list, change the list, and convert the list back into a tuple.This will add items to the tuple

myTuple = (1, 2, 3, 4)
myList = list(myTuple)
myList.append(5)
myTuple = tuple(myList)

print(myTuple)
