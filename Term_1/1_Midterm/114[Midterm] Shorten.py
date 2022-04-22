"""[Midterm] Shorten"""
def main():
    """[Midterm] Shorten"""
    numx1, numx2, result = 0, 0, ''
    while True:
        num1 = int(input())
        if num1 == -1:
            if result == '':
                result = str(numx1) if numx1 == (numx1 + numx2) \
else str(numx1) + '-' + str(numx1 + numx2)
            else:
                result = result + ', ' + str(numx1) if numx1 == (numx1 + numx2) else result + \
', ' + str(numx1) + '-' + str(numx1 + numx2)
            break
        if numx1 != num1:
            if numx1 == 0:
                numx1 = num1
            elif (numx1 + numx2 + 1) == num1:
                numx2 += 1
            else:
                if result == '':
                    result = str(numx1) if numx1 == (numx1 + numx2) else str(numx1) + \
'-' + str(numx1 + numx2)
                else:
                    result = result + ', ' + str(numx1) if numx1 == (numx1 + numx2) else result + \
', ' + str(numx1) + '-' + str(numx1 + numx2)
                numx1 = num1
                numx2 = 0
    print('' if result == '0' else result)
main()
