def main():

    passkey = input('Please enter your 8 digit passcode: ')
    
    print(encode_pass(passkey))

    print(decode_pass(encode_pass(passkey)))
    

def encode_pass(passkey):
    
    num_list = ''
    
    for i in passkey:
        temp_num = int(i) + 3
        if temp_num > 10 :
            temp_num -= 10
            num_list += str(temp_num)
        else:
            num_list += str(temp_num)
        
    return num_list

def decode_pass(passkey):

    num_list = ''

    for i in passkey:
        temp_num = int(i) - 3
        if temp_num < 0:
            temp_num += 10
            num_list += str(temp_num)
        else:
            num_list += str(temp_num)

    return num_list

if __name__ == '__main__':
    main()
