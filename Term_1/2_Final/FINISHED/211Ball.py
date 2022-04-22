"""Ball"""
def main():
    """Ball"""
    hight = float(input())
    count = 0
    while hight >= 0.01:
        hight = hight * 3/5
        count += 1
    print(count-1)
main()
