"""Tax"""
def main():
    """Tax"""
    num1 = int(input())
    num2 = int(input())
    ans = 0
    realans = 0
    if num2 <= 600:
        ans += ((num2)*0.5)
    elif num2 <= 1800:
        ans += ((num2 - 600)*1.50) + 300
    elif num2 > 1800:
        ans += ((num2 - 1800)*4) + 2100
    if num1 == 6:
        realans = ans*0.9
    elif num1 == 7:
        realans = ans*0.8
    elif num1 == 8:
        realans = ans*0.7
    elif num1 == 9:
        realans = ans*0.6
    elif num1 >= 10:
        realans = ans*0.5
    if num1 <= 5:
        print("%.2f "%ans)
    elif num1 >= 6:
        print("%.2f" %realans)
main()
