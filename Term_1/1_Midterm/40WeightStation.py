"""WeightStation"""
def main():
    """WeightStation"""
    avg = float(input())
    wheel1 = float(input())
    wheel2 = float(input())
    wheel3 = float(input())
    wheel4 = (avg*4)-(wheel1+wheel2+wheel3)
    less = avg-(avg/2)
    more = avg + (avg/2)
    if avg*4 > 15000:
        print("Overweight")
    elif  less < wheel1 < more and less < wheel2 < more and less < wheel3 < more\
 and less < wheel4 < more:
        print("Pass %.2f"%wheel4)
    else:
        print("Unbalance")
main()
