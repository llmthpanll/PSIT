"""Sequence I"""
def main():
    """Sequence I"""
    num1 = int(input())
    num2 = int(input())
    count_num = num2
    col = 0
    for _ in range(0, num1):
        for i in range(col, num2):
            print(i+1, end=" ")
            col = i + 1
        num2 = num2 + count_num
        print("")
main()
