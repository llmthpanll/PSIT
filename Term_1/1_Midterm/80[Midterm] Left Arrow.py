"""LeftArrow"""
def main():
    """LeftArrow"""
    width = int(input())
    height = int(input())
    height_2 = int((height-1)/2)
    for i in range(height_2):
        print(" "*(height_2-i) + "*"*width)
    print("*"*width)
    for i in range(height_2):
        print(" "*(i*2-1) + "*"*width)
main()
