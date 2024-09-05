def say_hello():
    print("Hello")
    print("How are you?")
say_hello()

def say_hello(name):
    print(f'Hello {name}')
say_hello('Olivia')

#if name is not provided, we can set a default
def say_hello(name = 'Stranger'):
    print(f'Hello {name}')
say_hello()


def add_num(num1,num2):
    return num1 + num2
result = add_num(6,8)
print(result)

def return_result(num3,num4):
    return num3 + num4
newResult = return_result(result,10)
print(newResult)