"""Diamond I"""
def main():
    """Diamond I"""
    mmm = int(input())
    nnn = int(input())
    lyst = []
    ans = []
    for _ in range(mmm):
        diamond = input().split()
        lyst.append(diamond)
    for i in range(nnn):
        cal = 0
        for j in lyst:
            cal += int(j[i])
        ans.append(cal)
    print(max(ans))
main()
