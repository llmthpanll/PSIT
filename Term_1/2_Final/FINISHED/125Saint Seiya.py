"""Saint Seiya"""
def main(second, punch):
    """Saint Seiya"""
    realpunch = 0
    for i in range(2, second+1, 2):
        if realpunch < punch:
            if i%6 == 0:
                realpunch += 1
            elif i%2 == 0:
                realpunch += 165
        else:
            realpunch += (second+1-i)*12 #+1 รอบ cash หายไป
            break
    print(realpunch)
main(int(input()), int(input()))
