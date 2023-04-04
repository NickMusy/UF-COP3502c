#defining operand var as user inputs
operand_1 = float(input('Enter first operand:'))
operand_2 = float(input('Enter second operand:'))

#printing the menu for the calculator
print('Calculator Menu')
print('---------------')
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')

#asking for user input in order to operate on numbers
operation = int(input('Which operation do you want to perform? '))

#using if/else/elif functions to perform operation on operands
if operation == 1:
    print('The result of the operation is', operand_1 + operand_2, '. Goodbye! ')
elif operation == 2:
    print('The result of the operation is', operand_1 - operand_2, '. Goodbye! ')
elif operation == 3:
    print('The result of the operation is', operand_1 * operand_2, '. Goodbye! ')
elif operation == 4:
    print('The result of the operation is', operand_1 / operand_2, '. Goodbye! ')
else:
    print('Error: Invalid selection! Terminating program.')