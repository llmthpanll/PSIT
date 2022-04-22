"""last stand"""
import json
def main():
    """last stand"""
    txt = json.loads(input())
    ans = ""
    for i in txt:
        ans = str(i)[-1]
        print(ans)
main()
