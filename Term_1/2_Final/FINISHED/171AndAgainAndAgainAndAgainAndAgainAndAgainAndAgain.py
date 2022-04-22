"""AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""
def main():
    """AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""
    message = input().replace(".", "").split()
    aeiou = "aeiou"
    lst = []
    for i in message:
        count = 0
        for j in i:
            if j in aeiou:
                count += 1
        if count >= 2:
            lst.append(i)
    lst.sort()
    if not lst:
        print("Nope")
    for i in lst:
        print(i)
main()
