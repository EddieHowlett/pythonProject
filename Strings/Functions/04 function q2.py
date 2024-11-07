def calculate(num1:float,num2:float,operation:str):
    """

    :param num1: The first argument should be a number
    :param num2: The second argument should be a number
    :param operation: It should be either add, subtract, multiply, or divide
    :return: return a float output
    """
    if operation.lower() == "add":
        result = num1 + num2

    elif operation == "subtract":
        result = num1 - num2

    elif operation == "multiply":
        result = num1 * num2

    elif operation == "divide":
        result =  num1 / num2

    else:
        raise Exception
    return result

number_1 = float(input(f'Please enter the first number: '))
number_2 = float(input(f'Please enter the second number: '))
operation_input = input(f'please enter  either add, subtract, multiply, or divide: ')
result = calculate(number_1, number_2, operation_input)
print(f'You have entered number 1 as {number_1}')
print(f'You have entered number 2 as {number_2}')
print(f'The operation you want to apply is {operation_input} on {number_1} and {number_2}')
print(f'Your result is: {result}')