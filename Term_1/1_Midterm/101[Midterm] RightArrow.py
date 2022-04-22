"""Problem"""
def main():
    """[Midterm] RightArrow"""
    width = int(input())
    high = int(input())
    total = high//2
    for i in range(high):
        print((" "*(total-(high//2)))+("*"*width))
        if i < high//2:
            total += 1
        else:
            total -= 1
main()
