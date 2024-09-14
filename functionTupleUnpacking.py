stock_prices = [('APPL',200),('GOOG',400),('MSFT',100)]
for item in stock_prices:
    print(item)

print()
    

for ticker,price in stock_prices:
    print(price+0.1*price)

print()

#Which employee will be employee of the month based on hours worked
work_hours = [('Abby', 100), ('Billy', 400), ('Cassie', 800)]

def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    # Move the return statement outside of the loop
    return (employee_of_month, current_max)

# Call the function and print the result
result = employee_check(work_hours)
print(result)

#tuple unpacking with a function call
name, hours = employee_check(work_hours)
print(name)

print()

#purposely producing an error
name, hours, location = employee_check(work_hours)