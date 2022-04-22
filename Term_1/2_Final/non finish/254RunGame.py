"""Rungame"""
def main(txt):
    """"Rungame"""
    txt = "0 "+txt
    txt = txt.split()
    ans = 0
    for i in range(len(txt)-1):
        ans += abs(int(txt[i])-int(txt[i+1]))
    print(ans)
main(input())
