"""[Midterm] Key"""
def main():
    """[Midterm] Key"""
    num = input()  #1234567890123
    num_sum = 0
    for i in num:
        num_sum += int(i)
    num2 = int(num[10:13])*10
    add = num_sum+num2
    if add >= 10000:
        add = str(add)
        add = add[1:5]
        print(add)
    elif add <= 999:
        add += 1000
        print(add)
    else:
        print(add)  #5146882735998
main()
