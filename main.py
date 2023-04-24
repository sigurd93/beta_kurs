import random

def add_numbers(num1, num2):
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1
    else:
        return add_numbers(num1-1, num2-1) + 2
    
print(add_numbers(10, 4))

def divide(num1, num2):
    return(num1/num2)
        
print(divide(10, 5))