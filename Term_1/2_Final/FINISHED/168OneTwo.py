"""OneTwo"""
def onetwo(alls):
    """OneTwo"""
    return "1" if alls == 1 else "2" if alls == 2 else onetwo(alls-1)+onetwo(alls-2)
def main(alls):
    """OneTwo"""
    print(onetwo(alls))
main(int(input()))
