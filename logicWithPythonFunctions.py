def check_even(number):
    return number % 2
print(check_even(10))

#Return true if any number in the list is even
def check_even_list(num_list):
    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass
    return False
print(check_even_list([1,9,7,2]))
print(check_even_list([1,1,1,1,1]))


#Return all even numbers list
def check_even_list(num_list):
    #   return all the even numbers in the list

    #placeholder variables
    even_numbers = []
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers
print(check_even_list([1,9,7,84,2]))
print(check_even_list([1,1,1,1,1,6]))