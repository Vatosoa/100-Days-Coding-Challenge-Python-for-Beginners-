def sum_of_digits(num):
    if num < 10:
        return num
    else:
        return num % 10 + sum_of_digits(num//10)
    
result = sum_of_digits(12345)
print(result)