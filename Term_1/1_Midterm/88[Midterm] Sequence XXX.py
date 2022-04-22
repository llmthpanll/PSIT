"""[Midterm] SequenceXXX"""
def main():
    """สาม LOOP"""
    num1 = int(input())
    num2 = int(input())
    num = num1 // 2
    for i in range(-num, num+1):
        for _ in range(num2):
            for j in range(-num, num+1):
                if abs(i) == abs(j) or j == -num or j == num or i == -num or i == num:
                    txt = "%s" %("*")
                    print(txt, end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        print()
main()
