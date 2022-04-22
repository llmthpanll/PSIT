"""PickThem"""
import json
def main():
    """PickThem"""
    state = 0
    my_list = json.loads(input())
    for i in my_list:
        if int(i) % 2 == 0:
            state = 1
    if state == 1:
        for i in my_list:
            if int(i) % 2 == 0:
                print(i)
    elif state == 0:
        print("Nope")
main()
