"""[Midterm] BigFrame"""
def main():
    """[Midterm] BigFrame"""
    txt1 = input().rstrip()
    txt2 = input().rstrip()
    txt3 = input().rstrip()
    txt4 = input().rstrip()
    txt5 = input().rstrip()
    find_marg = max(len(txt1), len(txt2), len(txt3), len(txt4), len(txt5))
    print("**"+("*"*find_marg)+"**")
    print("* "+txt1+(" "*(find_marg-len(txt1)))+" *")
    print("* "+txt2+(" "*(find_marg-len(txt2)))+" *")
    print("* "+txt3+(" "*(find_marg-len(txt3)))+" *")
    print("* "+txt4+(" "*(find_marg-len(txt4)))+" *")
    print("* "+txt5+(" "*(find_marg-len(txt5)))+" *")
    print("**"+("*"*find_marg)+"**")
main()
