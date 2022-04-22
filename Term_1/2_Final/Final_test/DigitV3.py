"""DigitV3"""
def main():
    """DigitV3"""
    ans = 0
    numcheck = {
        'zero' : '0', 'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6',
        'seven' : '7', 'eight' : '8', 'nine' : '9', 'ten' : '10', 'eleven' : '11', 'twelve' : '12',
        'thirteen' : '13', 'fourteen' : '14', 'fifteen' : '15', 'sixteen' : '16', 'seventeen' : '17',
        'eighteen' : '18', 'nineteen' : '19', 'twenty' : '20', 'thirty' : '30', 'forty' : '40',
        'fifty' : '50', 'sixty' : '60', 'seventy' : '70', 'seventy' : '80', 'ninety' : '90',
        'hundred' : '100', 'thousand' : '1000',
    }
    txt = input().split(" ")
    for i in txt:
        if i == "hundred":
            ans += (ans%10)*100
        elif i == "thousand":
            ans = ans*1000
        else:
            ans += int(numcheck[i])
    print(ans)
main()
