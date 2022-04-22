"""MyMath"""
import math
def ans1():
    """ans1"""
    scrap = (math.sin(math.radians(90)))+((math.sin(math.radians(60)))**2)
    part = (math.cos(math.radians(245**2)))+(math.cos(math.radians(45+135)))
    return scrap/part
def ans2():
    """ans2"""
    scrap = math.factorial(16)*math.factorial(4)
    part = math.factorial(8)
    return scrap/part
def ans3():
    """ans3"""
    scrap = 15+25
    part = math.sqrt(((25-12)**2)+((12-15)**2))
    return scrap/part
def ans5():
    """ans3"""
    scrap = math.log(4234, 5)+math.log2(8191)+(71*(math.log10(156154)))
    part = math.log(777, 7)-math.log(888, 8)-math.log(999, 9)
    return scrap/part
def main():
    """MyMath"""
    print(ans1())
    print(ans2())
    print(ans3())
    print(math.log10(1234**4))
    print(ans5())
main()
