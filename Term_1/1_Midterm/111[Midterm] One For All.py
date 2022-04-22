"""[Midterm] One For All    """
def main():
    """[Midterm] One For All    """
    count = int(input())
    level = 0
    ans = ""
    for _ in range(count):
        txt = input()
        level += 1
        if level == count:
            ans += (txt+"_%d"%count)
        elif level % 2 == 0:
            ans += (txt+"-"*level)
        else:
            ans += (txt+"*"*level)
    print(ans)

main()
