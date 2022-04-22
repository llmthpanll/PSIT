'''temperature'''
def main():
    '''temperature'''
    temp = float(input())
    unit_before = input()
    unit_after = input()
    if unit_before == "F":
        temp = (temp-32)*(5/9)
    elif unit_before == "K":
        temp = temp - 273.15
    elif unit_before == "R":
        temp = (temp*(5/9))-273.15
    if unit_after == "F":
        return '%.2f' %(temp*(9/5)+32)
    elif unit_after == "K":
        return '%.2f' %(temp+273.15)
    elif unit_after == "R":
        return '%.2f' %((temp+273.15)*(9/5))
    return '%.2f' %temp
print(main())
