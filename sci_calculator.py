# defining operand var as user inputs

import math

current_result = float(0)
menu = ('Calculator Menu\n'+'---------------\n'+'0. Exit Program\n'+'1. Addition\n'+'2. Subtraction\n' +
        '3. Multiplication\n'+'4. Division\n'+'5. Exponentiation\n'+'6. Logarithm\n'+'7. Display Average\n')
game_continue = True

print()
print('Current Result:', current_result)
print()

values = []

print(menu)

while game_continue == True:

    # asking for user input in order to operate on numbers
    operation = int(input('Enter Menu Selection: '))

    if operation not in range(0,8):
        print()
        print('Error: Invalid selection!')
        print()
        continue

    if operation == 0:
        print('Thanks for using this calculator. Goodbye!')
        exit()

    elif operation == 7:
        if len(values) == 0:
            print('Error: No calculations yet to average!')
            print()
            continue
        else:
            print('Sum of calculations:', sum(values))
            print('Number of calculations:', len(values))
            print('Average of calculations:',
                  round(sum(values)/len(values), 2))
            print()
        continue

    a = input('Enter first operand: ')
    operand_1 = current_result if a == 'RESULT' else float(a)

    a = input('Enter second operand: ')
    operand_2 = current_result if a == 'RESULT' else float(a)

    # using if/else/elif functions to perform operation on operands

    if operation == 1:
        current_result = operand_1 + operand_2
        values.append(operand_1 + operand_2)
        game_continue == True

    elif operation == 2:
        current_result = operand_1 - operand_2
        values.append(operand_1 - operand_2)
        game_continue == True

    elif operation == 3:
        current_result = operand_1 * operand_2
        values.append(operand_1 * operand_2)
        game_continue == True

    elif operation == 4:
        current_result = operand_1 / operand_2
        values.append(operand_1 / operand_2)
        game_continue == True

    elif operation == 5:
        current_result = operand_1 ** operand_2
        values.append(operand_1 ** operand_2)
        game_continue == True

    elif operation == 6:
        current_result = (math.log(operand_2, operand_1))
        values.append(math.log(operand_2, operand_1))
        game_continue == True

    else:
        print('Error: Invalid selection!')
        continue

    print('\nCurrent Result:',  current_result, '\n')

    print(menu)
