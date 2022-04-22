"""PickThemAgain"""
def main():
    """PickThemAgain"""
    my_ans = []
    state = 0
    txt = input().split(" ")
    for i in txt:
        if int(i) % 3 == 0 or int(i)%5 == 0:
            my_ans.append(i)
            state = 1
    my_ans.reverse()
    if state == 1:
        for i in my_ans:
            print(i)
    elif state == 0:
        print("Nope")
main()
