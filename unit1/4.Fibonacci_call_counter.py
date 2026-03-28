count = 0   # global counter

def fibonacci(n):
    global count
    count += 1   # count each function call

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Example
n = 5
result = fibonacci(n)

print("Fibonacci(", n, ") =", result)
print("Total function calls:", count)
