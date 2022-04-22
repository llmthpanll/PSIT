"""binary"""
def main():
    """binary"""
    num = int(input())
    txt = ""
    if num == 0:
        txt += "0"
    while True:
        if num <= 0:
            break
        if num%2 == 0:
            txt += "0"
        else:
            txt += "1"
        num = num//2
    print(txt[::-1])
main()
