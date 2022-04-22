"""4[Midterm] LargestNumber"""
def check(num1, num2): # 10 , 5
    """check"""
    cek = ((num1 >= num2)*num1) + ((num2 > num1)*num2)
    return cek

def main():
    """4[Midterm] LargestNumber"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int("%d%d%d" %(num1, num2, num3))     #  "321" >= "123"
    num5 = int("%d%d%d" %(num1, num3, num2))
    num6 = int("%d%d%d" %(num2, num1, num3))
    num7 = int("%d%d%d" %(num2, num3, num1))
    num8 = int("%d%d%d" %(num3, num1, num2))
    num9 = int("%d%d%d" %(num3, num2, num1))
    num10 = check(num4, num5)
    num11 = check(num6, num7)
    num12 = check(num8, num9)
    num13 = check(num10, num12)
    num14 = check(num13, num11)
    print(num14)
main()
