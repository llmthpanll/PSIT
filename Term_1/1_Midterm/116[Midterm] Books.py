"""[Midterm] Books"""
def main():
    """[Midterm] Books Functions"""
    import math
    num = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    count = 0
    day = 0
    kfff = 0
    while True:
        numplus = math.ceil((num3/num4)*num2)
        if count == num:
            break
        if numplus >= num2:
            break
        kfff += numplus
        if kfff >= num2:
            kfff = 0
            count += 1
        num3 += 1
        num4 += 1
        day += 1
    day += (num-count)
    print(day)
main()
