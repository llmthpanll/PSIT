"""CoPrime"""
def main():
    """CoPrime"""
    num1 = int(input())
    num2 = int(input())
    check = 1
    for i in range(1, num1+1):
        if num1%i == 0 and num2%i == 0:
            check = i
    if check == 1:
        print("YES")
        print(check)
    else:
        print("NO")
        print(check)
main()
