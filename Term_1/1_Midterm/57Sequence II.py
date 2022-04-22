"""Sequence II"""
def main():
    """Sequence II"""
    num = int(input())
    for i in range(num):
        for _ in range(num):
            print(i+(_*num), end=" ")
        print()
main()
