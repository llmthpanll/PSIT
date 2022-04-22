"""[Midterm] Stamps"""
def main():
    """[Midterm] Stamps"""
    n_input, a_input, b_input, c_input, d_input, stamp, total = \
int(input()), int(input()), int(input()), int(input()), int(input()), 0, 0
    for _ in range(n_input):
        amount = int(input())
        a_discount = amount
        while True:
            if stamp >= c_input and a_discount > 0:
                stamp -= c_input
                a_discount -= d_input
            else:
                break
        if amount >= a_input:
            if b_input != 0 or d_input != 0:
                stamp += int((a_discount / a_input)) * b_input
        total += 0 if a_discount <= 0 else a_discount
    print(int(total))
    print(int(stamp))
main()
