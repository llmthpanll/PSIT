"""ClockHands"""
def main():
    """ClockHands"""
    hour, sec = int(input()), int(input())
    hour *= 5
    hour += sec / 12
    hour %= 60
    print(sec <= hour < sec+1)
main()
