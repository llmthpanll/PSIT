"""Align"""
import math
def howlong(txt, length):
    """howlong"""
    long = length-(len(txt))
    return long

def main():
    """Align"""
    length = int(input())
    align = input()
    txt = input()
    left = math.ceil(howlong(txt, length)/2)
    right = math.floor(howlong(txt, length)/2)
    if align == "left":
        print("%s%s" %(txt, " "*howlong(txt, length)))
    elif align == "center":
        print("%s%s%s" %(" "*left, txt, " "*right))
    elif align == "right":
        print("%s%s" %(" "*howlong(txt, length), txt))

main()




