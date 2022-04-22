"""Hamburger"""
def main():
    """printขนมปังกับเนื้อ"""
    bread_left = int(input())
    bread_right = int(input())
    print("%s%s%s" %(("|"*bread_left), ("*"*((bread_left+bread_right)*2)), ("|"*bread_right)))
main()
