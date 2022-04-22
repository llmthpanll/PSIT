"""[Midterm] Diginity"""
def loop(num):
    """[Midterm] บวกไปจนกว่าจะเหลือตัวเดียว"""
    ans = 0
    for i in num:
        ans += int(i)
    if len(str(ans)) != 1:
        ans = loop(str(ans))
    return ans
def main():
    """[Midterm] Diginity"""
    while True:
        num = input()
        ans = 0
        if num == "0":
            break
        else:
            ans = loop(num)
            print(ans)

main()
