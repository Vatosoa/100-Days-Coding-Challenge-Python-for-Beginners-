def sum_list(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])

result = sum_list([1, 2, 3, 4, 5])
print(f"The sum is: {result}")
