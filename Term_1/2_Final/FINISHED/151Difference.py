"""Difference"""
def main():
    """Difference"""
    set_n = set()
    set_m = set()
    num_n = int(input())
    num_m = int(input())
    for _ in range(num_n):
        set_n.add(int(input()))
    for _ in range(num_m):
        set_m.add(int(input()))
    ans = set_n.difference(set_m)
    ans = sorted(ans)
    for i in ans:
        print(i, end=" ")
main()
