"""Phasmo"""
def main():
    """Phasmo"""
    printed = False
    all_evidence = ["EMF Level 5", "Ghost Writing", "Fingerprints",\
        "Spirit Box", "Freezing Temperatures", "Ghost Orb"]
    ghosts = {
        "Banshee": [0, 2, 4],
        "Demon": [1, 3, 4],
        "Jinn": [0, 3, 5],
        "Mare": [3, 4, 5],
        "Oni": [0, 1, 3],
        "Phantom": [0, 4, 5],
        "Poltergeist": [2, 3, 5],
        "Revenant": [0, 1, 2],
        "Shade": [0, 1, 5],
        "Spirit": [1, 2, 3],
        "Wraith": [2, 3, 4],
        "Yurei": [1, 4, 5]
    }
    my_evidence = []
    for i in range(3):
        text = input()
        if text in all_evidence:
            my_evidence.append(all_evidence.index(text))
    for ghost, evi in sorted(ghosts.items()):
        nono = False
        for i in my_evidence:
            if i not in evi:
                nono = True
        if not nono:
            printed = True
            print(ghost)
    if not printed:
        print("Not yet discovered")
main()
