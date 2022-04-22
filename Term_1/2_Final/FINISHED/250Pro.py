"""Pro"""
def main():
    """function"""
    come_x = int(input())           #โปรมา x
    pay_y = int(input())            #จ่าย
    pay_of_person = int(input())    #ราคาต่อคน
    if_come = int(input())          #มาจริง z คน
    #เช็คมาพอดีโปร
    if if_come%come_x == 0:
        ans = ((if_come/come_x)*pay_y)*pay_of_person
        print("%d" %ans)
    elif if_come < come_x:
        ans_2 = if_come*pay_of_person
        print("%d" %ans_2)
    elif if_come%come_x != 0:
        ans_3 = ((if_come//come_x)*pay_y)*pay_of_person
        ans_4 = (if_come%come_x)*pay_of_person
        print("%d" %(ans_3+ans_4))
main()
