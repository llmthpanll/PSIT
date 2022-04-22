"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def main():
    """19"""
    choose = input()
    num = [float(input()), float(input()), float(input())]
    if num[0] > num[1]:
        num[1], num[0] = num[0], num[1]
    if num[1] > num[2]:
        num[1], num[2] = num[2], num[1]
    if num[0] > num[1]:
        num[1], num[0] = num[0], num[1]
    if choose == "Ascend":
        print("%.2f, %.2f, %.2f " %(num[0], num[1], num[2]))
    elif choose == "Descend":
        print("%.2f, %.2f, %.2f " %(num[2], num[1], num[0]))
main()
