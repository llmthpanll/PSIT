"""Hamburger"""
def main():
    """Hamburger"""
    bread_left = int(input())
    bread_right = int(input())
    meat = (bread_left+bread_right)*2
    print("%s%s%s" %(("|"*bread_left), ("*"*meat), ("|"*bread_right)))
main()
