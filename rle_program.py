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
            print()

        elif option == 4:
            print()

        elif option == 5:
            print()

        elif option == 6:
            ConsoleGfx.display_image(current_image)
            print()

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

if __name__ == "__main__":
    main()

    

    