"""test"""
def main():
    """test"""
    my_ans=[]
    txt = input("Enter 2 imtegers : ").split()
    txt = sorted(txt)
    if txt[0].isdigit() == False or txt[1].isdigit() == False:
        print("Invalid input !!!")
    else:
        num_min = min(int(txt[0]), int(txt[1]))
        num_max = max(int(txt[0]), int(txt[1]))
        for i in range(num_min, num_max+1):
            if i%2==1:
                my_ans.append(i)
        for j in range(len(my_ans)):
            ans = str(my_ans).replace(", ", "+").replace("[", "").replace("]", "")
        print("%s = %d" %(ans, (sum(my_ans))))
main()
