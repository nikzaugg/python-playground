def factorial(n):
    print("factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        result = n * factorial(n-1)
        print("intermediate result for ", n, " * factorial(" ,n-1, "): ",result)
        return result  

# main Program
factorial_n = factorial(5)
print factorial_n


def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
# main Program
fibonacci_n = fibonacci(10)
print fibonacci_n