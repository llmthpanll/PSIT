"""PongYa"""
def main():
    """PongYa"""
    num = int(input())
    if num%3 == 0 or num%10 == 3:
        print("PONG")
    else:
        print(num)
main()
