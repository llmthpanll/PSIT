"""ข้อ 6"""
import math
def main():
    """ข้อ 6"""
    less_day = 0
    ex1 = int(input())
    ex2 = int(input())
    ex3 = int(input())
    ex4 = int(input())
    ex1_perday = int(input())
    ex2_perday = int(input())
    ex4_perday = int(input())
    ex3_perday = int(input())
    allday_ex1 = math.ceil(ex1/ex1_perday)
    allday_ex2 = math.ceil(ex2/ex2_perday)
    allday_ex3 = math.ceil(ex3/ex3_perday)
    allday_ex4 = math.ceil(ex4/ex4_perday)
    if less_day < allday_ex1:
        less_day = allday_ex1
    if less_day < allday_ex2:
        less_day = allday_ex2
    if less_day < allday_ex3:
        less_day = allday_ex3
    if less_day < allday_ex4:
        less_day = allday_ex4
    print(less_day)
main()
