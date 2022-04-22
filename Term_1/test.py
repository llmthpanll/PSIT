"""test"""
def main():
    """test"""
    txt = input("Enter 2 imtegers : ").split()
    for i in range(int(txt[0]), int(txt[1])):
        if i%2==1:
            break
    print(txt)
main()
