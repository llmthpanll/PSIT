"""Matrix_MN"""
def main(num1, num2):
    """Matrix_MN"""
    num0 = num1*num2
    list1 = []
    for _ in range(num0):
        num = int(input())
        list1.append(num)
    for i in range(1, num0 +1):
        print(list1[i-1], end=" ")
        if i % num2 == 0:
            print()
main(int(input()), int(input()))
