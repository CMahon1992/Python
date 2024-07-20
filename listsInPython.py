#creating a list
randomList = ['dogs',2,90.1,'cats']
print(randomList)
print(len(randomList))
print(randomList[0])
print(randomList[1:])

#joining two list together
secondList = ['penguin', 9, 30.1, 'kangaroo']
combinedList = randomList + secondList
print(combinedList)

#changing elements that are already in a list
randomList[0] = 'GOLDEN RETRIEVER'
print(randomList)

#adding to a List
randomList.append('apples')
print(randomList)

#removing an item from the list
print(secondList.pop())
print(secondList)

#removing element at a specific index
print(randomList.pop(2))
print(randomList)

#sorting a list
newList = [1,9,3,0,4,6,5]
print(newList)
newList.sort()
print(newList)

#reverse list
newList.reverse()
print(newList)
