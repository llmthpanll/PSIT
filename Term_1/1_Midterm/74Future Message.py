"""Future Message"""
def main():
    """Future Message"""
    txt = input()
    if txt.isdigit() == True:
        print("Number")
    elif txt.isupper() == True:
        print("Uppercase")
    elif txt.islower() == True:
        print("Lowercase")
    elif txt.istitle() == True:
        print("Title")
    elif txt.isspace() == True:
        print("Space")
    else:
        print("Other")
main()
