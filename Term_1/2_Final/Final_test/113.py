"""113"""
def check(txt):
    """check"""
    if "113" in txt:
        ans = txt.find("113")
        txt = txt[0:ans:] + txt[ans+3::]
        check(txt)
    else:
        print(txt)

def main(txt):
    """113"""
    check(txt)
main(input())
