"""Sequence IV"""
def main():
    """Sequence IV"""
    num = int(input())
    count_num = num
    col = 0
    for _ in range(0, num):
        for i in range(col, num):
            print(i+1, end=" ")
            col = i + 1
        num = num + count_num
        print("")
main()
