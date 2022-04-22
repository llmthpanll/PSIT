"""PSIT"""
def main(num1):
    """SMS"""
    text = []
    ans = ""
    this_dict = {
        "1" : "DEL",
        "2" : ["A", "B", "C"],
        "3" : ["D", "E", "F"],
        "4" : ["G", "H", "I"],
        "5" : ["J", "K", "L"],
        "6" : ["M", "N", "O"],
        "7" : ["P", "Q", "R", "S"],
        "8" : ["T", "U", "V"],
        "9" : ["W", "X", "Y", "Z"]
    }
    for i in range(num1):
        button = input()
        times = int(input())
        if button == "1":
            for _ in range(times):
                text.pop(-1)
        elif button == "7" or button == "9":
            text.append(this_dict[(button)][(int(times)%4-1)])
        else:
            text.append(this_dict[(button)][((int(times)%3-1))])
    for i in text:
        ans += i
    if ans == "":
        ans = "null"
    print(ans)
main(int(input()))
