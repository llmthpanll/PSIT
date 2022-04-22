"""PointInCircle"""
def main():
    """PointInCircle"""
    xxx = float(input())
    yyy = float(input())
    radius = float(input())
    x_n = float(input())
    y_n = float(input())
    distance = (((xxx-x_n)**2) +((yyy-y_n)**2))**0.5
    if distance <= radius:
        print("True")
    elif distance > radius:
        print("False")
main()
