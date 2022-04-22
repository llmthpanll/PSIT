"""Timing"""
def main():
    """Timing"""
    time = int(input())
    seconds = time%60
    minutes = time//60
    hours = minutes//60
    minutes = minutes%60
    days = hours//24
    hours = hours%24
    print(days, hours, minutes, seconds)
    #print("%d %d %d %d %d" %(days, hours, minutes, seconds))
main()
