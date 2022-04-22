"""Day I"""
def main():
    """Day I"""
    years = int(input())
    if (years % 400 == 0) or (years % 100 != 0) and (years % 4 == 0):
        print("Yes")
    else:
        print("No")
main()
