"""Sequence VI"""
def main():
    """Sequence VI"""
    row = int(input())
    col = 1
    for i in range(row):
        for k in range(col):
            print(k+1, end=" ")
        print()
        col = col+1
        i = i
main()
