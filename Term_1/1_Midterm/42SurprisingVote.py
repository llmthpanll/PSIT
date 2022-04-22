"""SurprisingVote"""
def main():
    """SurprisingVote"""
    num1 = float(input())
    num2 = float(input())
    num3 = 0 #ตัวน้อยสุด
    if num2*2 < num1:
        num3 = num1-num2*2
    if num2 - num3 > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
