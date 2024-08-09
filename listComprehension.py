# the code takes each character from the string myString, appends it to a list, and prints it.
myString = 'hello'

mylist = []
for letter in myString:
    mylist.append(letter)
    print(letter)

mylist = [letter for letter in myString]
print(mylist)

newList = [firstName for firstName in 'Carleena']
print(newList)

numList = [num for num in range(0,11)]
print(numList)

square = [num**2 for num in range(0,11)]
print(square)

evenList = [x for x in range(0,11) if x%2==0]
print(evenList)

#returning values from celsius to fahrenheit
celcius = [0, 10, 20, 34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheit)

#nested loops in the list comprehension
newTask = []
for y in [2,4,6]:
    for z in [1,10,1000]:
        newTask.append(y*z)
        print(newTask)

updateNum = [a*b for a in [1,2,3] for b in [1, 10, 1000]]
print(updateNum)