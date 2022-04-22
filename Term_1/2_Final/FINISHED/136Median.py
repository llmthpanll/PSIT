"""median"""
import math
def main():
    """median"""
    mid = 0
    count_list = int(input())
    my_list = []
    for _ in range(count_list):
        num = int(input())
        my_list.append(num)
    my_list.sort()    # [256, 276, 357, 421, 527, 532, 601, 831, 986, 1015]
    if count_list % 2 == 0:
        mid = math.ceil(count_list/2)
        real_ans = (my_list[mid-1] + my_list[mid])/2
        print("%.1f" %(real_ans))
    elif count_list % 2 == 1:
        mid = math.ceil(count_list/2)
        print("%.1f" %(my_list[mid-1]))
main()
