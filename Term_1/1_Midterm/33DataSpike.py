"""DataSpike"""
def marg(num1, num2):
    """DocString"""
    return (num1 * (num1 > num2)) + (num2 * (num2 >= num1))

def main():
    """DocString"""
    num1 = int(input())
    num2 = int(input())
    aaa = marg(num1, num2)
    num3 = int(input())
    aaa = marg(aaa, num3)
    num4 = int(input())
    aaa = marg(aaa, num4)
    num5 = int(input())
    aaa = marg(aaa, num5)
    num6 = int(input())
    aaa = marg(aaa, num6)
    num7 = int(input())
    aaa = marg(aaa, num7)
    num8 = int(input())
    aaa = marg(aaa, num8)
    print("%d" %aaa)
main()
