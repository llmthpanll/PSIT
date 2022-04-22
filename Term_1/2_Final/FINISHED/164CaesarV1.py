"""carser"""
import string
def main():
    """KKKK"""
    shift = int(input())
    text = input()
    result = ""
    for i in text:
        if i in string.ascii_letters:
            if i.isupper():
                c_index = ord(i) - ord("A")
                new_index = (c_index + shift) % 26
                new_unicode = new_index + ord("A")
                new_char = chr(new_unicode)
                result = result + new_char
            else:
                if i != " ":
                    c_index = ord(i) - ord("a")
                    new_index = (c_index + shift) % 26
                    new_unicode = new_index + ord("a")
                    new_char = chr(new_unicode)
                    result = result + new_char
                else:
                    result += i
        else:
            result += i
    print(result)
main()
