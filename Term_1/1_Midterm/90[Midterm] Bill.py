"""[Midterm] Bill"""
def main():
    """[Midterm] Bill"""
    price = int(input())
    service = price*10/100
    if service < 50:
        service = 50
    elif service > 1000:
        service = 1000
    real_price = price+service
    real_price = real_price*107/100
    print("%.2f" %real_price)
main()
