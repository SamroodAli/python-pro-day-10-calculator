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

result = 0
first_time_operation = True
continuing_operations = True

while continuing_operations:

    if first_time_operation:
        clear()
        first_time_operation=False
        num1 = float(input("Enter the first number\n"))
        # removing trailing single 0 if any
        if (num1*10) % 10==0:
            num1 = int(num1)
    else:
        num1 = result

    print("Enter the operator or c to clear and start again\ntype anything else to exit:\n")
    for key in operations:
        print(key,end=' ')
    operator = input('\n')

    if operator=='c':
        clear()
        result=0
        first_time_operation=True
        continue
    elif operator in operations:
        operation = operations[operator]
    else:
        clear()
        print("Thank you for using my calculator.")
        result = 0
        continuing_operations=False
        break

    num2 = float(input("Enter the next number\n"))
    # removing trailing single 0 if any
    if (num2*10) % 10==0:
        num2 = int(num2)

    result = operation(num1,num2)
    # removing trailing zero if results in a single zero decimal
    if (result*10) % 10==0:
        result = int(result)

    print(f"\n{num1} {operator} {num2} = {result}\n")
