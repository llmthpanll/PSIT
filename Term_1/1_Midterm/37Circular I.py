"""Circular I"""
def main():
    """Circular I"""
    my_x = float(input())
    my_y = float(input())
    radius = float(input())
    m_x = float(input())
    m_y = float(input())
    distance = (((my_x-m_x)**2) +((my_y-m_y)**2))**0.5
    if distance <= radius:
        print("Yes")
    elif distance > radius:
        print("No")
main()
