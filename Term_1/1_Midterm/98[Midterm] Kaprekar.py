"""[Midterm] Kaprekar"""
def sor(num):
    """[Midterm] Kaprekar"""
    num_list = []
    for i in num:
        num_list.append(int(i))
    data_list = num_list
    new_list = []
    ans = ""
    while data_list:
        munimum = data_list[0]  # arbitrary number in list
        for i in data_list:
            if i < munimum:
                munimum = i
        new_list.append(munimum)
        data_list.remove(munimum)
    for i in new_list:
        ans += str(i)
    return ans
def main():
    """[Midterm] Kaprekar"""
    num = input()
    count = 1
    while True:
        if num == "6174":
            print(count)
            break
        if len(str(num)) < 4:
            num += "0"
        else:
            mux = sor(num)[::-1]
            muxval = int(mux)
            munval = int(mux[::-1])
            ans = muxval-munval
            if ans == 6174:
                print(count)
                break
            else:
                num = str(ans)
                count += 1
main()
