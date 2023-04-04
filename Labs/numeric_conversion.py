# use substring for hex
import math

menu = '\nDecoding Menu\n-------------\n1. Decode hexadecimal\n2. Decode binary\n3. Convert binary to hexadecimal\n4. Quit\n'
print('Decoding Menu\n-------------\n1. Decode hexadecimal\n2. Decode binary\n3. Convert binary to hexadecimal\n4. Quit\n')


def main():

    while True:

        menu_choice = int(input('Please enter an option: '))

        if menu_choice == 1:
            arg = input('Please enter the numeric string to convert: ')
            print(f'Result:', hex_string_decode(arg))

        elif menu_choice == 2:
            arg = input('Please enter the numeric string to convert: ')
            print(f'Result:', binary_string_decode(arg))

        elif menu_choice == 3:
            arg = input('')

        elif menu_choice == 4:
            print('Goodbye!')
            exit()
        
        print(menu)


def binary_string_decode(my_str: str):
    cont_program = True
    n = -1
    binary_str_list = []
    binary_num_list = []
    power = 0

    while cont_program == True:

        if my_str == '':
            cont_program = False
            break

        if "0b" in my_str:
            my_str = my_str[2:]
        # removed prefix

        new_int = my_str[-1:]
        # finds the value of the next digit of the string

        binary_str_list.append(new_int)
        # adds the last number of the string to a list

        my_str = my_str[0:n]
        # removes the last digit from the string to avoid using same num twice

        binary_str_list = [int(i) for i in binary_str_list]
        # converts the strings in the list to ints

        new_val = (binary_str_list[-1] * 2 ** power)
        # gets the decimal value of new_int based on its position

        power += 1
        # increases power by one as the program iterates through the binary number

        binary_num_list.append(new_val)
        # adds the new value in decimal form to a list

    return (sum(binary_num_list))
    # prints the sum of the decimal numbers


def hex_string_decode(my_str: str):
    my_str = my_str.upper()
    cont_program = True
    n = -1
    hex_str_list = []
    hex_num_list = []
    power = 0
    # defined list

    while cont_program == True:

        if my_str == '':
            cont_program = False
            break

        if "0X" in my_str:
            my_str = my_str[2:]
        # removed prefix

        new_int = my_str[-1:]
        # finds the value of the next digit of the string

        hex_str_list.append(new_int)
        # adds the last number of the string to a list

        my_str = my_str[0:n]
        # removes the last digit from the string to avoid using same num twice

        hex_str_list = [array_nums(hex_str_list[-1])]
        # takes the substr given and converts to an int using array_nums

        new_val = (hex_str_list[-1] * 16 ** power)
        # gets the decimal value of new_int based on its position

        power += 1
        # increases power by one as the program iterates through the hex number

        hex_num_list.append(new_val)
        # adds the new value in decimal form to a list

    return sum(hex_num_list)
    # prints the sum of the decimal numbers

def hex_char_decode(my_str: str):
    my_str = my_str.upper()
    cont_program = True
    n = -1
    hex_str_list = []
    hex_num_list = []
    power = 0
    # defined list

    while cont_program == True:

        if my_str == '':
            cont_program = False
            break

        if "0X" in my_str:
            my_str = my_str[2:]
        # removed prefix

        new_int = my_str[-1:]
        # finds the value of the next digit of the string

        hex_str_list.append(new_int)
        # adds the last number of the string to a list

        my_str = my_str[0:n]
        # removes the last digit from the string to avoid using same num twice

        hex_str_list = [array_nums(hex_str_list[-1])]
        # takes the substr given and converts to an int using array_nums

        new_val = (hex_str_list[-1] * 16 ** power)
        # gets the decimal value of new_int based on its position

        power += 1
        # increases power by one as the program iterates through the hex number

        hex_num_list.append(new_val)
        # adds the new value in decimal form to a list

    return sum(hex_num_list)
    # prints the sum of the decimal numbers


def array_nums(a: str):
    str_list = ['0', '1', '2', '3', '4', '5', '6',
                '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    int_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    return int_list[str_list.index(a)]


if __name__ == '__main__':
    main()
