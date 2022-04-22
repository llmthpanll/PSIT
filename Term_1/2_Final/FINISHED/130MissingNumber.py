"""MissingNumber"""
def main():
    """MissingNumber"""
    my_list = []
    check_list = []
    num = int(input())
    for i in range(num+1):
        check_list.append(i)
    for _ in range(num):
        num1 = int(input())
        my_list.append(num1)
        if num1 == 0:
            break
    my_list.sort()
    for i in my_list:
        check_list.remove(i)
    for i in check_list:
        print(i)
main()
