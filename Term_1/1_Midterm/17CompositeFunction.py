"""CompositeFunction"""
def fff(xxx):
    """f(X)"""
    return 2*xxx
def ggg(xxx):
    """g(X)"""
    return xxx/2+1
def main():
    """CompositeFunction"""
    var = int(input())
    print("%.2f" %fff(ggg(var)))
    print("%.2f" %ggg(fff(var)))
main()
