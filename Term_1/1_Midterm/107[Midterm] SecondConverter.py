"""[Midterm] SecondConverter"""
def main():
    """[Midterm] SecondConverter"""
    sec_in_rlw = int(input())
    sec_in_mw = int(input())
    min_in_mw = int(input())
    h_in_mw = int(input())
    ans_min = sec_in_rlw//sec_in_mw
    ans_sec = sec_in_rlw%sec_in_mw
    ans_h = ans_min//min_in_mw
    ans_min = ans_min%min_in_mw
    ans_h = ans_h%h_in_mw
    print("%d:%d:%d"%(ans_h, ans_min, ans_sec))
main()
