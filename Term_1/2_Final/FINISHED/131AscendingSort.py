"""AscendingSort"""
def main():
    """AscendingSort"""
    my_list = []
    for _ in range(5):
        num1 = int(input())
        my_list.append(num1)
    my_list.sort()
    for i in my_list:
        print(i)
main()
