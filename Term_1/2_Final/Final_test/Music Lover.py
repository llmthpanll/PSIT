"""Music Lover"""
def main(num):
    """Music Lover"""
    this_dict = dict()
    for _ in range(num):
        band, song = input().rstrip().split("-")
        this_dict.setdefault(band, []).append(song)
    for i in this_dict.keys():
        print(i)
        for j in range(len(this_dict[i])):
            print(this_dict[i][j])
main(int(input()))
