"""Triangle I"""
def main():
    """Triangle I"""
    num = [float(input()), float(input()), float(input())]
    if num[0] > num[1]:
        num[1], num[0] = num[0], num[1]
    if num[1] > num[2]:
        num[1], num[2] = num[2], num[1]
    if num[0] > num[1]:
        num[1], num[0] = num[0], num[1]
    pythagoras = ((num[0]**2)+(num[1]**2))**0.5
    if num[2] <= pythagoras <= num[2]+0.01:
        print("Yes")
    else:
        print("No")
main()

