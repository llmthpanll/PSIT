"""iPad Air"""
def main(st1, st2, st3, color):
    """iPad Air"""
    if st1 in color and st2 == '64' and st3 == 'Wi-Fi':
        print('19900')
    elif st1 in color and st2 == '256' and st3 == 'Wi-Fi':
        print('24900')
    elif st1 in color and st2 == '64' and st3 == 'Wi-Fi + Cellular':
        print('24400')
    elif st1 in color and st2 == '256' and st3 == 'Wi-Fi + Cellular':
        print('29400')
    else:
        print('Not Available')
main(input(), input(), input(), ['Space Gray', 'Silver', 'Green', 'Rose Gold', 'Sky Blue'])
