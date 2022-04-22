"""bookworm"""
def main():
    """bookworm"""
    for _ in range(int(input())):
        minute = float(input())
        my_list = sorted([float(input()) for _ in range(int(input()))])
        i = 0 # bruh pylint go bruh bruh bruh
        for i in range(len(my_list)):
            if sum(my_list[:i+1]) > minute:
                break
            i += 1
        print(i)
main()
