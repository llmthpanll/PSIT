"""BloodDonation"""
def main():
    """BloodDonation"""
    age = int(input())
    weight = float(input())
    times = int(input())
    validity = True
    if age == 17 or 60 <= age <= 70:
        certificate = input()
        if certificate == 'False':
            validity = False
    if times == 0:
        if age > 55:
            validity = False
    if weight < 45:
        validity = False
    if 17 > age or age > 70:
        validity = False
    if validity == True:
        print('Yes')
    else:
        print('No')
main()
