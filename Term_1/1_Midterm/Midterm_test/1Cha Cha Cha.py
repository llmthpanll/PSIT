"""ข้อ 1"""
import math
def main():
    """ข้อ 1"""
    day = int(input())
    i = 0
    ans = 0
    while True:
        if i == day:
            break
        i += 1
        hours = math.ceil(float(input()))
        ans += hours
    income = ans*8720
    print(income)
main()
