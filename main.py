from replit import clear
from art import logo
# Calculator
# add
def add(n1,n2):
    """returning sum of num1 and num2"""
    return n1+n2

# subtract
def subtract(n1,n2):
    """returning subtraction of num2 from num1"""
    return n1-n2

# multiply
def multiply(n1,n2):
    """returning product of num1 and num2"""
    return n1*n2

# division
def divide(n1,n2):
    """returning result of division of num1 and num2"""
    return n1/n2


operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

def num_check(num):
    if num =='c':
        return calculator()
    try:
        num = float(num)
    except:
        new_num= input('not a valid number, please enter number again\nc=exit\n')
        num=num_check(new_num)

    if (num*10) % 10==0:
        num = int(num)
    return num

def calculator():
    """ a calculator function"""
    clear()
    print(logo)
    print('type c anytime to clear')
    
    result = input("Enter the first number\n")
    result = num_check(result)
    
    while True:
        valid_operator=False
        while not valid_operator:
            print("\nEnter the operator")
            for key in operations:
                print(key,end=' ')
            operator = input('\n')
            if operator =='c':
                return calculator()
            elif operator in operations:
                valid_operator=True
                operation = operations[operator]
            else:
                print('\nNot a valid operator.',end=' ')

        num2 = input("\nEnter the next number\n")
        num2 = num_check(num2)

        num1 = result
        result = operation(result,num2)
        # removing trailing zero if results in a single zero decimal
        if (result*10) % 10==0:
            result = int(result)

        print(f"""\n____________________________\n\n{num1} {operator} {num2} = {result}\n____________________________""")

# starting the calculator
calculator()