"""Area"""
def main():
    """Area"""
    num = int(input())
    count = 0
    for _ in range(num):
        txt = input().replace(" ", "")
        count += len(txt)
    print(count)
main()
