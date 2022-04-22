"""Regulation"""
def main():
    """Regulation"""
    aaa = input()
    bbb = float(input())
    ccc = input()
    print("%30s" %aaa)
    aaa = aaa.zfill(30)
    print("%s" %aaa)
    print("%.2f" %bbb)
    print("%.12f" %bbb)
    ccc = ccc.rjust(40, " ")
    print(ccc)
main()
