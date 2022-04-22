"""[Midterm] ValidVar"""
import keyword
def main():
    """[Midterm] ValidVar"""
    count_input = int(input())
    punc = '''!()-[]{};:'",<>./?\\@#$%^+=&*~'''
    txtcheck = ""
    for i in range(count_input):
        variable = input()
        if variable[-1] == " ":
            variable = variable[:-1]
        for i in variable:
            if i in punc or keyword.iskeyword(variable) or variable[0].isdigit() \
or " " in variable[1:]:
                print("Invalid")
                txtcheck = ""
                break
            else:
                txtcheck += i
            if variable == txtcheck:
                print("Valid")
                txtcheck = ""
                break
main()
