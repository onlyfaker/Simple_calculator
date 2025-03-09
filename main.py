import os

from art import LOGO
print(LOGO)
def sum(a,b):
    sumup = a+b
    return sumup

def sub(a,b):
    subtract = a - b
    return subtract

def multi(a,b):
    multiply = a*b
    return multiply

def div(a,b):
    divide = a/b
    return divide

looping=True
while looping:
    num1 = float(input("What's the first number: "))
    loop_until_again_is_no = True
    while loop_until_again_is_no==True:
        operation = input("""    +
    -
    *
    /
Pick an operation: """ )
        num2 = float(input("What's the next number: "))
        if operation=='+':
            print(f'{num1} {operation} {num2} = {sum(num1,num2)}')
            num1 = sum(num1,num2)
        elif operation=='-':
            print(f'{num1} {operation} {num2} = {sub(num1,num2)}')
            num1 = sub(num1,num2)
        elif operation=='*':
            print(f'{num1} {operation} {num2} = {multi(num1,num2)}')
            num1 = multi(num1,num2)
        elif operation=='/':
            print(f'{num1} {operation} {num2} = {div(num1,num2)}')
            num1 = div(num1,num2)

        again = input(f"To continue with current number {num1} type 'y' or 'n' "
                      f"to start a new calculation(to exit - 'e'): ").lower()
        if again == 'n':
            print('\n' * 20)
            break
        elif again=='y':
            continue
        elif again=='e':
            looping=False
            break





