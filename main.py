from replit import clear
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


def calculator():
    """ a calculator function"""
    clear()
    result = float(input("Enter the first number\n"))
        # removing trailing single 0 if any
    if (result*10) % 10==0:
        result = int(result)
    
    while True:
        print("\nEnter the operator")
        for key in operations:
            print(key,end=' ')
        print("\nc = clear and start again \ntyping anything else will exit")
        operator = input('\n')

        if operator =='c':
            return calculator()
        elif operator in operations:
            operation = operations[operator]
        else:
            clear()
            return

        num2 = input("\nEnter the next number or x to exit\n")
        if num2 =="x":
            clear()
            print("Thank you for using my calculator")
            return
        else:
            num2=float(num2)
        
        # removing trailing single 0 if any
        if (num2*10) % 10==0:
            num2 = int(num2)

        num1 = result
        result = operation(result,num2)
        # removing trailing zero if results in a single zero decimal
        if (result*10) % 10==0:
            result = int(result)

        print(f"""\n____________________________\n\n{num1} {operator} {num2} = {result}\n____________________________""")

# starting the calculator
calculator()