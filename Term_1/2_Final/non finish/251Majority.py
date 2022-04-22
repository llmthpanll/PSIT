"""Majority"""
def main():
    """Majority"""
    regis = int(input())
    amount = int(input())
    my_list = []
    ans = []
    for _ in range(amount):
        my_list.append(int(input()))
    for i in range(regis):
        ans.append(my_list.count(i+1))
    sort_ans = sorted(ans)
    score = sort_ans.pop()
    result = ans.index(score)
    if score >= (amount/2):
        print("%d %d" %(result+1, score))
    else:
        print(0, score)
main()
