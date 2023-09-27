# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def fibonacci(num):
    fib_sequence = [0,1]
    while len(fib_sequence) < num:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

result = fibonacci(10)
print(result)