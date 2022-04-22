"""fib"""
def fib(num):
    """fib"""
    return fib(num-1) + fib(num-2) if num not in (0, 1) else num
print(fib(int(input())))
