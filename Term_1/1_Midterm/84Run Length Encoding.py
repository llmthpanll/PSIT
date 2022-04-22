"""Run Length Encoding"""
def main():
    """Run Length Encoding"""
    txt = input()
    textchecker = txt[0]
    count = 0
    ans = ""
    for i in range(0, len(txt)):
        if textchecker == txt[i]:
            count += 1
        else:
            ans += str(count)+txt[i-1]
            textchecker = txt[i]
            count = 1
    ans += str(count)+txt[-1]#บวกชุดสุดท้าย
    print(ans)

main()
