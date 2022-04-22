"""GraderMachine"""
def main():
    """GraderMachine"""
    start = int(input())
    end = int(input())
    ans = 0
    print("pass :", end=" ")
    if start < end:
        while start <= end:
            if start % 2 == 0:
                print(start, end=" ")
                ans += start
            start += 1
    else:
        while start >= end:
            if start % 2 == 0:
                print(start, end=" ")
                ans += start
            start -= 1
    print()
    print("Sum : %d" %ans)
main()
