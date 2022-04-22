"""[Midterm] Lotto"""
def main():
    """[Midterm] Lotto"""
    first_prize = input()
    last_two_prize = input()
    first_three_prize_1 = input()
    first_three_prize_2 = input()
    last_three_prize_1 = input()
    last_three_prize_2 = input()
    lotto = input()
    ans = 0
    #รางวัลที่ 1
    if lotto == first_prize:
        ans += 6000000
    #รางวัลเลขท้าย 2 ตัว
    if lotto[-2] == last_two_prize[0] and \
        lotto[-1] == last_two_prize[1]:
        ans += 2000
    #รางวัลเลขหน้า 3 ตัว
    if lotto[0] == first_three_prize_1[0] \
        and lotto[1] == first_three_prize_1[1]\
             and lotto[2] == first_three_prize_1[2]:
        ans += 4000
    if lotto[0] == first_three_prize_2[0] \
        and lotto[1] == first_three_prize_2[1]\
             and lotto[2] == first_three_prize_2[2]:
        ans += 4000
    #รางวัลเลขท้าย 3 ตัว
    if lotto[-1] == last_three_prize_1[2] and \
        lotto[-2] == last_three_prize_1[1] and \
            lotto[-3] == last_three_prize_1[0]:
        ans += 4000
    if lotto[-1] == last_three_prize_2[2] and \
        lotto[-2] == last_three_prize_2[1] and \
            lotto[-3] == last_three_prize_2[0]:
        ans += 4000
    #รางวัลใกล้เคียง
    if int(first_prize) == 0 and (int(lotto) == 999999 or int(lotto) == 1):
        ans += 100000
    elif int(first_prize) == 999999 and (int(lotto) == 0 or int(lotto) == 999998):
        ans += 100000
    elif (int(lotto)) == int(first_prize)+1 or (int(lotto)) == int(first_prize)-1:
        ans += 100000
    #ไม่ถูกเลย
    else:
        ans += 0
    print(ans)
main()
