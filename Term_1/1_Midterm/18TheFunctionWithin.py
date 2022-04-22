"""TheFunctionWithin"""
def fff(xxx):
    """f(x)"""
    return 2*xxx
def ggg(xxx):
    """g(x)"""
    return 3*(xxx**4)-(xxx**3)+2*(xxx**2)+10
def hhh(xxx, yyy, zzz):
    """h(x,y,z)"""
    return ((zzz+xxx)**2)-(xxx*yyy)+(yyy**2)
def iii(aaa, bbb, ccc, ddd):
    """i(a,b,c,d)"""
    scrap = aaa**2+bbb**2-ccc**2
    part = (ddd**2)-(2*aaa*ddd)+(2*aaa)
    return scrap/part
def main():
    """TheFunctionWithin"""
    aaa = float(input())
    bbb = float(input())
    ccc = float(input())
    ddd = float(input())
    print(fff(fff(aaa)))
    print(ggg(fff(aaa-bbb)))
    print(hhh(fff(aaa+bbb), fff(aaa+ccc), ggg(fff(ddd**2))))
    print(iii(hhh(fff(aaa+bbb), fff(aaa-ccc), ggg(fff(ddd**2))), ggg(fff(aaa-bbb)),\
        fff(fff(fff(fff(fff(ccc))))), ddd**8))
main()
