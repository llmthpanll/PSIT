"""Coupon"""
def main():
    """Coupon"""
    price = int(input())
    coupon_1 = input().split(" ")
    coupon_2 = input().split(" ")
    sell_1 = 0
    sell_2 = 0
    percent = 0
    coupon_1[0] = float(coupon_1[0])
    coupon_1[1] = float(coupon_1[1])
    coupon_2[0] = float(coupon_2[0])
    coupon_2[1] = float(coupon_2[1])
    if price >= coupon_1[1]:
        sell_1 = (price - coupon_1[0])/1
    if price >= coupon_2[1]:
        percent = price * coupon_2[0]/100
        sell_2 = price - percent
    if coupon_1[0] == percent:
        if coupon_1[1] == coupon_2[1]:
            print("1 %.1f" %(sell_1))
        elif coupon_1[1] > coupon_2[1]:
            print("2 %.1f" %(sell_2))
        elif coupon_1[1] < coupon_2[1]:
            print("1 %.1f" %(sell_1))
    if sell_1 == 0 and sell_2 == 0:
        print("Nope")
    elif sell_1 > sell_2:
        print("2 %.1f" %(sell_2))
    elif sell_1 < sell_2:
        print("1 %.1f" %(sell_1))
main()
