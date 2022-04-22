"""[Midterm] Turnstile"""
def main():
    """[Midterm] Turnstile"""
    door = 0
    people = 0
    while True:
        action = input().lower()
        if action == "end":
            break
        if action == "c":
            door = 1
        if action == "p":
            if door == 1:
                people += 1
            door = 0
    print(people)
main()
