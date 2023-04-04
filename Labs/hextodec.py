def main():
    
    cont_program = True
    n = -1
    hex_str_list = []
    hex_num_list = []
    power = 0
        #defined list
    
    my_str = input("hi")
    

    while cont_program == True:
    
        if my_str == '':
            cont_program = False
            break
        
        my_str = my_str.removeprefix('0x')
        #removed prefix
        
        new_int = my_str[-1:]
        #finds the value of the next digit of the string

        hex_str_list.append(new_int)
        #adds the last number of the string to a list

        my_str = my_str[0:n]
        #removes the last digit from the string to avoid using same num twice

        hex_str_list = [array_nums(hex_str_list[-1])]
        #takes the substr given and converts to an int using array_nums

        new_val = (hex_str_list[-1] * 16 ** power)
        #gets the decimal value of new_int based on its position 
        
        power += 1
        #increases power by one as the program iterates through the hex number 

        hex_num_list.append(new_val)
        #adds the new value in decimal form to a list
    
    print(sum(hex_num_list))
    #prints the sum of the decimal numbers

def array_nums(a:str):
    str_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8' '9', 'A', 'B', 'C', 'D', 'E', 'F']
    int_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    return int_list[str_list.index(a)+1]
    
main()