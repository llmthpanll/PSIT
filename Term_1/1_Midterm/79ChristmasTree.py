"""ChristmasTree"""
def main():
    """ChristmasTree"""
    number = int(input())
    row = int(input())
    for i in range(1, number+1):
        print(" "*(number-i), end="")
        print("*"*(i*2-1))
    for _ in range(row):
        print(" "*(number-2), end="")
        print("---")
main()
