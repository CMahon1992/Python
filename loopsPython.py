#loops are used to iterate over each object
myList = [1,2,3,4,5,6,7,8,9,10]

for num in myList:
    print(num)

#prints hello 10 times
for greeting in myList:
    print("hello")

#print even number. 
for number in myList:
    if number % 2 == 0:
        print(number)
    else:
        print(f'Odd Number: {number}')

list_sum = 0
for addNum in myList:
    list_sum = list_sum + addNum
    print(list_sum) #running tally
    
print(list_sum) #total

#looping through a string
myString = "Hello World "

for printString in myString:
    print(printString)

#another way to loop through a string

for state in "New York ":
    print(state)

#if you do not intend to use the variable name, use underscore. Corgi will print out the length of the string puppies
for _ in "puppies":
    print("Corgi")

#loop through tuple
tup = (1,2,3)
for row in tup:
    print(row)

tupList = [(1,2),(3,4),(5,6),(7,8),(9,10)]
for x in tupList:
    print(x)

#tuple unpacking. To do this pass in the variable as the same structure
for (a,b) in tupList:
    print(a)
    print(b)

#iterating through a dictionary
baseball = {'k1':'Yankees','k2':'Mets','k3':'Redsox'}
#this will print the keys by default
for teams in baseball:
    print(teams)

#to get key value pairs for dictionary, append .items 
for teams in baseball.items():
    print(teams)

#another way to print values
for value in baseball.values():
    print(value)