"""Runner"""
def main():
    """Runner"""
    distance = float(input())
    count = int(input())
    lyst = []
    run = []
    for _ in range(count):
        player = input().split(" ")
        lyst.append(player)
    lyst2 = lyst.copy()
    lyst.sort(key=lambda i: float(i[0]), reverse=True)
    for i in lyst:
        xxx = (distance-float(i[1]))/float(i[0])
        run.append(xxx)
    print(lyst2.index(lyst[run.index(min(run))])+1)
main()
