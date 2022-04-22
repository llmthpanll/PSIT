"""VerticalHistogram"""
def sortalgo(var):
    """สำหรับเพื่อนที่แอบเข้ามาดูโค้ดเรา function นี้จะคืนค่าให้ function sorted โดย
    sorted จะทำการเรียงด้วยค่าที่รีเทินนะ ค่าน้อยอยู่หน้า ค่ามากอยู่หลัง"""
    char = var[0]
    return ord(char) + (100 if char.isupper() else 0)

def main():
    """VerticalHistogram"""
    string = input()
    alphacount = tuple(sorted({i: string.count(i) for i in string}.items(), key=sortalgo))
    for i in range(max({i[1] for i in alphacount}), 0, -1):
        print("{:03d}".format(i), end=" ")
        for _, count in alphacount:
            print(" " if count < i else "*", end=" ")
        print()
    print("    " + " ".join([i[0] for i in alphacount]))
main()
