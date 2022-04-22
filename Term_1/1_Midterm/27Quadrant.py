"""Quadrant"""
def main():
    """Quadrant"""
    num1 = int(input())
    num2 = int(input())
    if num1 > 0 and num2 > 0:
        print("Q1")
    elif num1 > 0 and num2 < 0:
        print("Q4")
    elif num1 < 0 and num2 > 0:
        print("Q2")
    elif num1 < 0 and num2 < 0:
        print("Q3")
    elif num2 == 0 and num1 != 0:
        print("X")
    elif num1 == 0 and num2 != 0:
        print("Y")
    elif num1 == 0 and num2 == 0:
        print("O")
main()
