"""[Midterm] diamond"""
def main():
    """[Midterm] diamond"""
    num = int(input())
    half = num//2
    for i in range(num):
        for j in range(num):
            if i == half or i+j == half or j-i == half or i-j == half or j == num-i+half-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
main()
