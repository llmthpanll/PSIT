"""Compound Interest"""
def main():
    """Compound Interest"""
    money = int(input())
    percent = (float(input())/100)
    years = int(input())
    stack = 0
    if years == 0:
        stack = money
    elif years > 0:
        for _ in range(years):
            stack = money + (money*percent)
            money = stack
    print("%.2f" %(stack))
main()
