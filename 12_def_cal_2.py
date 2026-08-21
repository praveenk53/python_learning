#Simple calculator using functions
#Create 4 functions: add(a, b), subtract(a, b), multiply(a, b), divide(a, b)
#Each function should return the result
#Ask user for two numbers and an operation, then call the appropriate function and print the result

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul (x,y):
    return x*y
def div(x,y):
    return x/y
a = int(input("enter the first number : "))
b = int(input("enter the second number: "))
op = input("enter the operator , ex : (+ , - , * , / ) ")
if op == "+":
    result = add(a,b)
elif op == "-":
    result = sub(a,b)
elif op == "*":
    result = mul(a,b)
elif op == "/":
    result = div(a,b)
else:
    print("invalid input ")
print("result is :  ", result )
