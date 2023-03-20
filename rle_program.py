from console_gfx import ConsoleGfx

cont_program = True

def main():

    print('Welcome to the RLE image encoder!')
    print()
    print('Displaying Spectrum Image: ')
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)

    print()
    print()
    print('RLE Menu')
    print('--------')
    print('0. Exit')
    print('1. Load File')
    print('2. Load Test Image')
    print('3. Read RLE String')
    print('4. Read RLE Hex String')
    print('5. Read Data Hex String')
    print('6. Display Image')
    print('7. Display RLE String')
    print('8. Display Hex RLE Data')
    print('9. Display Hex Flat Data')
    print()

    current_image = []
    while cont_program == True:

        option = int(input('Select a Menu Option: '))

        if option == 0:
            exit()
    
        elif option == 1:
            filename = input('Enter name of file to load: ')
            current_image = ConsoleGfx.load_file(filename)
            print()

        elif option == 2:
            current_image = ConsoleGfx.test_image
            print('Test image data loaded.')
            print()

        elif option == 3:
            image_data = (input('Enter an RLE string to be decoded: '))
            current_image = string_to_rle(image_data)
            print()

        elif option == 4:
            image_data = input('Enter the hex string holding RLE data: ')
            new_format = string_to_data(image_data)
            current_image = decode_rle(new_format)
            print()

        elif option == 5:
            image_data = input('Enter the hex string holding RLE data: ')
            current_image = string_to_data(image_data)
            print()

        elif option == 6:
            ConsoleGfx.display_image(current_image)

        elif option == 7:
            print()

        elif option == 8:
            print()

        elif option == 9:
            print()

        else:
            print('Error!')


def to_hex_string(numbers):
    hex_digits = "0123456789abcdef"
    hex_string = ""
    for num in numbers:
        if num // 16 == 0:
            hex_string += hex_digits[num % 16]
        else:
            hex_string += hex_digits[num // 16] + hex_digits[num % 16]
    return hex_string

def count_runs(list):
    runs = 0
    previous_num = None
    consecutive_nums = 0
    for num in list:
        if num == previous_num:
            consecutive_nums += 1
        if consecutive_nums == 15:
                runs += 1
                consecutive_nums = 0
                previous_num = num  
        if num != previous_num:
                runs += 1
                previous_num = num
    return runs


def encode_rle(flat_data):
    encoded_list = []
    i = 0
    while i < len(flat_data):
        value = flat_data[i]
        run_length = 1
        while i + run_length < len(flat_data) and run_length < 15 and flat_data[i+run_length] == value:
            run_length += 1
        encoded_list.extend([run_length, value])
        i += run_length
    return encoded_list

def get_decoded_length(encoded_lst):
    decoded_list = []
    for i in range(0, len(encoded_lst), 2):
        count = encoded_lst[i]
        num = encoded_lst[i+1]
        for j in range(count):
            decoded_list.append(num)
    return len(decoded_list)


def decode_rle(rle_data):
    decoded_list = []
    i = 0
    while i < len(rle_data):
        num_of_repeats = rle_data[i]
        value = rle_data[i+1]
        decoded_list.extend([value] * num_of_repeats)
        i += 2
    return decoded_list

def string_to_data(data_string):
    hex_digits = "0123456789abcdef"
    decimal_list = []
    for i in data_string:
        if i in hex_digits:
            decimal_list.append(int(i, 16))
    return decimal_list

def to_rle_string(rle_data:list):

    hex_digits = "0123456789abcdef"
    end_list = ''
    count = 1

    for i in rle_data:
        if count % 2 == 0:
            if i // 16 == 0:
                end_list += str(hex_digits[i % 16])
                count += 1
                rle_data = rle_data[1:]
                if len(rle_data) > 0:
                    end_list += ':'
            else:
                end_list += str(hex_digits[i // 16] + hex_digits[i % 16])
                count += 1
                rle_data = rle_data[1:]
                if len(rle_data) > 0:
                    end_list += ':'
        else:
            end_list += str(i)
            count += 1
            rle_data = rle_data[1:]
  
    return(end_list)

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



if __name__ == "__main__":
    main()

    

    