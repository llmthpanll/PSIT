"""BrickBridge"""
def main():
    """BrickBridge"""
    numa = int(input())
    numb = int(input())
    numgold = int(input())
    if numgold%5 > numa or (numa+(numb*5)) < numgold:
        print(-1)
    else:
        if numb*5 >= numgold:
            small = numgold%5
        else:
            small = numgold-(numb*5)
        print(small)
main()
