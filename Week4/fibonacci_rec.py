def fibonacci(n):
    if n < 2:
        return n
    fib = fibonacci(n. - 1) + fibonacci(n - 2)
    return fib


n = int(input())
print(fibonacci(n))
