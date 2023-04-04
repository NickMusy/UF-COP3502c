'''
to_rle_string(rle_data)
Translates RLE data into a human-readable representation. 
For each run, in order, it should display the runlength in decimal (1-2 digits);
the run value in hexadecimal (1 digit); and a delimiter, ‘:’, between runs. (See
examples in standalone section.)
Ex: to_rle_string([15, 15, 6, 4]) yields string "15f:64".

8. string_to_rle(rle_string)
Translates a string in human-readable RLE format (with delimiters) into RLE byte data. (Inverse of #7)
Ex: string_to_rle("15f:64") yields list [15, 15, 6, 4].

need to add something that uses %2 after adding to list to know if delimiter needs to be added in str and can be used
to determine if the num should be in decimal or hex

for #8, need to first separate the string into shorter strings in between colons
then translate smaller strings from hex to decimal

should return a list of ints


need to determine if object in list has only one 


'''
list_1 = ('15f:64')


def string_to_rle(rle_string:str):

    num = 1
    decimal_list = []
    new_list = rle_string.split(':')
    
    run_list = [i[:-1] for i in new_list]
    hex_num_val = [i[-1:] for i in new_list]
    
    for i in hex_num_val:
        decimal_num = int(i, 16)
        decimal_list.append(decimal_num)

    for i in decimal_list:
        run_list.insert(num, i)
        num += 2
    
    run_list = [int(i) for i in run_list]

    return(run_list)

string_to_rle(list_1)
