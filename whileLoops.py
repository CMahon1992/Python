x = 0

while x < 5:
    print(f'The current value of x = {x}')
    x = x + 1
else:
    print('X IS NO LONGER LESS THAN 5')

#using the pass statement
y = [1,2,3,4]

for test in y:
    #avoiding a syntax error
    pass
print('Script has ended')

#using he continue statement
name = 'Carleena '

#using the continue statement
#goes back to the top of the enclosing loop
for firstName in name:
    if firstName == 'a':
        continue
    print(firstName)

#using the break statement
#stops the loop
for firstName in name:
    if firstName == 'l':
        break
    print(firstName)

#using break in a while loop
z = 0
while z < 5:
    if z == 3:
        break
    print(f'{z} is less than 5')
    z +=1