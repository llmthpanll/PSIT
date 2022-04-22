"""Blackjack"""
def calculator(card):
    """calculator"""
    if card in 'JQK':
        return 10
    elif card in "A":
        return 11
    else:
        return card

def main():
    """Blackjack"""
    num_card = int(input())
    card_1 = int(calculator(input()))
    card_2 = int(calculator(input()))
    if num_card == 3:
        card_3 = int(calculator(input()))
        print(card_1+card_2+card_3)
    elif num_card == 2:
        print(card_1+card_2)
main()
