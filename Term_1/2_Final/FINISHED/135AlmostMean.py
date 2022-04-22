"""AlmostMean"""
def main():
    """AlmostMean"""
    score = []
    data = []
    mean = 0
    ans = 0
    num = int(input())
    for _ in range(num):
        txt = input()
        data.append(txt)
        txt = txt.split("\t")
        score.append(float(txt.pop(1)))
    mean = (sum(score))/num
    score2 = sorted(score)
    score2.reverse()
    for i in score2:
        if i <= mean:
            ans = score.index(i)
            print(data[ans])
            break
main()
