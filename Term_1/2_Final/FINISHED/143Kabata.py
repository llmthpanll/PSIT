"""Kabata"""
def main():
    """Kabata"""
    num = int(input())
    for _ in range(num):
        word = input()
        word = word.replace('baka', '-').replace("bakka", "").\
            replace("ta", "").replace("ba", "").replace("ka", "")
        if word == "":
            print("yes")
        else:
            print("no")
main()
