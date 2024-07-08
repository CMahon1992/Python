#Using Indexing to grab the 'e'
myString = "abcdefg"
print("The index of 4 in myString is " + myString[4]);

#using reverse indexing to grab the letter 'c'
print("The index of -5 in myString is " + myString[-5]);

#using start at index 3 and go all the way to the end by using [3:]
alphabet = "abcdefghijklmnop"
print(alphabet[3:]);

#stop index used grab up to a certain index using [:3]
print(alphabet[:3]);

#grabbing a subsection
print(alphabet[6:13]);

#index below is the start:stop:step
season = "sopuhymqwmioembrlo"
print("My birthday is in the " + season[0:16:3] +".")