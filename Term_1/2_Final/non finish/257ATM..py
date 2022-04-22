"""ATM"""
def main():
    """ATM"""
    start = int(input())
    while True:
        case = input()
        if case == "END":
            break
        elif case[0] == "D":
            start += int(case[2::])
        elif case[0] == "W":
            if start <= int(case[2::]):
                start -= start
            else:
                start -= int(case[2::])
            if start == 0:
                continue
    print(start)
main()
