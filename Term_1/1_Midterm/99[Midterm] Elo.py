"""[Midterm] Elo"""
def main():
    """[Midterm] Elo"""
    rate_a = int(input())
    rate_b = int(input())
    player = input()
    if player == "A":
        elo = 1/(1+(10**((rate_b-rate_a)/400)))
    elif player == "B":
        elo = 1/(1+(10**((rate_a-rate_b)/400)))
    print("%.2f" %elo)
main()
