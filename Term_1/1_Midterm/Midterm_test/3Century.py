"""ข้อ 3"""
import math
def main():
    """ข้อ 3"""
    amount_year = int(input())
    i = 0
    while True:
        if i == amount_year:
            break
        i += 1
        year = input()
        txt = year.find("B.E. ")
        if txt == 0:
            year = year.replace("B.E. ", "")
            year = int(year) - 543
        elif txt == -1:
            year = year.replace("A.D. ", "")
            year = int(year)
        if year < 0:
            print("ERROR")
        else:
            print(math.ceil(year/100))
main()
