"""[Midterm] Milk V.1"""
def main():
    """[Midterm] Milk V.1"""
    num1, num2, num3, num4 = int(input()), int(input()), int(input()), int(input())
    have_cap = num4 // num1
    milk = have_cap
    if num2 == 0:
        print(milk)
    else:
        while True:
            more = (have_cap // num2) * num3
            milk += more
            mod = (have_cap % num2)
            have_cap = 0
            have_cap += mod
            have_cap += more
            more = 0
            if have_cap < num2:
                break
        print(milk)
main()
