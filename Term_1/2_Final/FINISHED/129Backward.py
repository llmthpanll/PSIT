"""Backward"""
def main():
    """Backward"""
    my_list = []
    while True:
        txt = input()
        if txt == "NULL":
            break
        my_list.append(txt)
    for _ in range(len(my_list)):
        print(my_list.pop(-1))
main()
