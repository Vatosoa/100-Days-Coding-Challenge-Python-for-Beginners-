import math

def is_perfect_square(num):
    sqrt = math.isqrt(num)
    print(sqrt)
    return sqrt * sqrt == num

num = 25
print(is_perfect_square(num))