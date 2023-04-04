final_sum = 0

curr_value = int(input())

while curr_value > 0:
    final_sum = final_sum + curr_value
    curr_value = int(input())

print(f'Sum: {final_sum}')