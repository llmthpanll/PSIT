"""เห็นทะเลยังเป็นหน้าเธอ มันละเมอคิดถึงเธอทุกที"""
def main(txt):
    """เห็นทะเลยังเป็นหน้าเธอ มันละเมอคิดถึงเธอทุกที"""
    zone = {
        "THE SHALLOW ZONE" : ["BULL SHARK"],
        "THE TWILIGHT ZONE" : ["CHAIN CATSHARK", "GREAT WHITE SHARK", "GUMMY SHARK", "BLUE SHARK", "MAKO SHARK"],
        "THE MIDNIGHT ZONE" : ["FRILLED SHARK", "GOBLIN SHARK", "SIXGILL SHARK", "GREENLAND SHARK", \
    "COOKIECUTTER SHARK"],
        "THE ABYSSAL ZONE" : ["MEGAMOUTH SHARK"]
    }
    for i in zone.keys():
        if txt in zone[i]:
            print(i)
            break
    else:
        print("ZONE JAI MA KLUNG RAK DUAY KAN MAI.")
main(input())
