"""3nPlus1"""
def main():
    """3nPlus1"""
    ans = 0
    while True:
        num = int(input())
        while True:
            if num == 1:
                ans += 1
                print(ans)
                ans = 0
                break
            elif num%2 == 0:
                num = num/2
                ans += 1
            else:
                num = (num*3) + 1
                ans += 1
            if num == 0:
                break
        if num == 0:
            break
main()
