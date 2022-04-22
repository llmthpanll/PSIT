"""Gcd"""
def gcd_euclidean(num1, num2):
    """func"""
    while num2 != 0:
        num1, num2 = num2, num1%num2
    print("%d" %num1)
gcd_euclidean(float(input()), float(input()))
