"""Cat Parade"""
def main():
    """Cat Parade"""
    position = []
    spec = []
    while True:
        txt = input().split(", ")
        #pop ออกเมื่อเจอ dog
        if txt == ["IT\'S A DOG"]:
            position.pop()
            continue
        if txt == ['END']:
            break
        position += (txt)
    #loop กรองสายพันธุ์ว่ามีเท่าไร
    for i in range(len(position)):
        if position[i] not in spec:
            spec.append(position[i])
    #เรียงa-z
    spec.sort()
    #loop ตอบ
    for i in range(len(spec)):
        print("%s %d %d"%(spec[i], (position.index(spec[i])+1), position.count(spec[i])))
main()
