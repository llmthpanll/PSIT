"""Inverter"""
def main():
    """Inverter"""
    num = input()
    ans = ""
    for i in num:
        if i == "0":
            ans += "1"
        elif i == "1":
            ans += "0"
    print(ans.lstrip("0"))
main()
