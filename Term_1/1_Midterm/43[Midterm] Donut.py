"""[Midterm] Donut"""
def main():
    """[Midterm] Donut"""
    price = int(input())
    amount = int(input())
    free = int(input())
    want = int(input())
    donut = 0
    promo = amount+free
    inwant = want//promo
    if want == 0:
        print("0 0")
    if want > 0:
        donut = inwant*promo
        left = want-donut
        if left > amount:
            left = amount
        if left >= amount:
            donut += promo
        else:
            donut += left
        print((price*inwant*amount)+(left*price), donut)
main()
