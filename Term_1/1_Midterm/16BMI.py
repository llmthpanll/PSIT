"""aver"""
def aver(www, hhh):
    """aver"""
    return www/(hhh/100)**2
def printt(name, bmi):
    """PRINT"""
    print("%s's  BMI = %.2f" %(name, bmi))
def main():
    """aver"""
    name1 = input()
    weight1 = float(input())
    height1 = float(input())
    name2 = input()
    weight2 = float(input())
    height2 = float(input())
    name3 = input()
    weight3 = float(input())
    height3 = float(input())
    name4 = input()
    weight4 = float(input())
    height4 = float(input())
    name5 = input()
    weight5 = float(input())
    height5 = float(input())
    printt(name1, aver(weight1, height1))
    printt(name2, aver(weight2, height2))
    printt(name3, aver(weight3, height3))
    printt(name4, aver(weight4, height4))
    printt(name5, aver(weight5, height5))
main()
