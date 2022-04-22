"""Sequence III"""
import math
def main():
    """Sequence III"""
    num1 = int(input())
    num2 = math.ceil(num1/7)
    for _ in range(num2):
        for _ in range(7):
            if num1 < 1:
                break
            print(num1, end=" ")
            num1 -= 1
        print()
main()
