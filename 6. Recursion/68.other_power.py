def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        return power(base, exponent/2)**2
    else:
        return base * power(base, exponent//2)**2
    
result = power(2,3)
print(f"The result is: {result}")