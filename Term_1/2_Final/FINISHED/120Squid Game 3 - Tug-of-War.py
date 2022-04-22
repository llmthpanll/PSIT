"""ข้อ9"""
def teama():
    """team A"""
    i = 0
    power = 0
    all_power = 0
    while True:
        if i == 10:
            break
        i += 1
        power = int(input())
        all_power += power
    return all_power
def teamb():
    """team B"""
    i = 0
    power = 0
    all_power = 0
    while True:
        if i == 10:
            break
        i += 1
        power = int(input())
        all_power += power
    return all_power
def main():
    """ข้อ9"""
    power_a = teama()
    power_b = teamb()
    if power_a > power_b:
        print("B")
    elif power_a < power_b:
        print("A")
    else:
        print("AB")
main()
