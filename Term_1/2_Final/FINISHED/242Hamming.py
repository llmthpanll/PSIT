"""Hamming"""
def main(name, name1):
    """function"""
    ans = 0
    for i in range(len(name)):
        if name[i] != name1[i]:
            ans += 1
    print(ans)
main(input(), input())
