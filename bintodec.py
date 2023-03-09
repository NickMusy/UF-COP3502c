def main():

    cont_program = True
    my_str = input('enter your binary number: ')
    n = -1
    binary_str_list = []
    binary_num_list = []
    power = 0
        #defined list
    

    while cont_program == True:
    
        if my_str == '':
            cont_program = False
            break
        
        my_str = my_str.removeprefix('0b')
        #removed prefix
        
        new_int = my_str[-1:]
        #finds the value of the next digit of the string

        binary_str_list.append(new_int)
        #adds the last number of the string to a list

        my_str = my_str[0:n]
        #removes the last digit from the string to avoid using same num twice
        
        binary_str_list = [int(i) for i in binary_str_list]
        #converts the strings in the list to ints

        new_val = (binary_str_list[-1] * 2 ** power)
        #gets the decimal value of new_int based on its position 
        
        power += 1
        #increases power by one as the program iterates through the binary number 

        binary_num_list.append(new_val)
        #adds the new value in decimal form to a list
    
    print(sum(binary_num_list))
    #prints the sum of the decimal numbers

main()    
