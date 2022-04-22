"""LineSorting"""
def main():
    """LineSorting"""
    num = int(input())
    my_list = []
    for _ in range(num):
        my_list.append(input())
    my_list.sort(key=len)
    print(my_list)
    for i in my_list:
        print(i)
    for i in range(len(my_list)):
        ans = my_list.pop()
        print(ans)
main()
