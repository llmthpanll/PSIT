"""Sequence VII"""
def main():
    """Sequence VII"""
    num = int(input())
    for i in range(1, num+1):
        for _ in range(i):
            print(_+1, end=" ")
        print()
    for i in range(num-1, 0, -1):
        for _ in range(i):
            print(_+1, end=" ")
        print()
main()
