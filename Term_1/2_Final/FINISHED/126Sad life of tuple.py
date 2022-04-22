"""Sad life of tuple"""
def main():
    """Sad life of tuple"""
    mytu = input().split(" ")
    fin = input()
    location = 0
    mytu = tuple(mytu)
    amout = mytu.count(fin)
    location = int(mytu.index(fin))
    for _ in range(amout):
        for _ in range(amout):
            print(location, end=" ")
        print()
main()
