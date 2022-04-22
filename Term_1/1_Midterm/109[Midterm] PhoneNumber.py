"""[Midterm] PhoneNumber"""
def main():
    """[Midterm] PhoneNumber"""
    phone = input()
    nation = input()
    if len(phone) == 9:
        if nation == "Domestic":
            print(phone[0]+" "+phone[1:5]+" "+phone[5:])
        else:
            print("+66"+" "+phone[1:5]+" "+phone[5:])
    else:
        if nation == "Domestic":
            print(phone[0:2:]+" "+phone[2:6]+" "+phone[6:])
        else:
            print("+66"+phone[1]+" "+phone[2:6]+" "+phone[6:])
main()
