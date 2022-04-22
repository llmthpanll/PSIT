"""PSIT"""
def main():
    """main"""
    num = input()
    ans = from_roman(num)
    print(ans)

def from_roman(num):
    """Do_Roman"""
    roman_numerals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = 0
    for i, j in enumerate(num):
        if (i+1) == len(num) or roman_numerals[j] >= roman_numerals[num[i+1]]:
            result += roman_numerals[j]
        else:
            result -= roman_numerals[j]
    return result
main()
