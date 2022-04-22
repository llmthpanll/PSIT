"""[Midterm] Parallelogram"""
def main():
    """[Midterm] Parallelogram"""
    txt = input()
    count = len(txt)
    for i in range(0, count):
        print(" "*(count-i-1)+txt[0:i+1])
    for i in range(0, count):
        print(txt[i+1:count:])
main()
