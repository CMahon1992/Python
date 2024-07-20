#using .format() method is a good way to format objects into strings for print statements

print ("I {}".format('printed') + ' a string.')

#submitting strings in the same order I supplied them.
print ("Supplied Order: The {} {} {}".format('fox','quick','brown'))

#submitting strings based off index position
print ("Reordered based on index position: The {1} {2} {0}".format('fox','quick','brown'))

#assigning key words as variable names
print ("Using Key Words: The {q} {b} {f}".format(f='fox',q='quick',b='brown'))

#Float Formatting: allows you to adjust width and position of floating point number
# "{value:width.precisionf}" width represents white space and precision represent decimal places
result = 100/777
print("The result is {}".format(result))

print("The formatted result is {r:10.3f}".format(r=result))

#f string literals
name = "Carleena"
print(f"My name is {name}")

middleName = "Winter"
season = "Summer"
print(f"Her middle name is {middleName} but her birthday is in the {season}.")