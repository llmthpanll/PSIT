"""[Midterm] Stair"""
def main():
    """[Midterm] Stair"""
    high = int(input())
    floor = int(input())
    able = True
    check = 0
    count = 0
    for _ in range(1, floor+1):
        step = int(input())
        check += step
        if step > high:
            able = False
        elif check == high:
            count += 1
            check = 0
        elif check > high:
            count += 1
            check = step
    if check > 0:
        count += 1
    print(able*str(count) + (able == False)*"NO")
main()
