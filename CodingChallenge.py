import sys

input_array = list(map(int, sys.argv[1].split(",")))
input_array.sort()
expected_sum = int(sys.argv[-1])

start_index = 0
end_index = len(input_array) - 1

while(start_index < end_index):
    if (input_array[start_index] + input_array[end_index]) == expected_sum:
        print("+ {}, {}".format(input_array[start_index], input_array[end_index], input_array[start_index] + input_array[end_index]))
        start_index += 1
        end_index -= 1
    elif (input_array[start_index] + input_array[end_index]) > expected_sum:
        end_index -= 1
    else:            
        start_index += 1
