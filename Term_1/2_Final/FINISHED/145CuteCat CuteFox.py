"""CuteCat CuteFox"""
def main1(dictcat, txt):
    """Function DocString"""
    return len([few for few in dictcat.values() if txt in few])

def main():
    """Function DocString"""
    num1, dictcat, catresult = int(input()), {}, {}
    for _ in range(num1):
        txt = str(input())
        if len(txt.split('"')) > len(txt.split("'")):
            dictcat[txt.split('"')[1]] = txt.split('"')[3]
        else:
            dictcat[txt.split("'")[1]] = txt.split("'")[3]
    countcat, countfox = main1(dictcat, "Cat"), main1(dictcat, "Fox")
    checkcat, checkfox, count = "Cat01" in dictcat.values(), "Fox01" in dictcat.values(), 0
    if countcat == 0 or checkcat == 0:
        catresult["Garfield"] = "Cat01"
    if countfox == 0 or checkfox == 0:
        catresult["Fubuki"] = "Fox01"
    for key, value in sorted(dictcat.items(), key=lambda x: x[1]):
        if checkfox == 0 and value.count("Fox") >= 1 and count == 0:
            count += 1
            catresult["Fubuki"] = "Fox01"
        catresult[key] = value
    countcat, countfox = main1(catresult, "Cat"), main1(catresult, "Fox")
    cat, fox = {}, {}
    for key, value in catresult.items():
        if value.count("Cat") >= 1:
            cat.update({int(value.split("Cat")[1]): [key, value]})
        elif value.count("Fox") >= 1:
            fox.update({int(value.split("Fox")[1]): [key, value]})
    print("Cat : %d\nFox : %d" %(countcat, countfox))
    for cry in sorted(cat):
        print(cat[cry][0] + " : " + cat[cry][1])
    for cry in sorted(fox):
        print(fox[cry][0] + " : " + fox[cry][1])
main()
