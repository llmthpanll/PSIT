""" Seeker """
def main():
    """ Seeker นะ ไม่ใช่ seeki ถ้าหนู sexy พี่"""
    text = input()
    check = ""
    ans = 0
    for i in text:
        if i.isdigit() == True:
            check += i
        else:
            if check == "":
                ans += 0
            else:
                ans += int(check)
                check = ""
    if check.isdigit() == True:
        print(ans + int(check))
    else:
        print(ans)
main()
