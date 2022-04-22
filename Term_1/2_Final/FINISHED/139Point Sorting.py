"""Point Sorting"""
def main(count):
    """Point Sorting"""
    for _ in range(count):
        countnext = int(input())
        lst = []
        for _ in range(countnext):
            txt = input().split()
            lstint = []
            lstint.append(int(txt[0]))
            lstint.append(int(txt[1]))
            lst.append(lstint)
        lst.sort(reverse=True, key=lambda lst: lst[1])
        lst.sort(key=lambda lst: lst[0]+lst[1])
        for i in lst:
            for j in i:
                print(j, end=" ")
            print()
main(int(input()))
