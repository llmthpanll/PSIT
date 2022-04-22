"""iPhone 13 Again"""
def looppoint(mem):
    """iPhone 13 Again"""
    point = ""
    for i in mem:
        if i.isalpha():
            point += i
    return point
def loopnum(mem):
    """iPhone 13 Again"""
    realmem = ""
    for i in mem:
        if i.isdigit():
            realmem += i
    return realmem
def checkmemmini(mem):
    """iPhone 13 Again"""
    ans = loopnum(mem)
    point = looppoint(mem)
    realans = ""
    if ans == "128" and point == "GB":
        realans += "25900"
    elif ans == "256" and point == "GB":
        realans += "29900"
    elif ans == "512" and point == "GB":
        realans += "37900"
    else:
        realans += "Not Available"
    return realans
def checkmemphone(mem):
    """iPhone 13 Again"""
    ans = loopnum(mem)
    point = looppoint(mem)
    realans = ""
    if ans == "128" and point == "GB":
        realans += "29900"
    elif ans == "256" and point == "GB":
        realans += "33900"
    elif ans == "512" and point == "GB":
        realans += "41900"
    else:
        realans += "Not Available"
    return realans
def checkmempro(mem):
    """iPhone 13 Again"""
    ans = loopnum(mem)
    point = looppoint(mem)
    realans = ""
    if ans == "128" and point == "GB":
        realans += "38900"
    elif ans == "256" and point == "GB":
        realans += "42900"
    elif ans == "512" and point == "GB":
        realans += "50900"
    elif ans == "1" and point == "TB":
        realans += "58900"
    else:
        realans += "Not Available"
    return realans
def checkmempromax(mem):
    """iPhone 13 Again"""
    ans = loopnum(mem)
    point = looppoint(mem)
    realans = ""
    if ans == "128" and point == "GB":
        realans += "42900"
    elif ans == "256" and point == "GB":
        realans += "46900"
    elif ans == "512" and point == "GB":
        realans += "54900"
    elif ans == "1" and point == "TB":
        realans += "62900"
    else:
        realans += "Not Available"
    return realans
def main():
    """iPhone 13 Again"""
    phone = input()
    mem = input()
    if looppoint(mem) == "TB" and (phone == "iPhone 13 mini" or phone == "iPhone 13"):
        print("Not Available")
    elif phone == "iPhone 13 mini":
        print(checkmemmini(mem))
    elif phone == "iPhone 13":
        print(checkmemphone(mem))
    elif phone == "iPhone 13 Pro":
        print(checkmempro(mem))
    elif phone == "iPhone 13 Pro Max":
        print(checkmempromax(mem))
    else:
        print("Not Available")
main()
