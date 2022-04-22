"""[Midterm] Restaurant"""
def main():
    """[Midterm] Restaurant"""
    order_food = float(input()) #{a > 0}
    promotion = float(input()) #{b >= a}
    discount = float(input()) #{0 <= c <= 100}%
    order_more_food = float(input()) #​{d >= 0}
    pill = 0
    order_foodans = 0
    #เช็ค promotion กับอาหารที่กินตอนแรก  == จะได้ราคาตอนแรกที่จ่าย
    if order_food >= promotion:
        order_foodans = order_food-(order_food*(discount/100))
    else:
        order_foodans = order_food
    #เช็ค promotion กับอาหารที่กินรวมสั่งเพิ่ม
    if (order_food+order_more_food) >= promotion:
        pill = (order_food+order_more_food) - ((order_food+order_more_food) * (discount/100))
    #promotion ไม่ติด
    if (order_food+order_more_food) < promotion:
        pill = (order_food+order_more_food)
    #เช็คเงื่อนไข
    if pill < order_foodans:
        print("Yes %.3f"%(order_foodans-pill))
    elif pill == order_foodans:
        print("Yes")
    else:
        print("No %.3f"%(pill-order_foodans))
main()
