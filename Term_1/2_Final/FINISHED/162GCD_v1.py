"""GCD_v1"""
def main():
    """GCD_v1"""
    num1 = int(input())
    num2 = int(input())
    for i in range(100000, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            print(i)
            break
main()
