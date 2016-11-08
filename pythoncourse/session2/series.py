def fibonacci(n):
    """Establish non 0 bases and then find value at n"""
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)

# Test to print 5th value of Fib sequence #

#print(fibonacci(5))


def lucas(n):
    """Establish non 0 bases and then find value at n"""
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)

def sum_series():
    dummy





