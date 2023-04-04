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




lst = [4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,8,7]
encoded = rle_compress(lst)
print(encoded)