def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
num= 4
print(f"The factoria of {num} is {factorial(num)}") 