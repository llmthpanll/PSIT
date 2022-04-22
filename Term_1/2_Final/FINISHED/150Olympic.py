"""Olympic"""
def main():
    """Olympic"""
    countries = dict()
    for _ in range(int(input())):
        coun = input().split(" ")
        countries[coun[0]] = tuple(map(int, coun[1:]))
    sorted_countries = sorted(countries.items(), key=lambda a: sum(a[1]), reverse=True)
    sorted_countries.sort(key=lambda a: a[0])
    sorted_countries.sort(key=lambda a: a[1], reverse=True)
    rank = 0
    keep = 0
    old = 0
    for country, score in sorted_countries:
        scoresum = sum(score)
        score = " ".join(map(str, score))
        if score != old:
            rank += keep
            keep = 0
            rank += 1
        elif rank != 0:
            keep += 1
        print(rank, country, score, scoresum)
        old = score
main()
