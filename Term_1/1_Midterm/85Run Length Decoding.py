"""Run Length Decoding"""
def main():
    """Run Length Decoding"""
    txt = input()
    txt2 = txt
    ans = ""
    for i in txt2:
        if not i.isdigit():
            txt2 = txt2.replace(i, " ")
    txt3 = txt2.split(" ")
    txt3 = [i for i in txt3 if i] #txt3ตัวเลขเฉยๆ

    for i in txt:
        if i.isdigit():
            txt = txt.replace(i, " ")
    txt1 = txt.split(" ")
    txt1 = [i for i in txt1 if i] #txt1ตัวอักษรอย่างเดียว)

    for i in range(len(txt1)):
        ans += txt1[i]*int(txt3[i])
    print(ans)

main()
