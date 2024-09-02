# Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
newST = st.split()
print(newST)

for letter in newST:
    if letter.startswith("s"):
        print(letter)

#use range() to print all the even numbers from 0 to 10

for checkNum in range(0,10):
    if checkNum % 2 == 0:
        print(checkNum)

#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3
divisibleByThree = [divisible for divisible in range(1,50) if divisible % 3 == 0]
print(divisibleByThree) 

#Go through the string below and of the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
stLength = st.split()
print(stLength)

for word in stLength:
    if len(word) % 2 == 0:
        print(f'{word} is even')


#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of
#the number, and for the multiples of five print "Buzz". For numbers which are mutiples of both three and
# five print "FizzBuzz" 

for program in range(1,100):
    if program  % 3 == 0 and program % 5 == 0:
        print('FizzBuzz')
    elif program % 3 == 0:
        print('Fizz')
    elif program % 5 == 0:
        print('Buzz')
    else:
        print(program)

#Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
first_letters = [word[0] for word in st.split()]
print(first_letters)