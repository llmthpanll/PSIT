"""SumOfNumber"""
def main():
    """SumOfNumber"""
    my_num = []
    num_check = int(input())
    while True:
        num = int(input())
        if num == -1:
            break
        my_num.append(num)
        num_all = sum(my_num)
        if num_all == num_check:
            break
    print(num_all)
main()
