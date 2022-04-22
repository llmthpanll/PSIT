"""LetterFrequency"""
import string
def main():
    """LetterFrequency"""
    text = input().lower().replace(" ", "")
    ans = list(filter(lambda a: a in string.ascii_letters, text))
    ans = max(set(text), key=text.count)
    print(ans)
main()
