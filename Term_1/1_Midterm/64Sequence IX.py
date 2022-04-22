"""Sequence IX"""
def main():
    """Sequence IX"""
    num = int(input())
    for i in range(1, num+1):
        for j in range(-num+1, num, 1):
            if j == 0 or abs(j) < i:
                print("%02d"%(i-abs(j)), end=" ")
            else:
                print("  ", end=" ")
        print()
main()
