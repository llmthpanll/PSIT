"""Day2011"""
def main():
    """Day2011"""
    my_day = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
    day_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    all_day = 0
    day = int(input())     #วันที่ 1
    month = int(input())   #เดือน 3
    for i in range(month):
        all_day += day_in_month[i]
    all_day = all_day + day
    print(my_day[all_day%7])
main()
