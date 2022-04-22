"""a"""
def main():
    """a"""
    studict = []
    while True:
        stud = input()
        if stud == "END":
            break
        studict.append(stud[:4])
    old_year = 0
    for i in sorted(set(studict)):
        year = i[:2]
        print(year if year != old_year else "--", int(i[2:4]), studict.count(i))
        old_year = year
main()
