"""Circular II"""
def main():
    """Circular II"""
    x_my = float(input())
    y_my = float(input())
    radius_my = float(input())
    x_fri = float(input())
    y_fri = float(input())
    radius_fri = float(input())
    distance = (((x_my-x_fri)**2)+((y_my-y_fri)**2))**0.5
    if distance >= radius_my + radius_fri:
        print("No")
    elif distance < radius_my + radius_fri:
        print("Yes")
main()
