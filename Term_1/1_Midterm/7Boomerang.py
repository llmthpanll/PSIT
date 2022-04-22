"""JumpAround"""
def cal_1(xxx):
    """สมการ1"""
    return xxx+1
def cal_2(yyy):
    """สมการ2"""
    return 7*(yyy**3)+2*(yyy**2)-31*yyy+1
def cal_3(zzz):
    """สมการ3"""
    return 0-zzz
def cal_4(xxx, yyy):
    """สมการ4"""
    return (xxx+yyy)*(xxx-yyy)
def cal_5(xxx, yyy, zzz):
    """สมการ5"""
    return (yyy-((yyy**2)-(4*xxx*zzz))**0.5)/(2*xxx)

def main():
    """JumpAround"""
    var_1 = int(input())
    var_2 = int(input())
    var_3 = int(input())
    print(cal_1(var_1))
    print(cal_2(var_2))
    print(cal_3(var_3))
    print(cal_4(var_1, var_2))
    print(cal_5(var_1, var_2, var_3))
main()
