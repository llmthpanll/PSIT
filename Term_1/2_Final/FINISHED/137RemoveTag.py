"""RemoveTag"""
def main():
    """RemoveTag"""
    message = input().replace("<", "$<").replace(">", ">$").split("$")
    check = list(filter(lambda x, ok="<": ok not in x, message))
    ans = ' '.join(check)
    print(ans.split())
main()
