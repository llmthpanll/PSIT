"""Digit v2"""
def main(name):
    """ficn"""
    if name[0][-2:] == "ty" or name[0][-4:] == "teen" or name[0] == "twelve" \
or name[0] == "eleven" or name[0] == "ten":
        print(2)
    elif len(name) > 1:
        if name[1] == "thousand":
            print(4)
        elif name[1] == "hundred":
            print(3)
    else:
        print(1)
main(input().split(" "))
