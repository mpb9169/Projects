def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    if len(lst) == 2:
        return lst[0] if lst[0] > lst[1] else lst[1]
    
    mid = len(lst) // 2
    left_max = find_max(lst[:mid])
    right_max = find_max(lst[mid:])
    
    return left_max if left_max > right_max else right_max


userinput = input("Enter numbers separated by spaces: ")
numbers = [float(x) for x in userinput.split()]

if not numbers:
    print("No numbers entered.")
else:
    print(f"Max value: {find_max(numbers)}")