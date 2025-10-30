def find_positions(arr):
    min_pos = arr.index(min(arr))  
    max_pos = arr.index(max(arr)) 
    return min_pos, max_pos

input_array = input()
array = eval(input_array)

if not isinstance(array, list):
    raise ValueError("Input is not a list")

if all(isinstance(x, (int)) for x in array):
    min_pos, max_pos = find_positions(array)
    print(f"{min_pos}, {max_pos}")
else: 
    print("Not Array, it is List.")