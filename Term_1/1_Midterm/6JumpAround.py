"""JumpAround"""
def cal_1(xxx):
    """สมการ1"""
    return xxx
def cal_2(xxx):
    """สมการ2"""
    return xxx+5
def cal_3(xxx):
    """สมการ3"""
    return xxx-17
def cal_4(xxx):
    """สมการ4"""
    return xxx*32
def cal_5(xxx):
    """สมการ5"""
    return (5*(xxx**2))+((10*5)*xxx)+3

def main():
    """JumpAround"""
    ans = int(input())
    print(cal_1(ans))
    print(cal_2(ans))
    print(cal_3(ans))
    print(cal_4(ans))
    print(cal_5(ans))
main()
