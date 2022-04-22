"""RockPaperScissor"""
def main():
    """RockPaperScissor"""
    txt = input()
    num = 2
    player_a = 0
    player_b = 0
    for i in range(0, len(txt), num):
        unknow = (txt[i:i+num])
        if unknow == "SR":
            player_b += 1
        elif unknow == "RP":
            player_b += 1
        elif unknow == "PS":
            player_b += 1
        elif unknow == "SS" or unknow == "PP" or unknow == "RR":
            player_b += 0
        elif unknow == "RS":
            player_a += 1
        elif unknow == "PR":
            player_a += 1
        elif unknow == "SP":
            player_a += 1
        elif unknow == "SS" or unknow == "PP" or unknow == "RR":
            player_a += 0
    if player_a > player_b:
        print("A win %d-%d" %(player_a, player_b))
    if player_a < player_b:
        print("B win %d-%d" %(player_b, player_a))
    if player_a == player_b:
        print("DRAW %d" %(player_a))
main()
