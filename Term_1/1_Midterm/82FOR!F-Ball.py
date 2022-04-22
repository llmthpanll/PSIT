"""FOR!F-Ball"""
def main():
    """FOR!F-Ball"""
    txt = input()
    position = ["ball", "fake1", "fake2"]
    for i in range(len(txt)):
        unknow = txt[i:i+1]
        if unknow == "A":
            temp = position[0]
            position[0] = position[1]
            position[1] = temp
        elif unknow == "B":
            temp = position[1]
            position[1] = position[2]
            position[2] = temp
        elif unknow == "C":
            temp = position[2]
            position[2] = position[0]
            position[0] = temp
    print((position.index("ball"))+1)
main()
