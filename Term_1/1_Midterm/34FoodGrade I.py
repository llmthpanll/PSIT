"""FoodGrade I"""
def check():
    """check"""
    num = float(input())
    xxx = 0
    if 50 <= num <= 70:
        xxx = num
    return xxx

def main():
    """FoodGrade I"""
    my_list = list()
    my_list.append(check())
    my_list.append(check())
    my_list.append(check())
    my_list.append(check())
    my_list.append(check())
    my_list.append(check())
    my_list.append(check())
    my_list.append(check())
    my_list.append(check())
    my_list.append(check())
    my_list.append(check())
    my_list.append(check())
    my_list.append(check())
    my_list.append(check())
    my_list.append(check())
    my_list.append(check())
    my_list.append(check())
    my_list.append(check())
    my_list.append(check())
    my_list.append(check())
    my_list.append(check())
    my_list.append(check())
    my_list.append(check())
    my_list.append(check())
    ans = len(my_list) - my_list.count(0)
    print(ans)
main()
