"""Muddled Menu"""
def main():
    """Muddled Menu"""
    menu = []
    while True:
        couse = input()
        if couse == "DONE":
            break
        elif couse == "CLOSED":
            return print("Full Course: [] Reversed: []")
        elif couse == "SOMETHING'S WRONG":
            menu.clear()
            continue
        elif couse[0:10:] == "Can't do: ":
            menu.remove(couse[10::])
        else:
            txt = couse.split(" #")
            if txt[1].isnumeric():
                menu.insert(int(txt[1])-1, txt[0])
            else:
                menu.append(txt[0])
    print("Full Course: "+str(menu), end=" ")
    menu.reverse()
    print("Reversed: "+str(menu))
main()
