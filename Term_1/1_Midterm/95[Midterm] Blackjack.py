"""DocString"""
def main():
    """DocString"""
    round1, score, check = int(input()), 0, 0
    for _ in range(round1):
        num = input().upper()
        if num == "A":
            score += 1
            check = 1
        if num == "J" or num == "Q" or num == "K":
            score += 10
        if num != "A" and num != "J" and num != "Q" and num != "K":
            score += int(num)
    if check == 1 and score <= 11:
        print(score + 10)
    else:
        print(score)
main()
