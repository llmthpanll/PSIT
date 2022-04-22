"""[Midterm] Harshad"""
def loop(num):
    """บวกเลขทุกหลัก"""
    ans = 0
    num = str(num)
    if int(num) < 0:
        for i in num[1:]:
            ans += int(i)
        ans = ans*(-1)
    else:
        for i in num:
            ans += int(i)
    return ans
def main():
    """[Midterm] Harshad"""
    for _ in range(10):
        num = int(input())
        if num == 0:
            print("No")
        elif len(str(num)) == 1:
            if num%num == 0:
                print("Yes")
            else:
                print("No")
        else:
            if (num%loop(num)) == 0:
                print("Yes")
            else:
                print("No")
main()
