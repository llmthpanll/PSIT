"""[Midterm] Nearer"""
def main():
    """[Midterm] Nearer"""
    p_alice = int(input())
    p_bob = int(input())
    p_icecream = int(input())
    d_atoi = abs(p_icecream-p_alice)
    d_btoi = abs(p_icecream-p_bob)
    if d_atoi == d_btoi:
        print("%s %d" %("Sundaes", d_atoi))
    elif d_atoi > d_btoi:
        print("%s %d" %("Bob", d_btoi))
    elif d_btoi > d_atoi:
        print("%s %d" %("Alice", d_atoi))
main()
