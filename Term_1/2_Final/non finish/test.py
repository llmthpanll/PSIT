"""bloodDonation"""
def main():
    """bloodDonation"""
    age = int(input())
    weight = float(input())
    times = int(input())
    validity = False
    if age == 17 or 60 <= age <= 70:
        certi = input()
        if certi == "False":
            validity = False
    if times == 0:
        if age > 55:
            validity = True
    if weight >= 45:
        validity = True
    if 17 <= age <= 70:
        validity = True
    if validity == False:
        print("No")
    else:
        print("Yes")
main()
