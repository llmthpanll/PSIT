"""[Midterm] Pringles"""
def main():
    """[Midterm] Pringles"""
    border_top = input()
    pringle = input()
    border_bottom = input()
    num = int(input())
    eat_count = 0
    left_count = 0
    eat = pringle[:num:]
    left = pringle[num::]
    for i in eat:
        if i == ")":
            eat_count += 1
    for i in left:
        if i == ")":
            left_count += 1
    print(eat_count)
    if left_count == 0:
        print("None.")
    else:
        print("There are still some left.")
    print(border_top)
    print("%s%s" %((" "*num), pringle[num:]))
    print(border_bottom)
main()
