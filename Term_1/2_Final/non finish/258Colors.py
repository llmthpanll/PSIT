"""colors"""
def main():
    """colors"""
    color_a = input()
    color_b = input()
    if color_a == "Red" and color_b == "Yellow":
        print("Orange")
    elif color_a == "Red" and color_b == "Blue":
        print("Violet")
    elif color_a == "Yellow" and color_b == "Red":
        print("Orange")
    elif color_a == "Yellow" and color_b == "Blue":
        print("Green")
    elif color_a == "Blue" and color_b == "Yellow":
        print("Green")
    elif color_a == "Blue" and color_b == "Red":
        print("Violet")
    elif color_a == "Red" and color_b == "Red":
        print("Red")
    elif color_a == "Yellow" and color_b == "Yellow":
        print("Yellow")
    elif color_a == "Blue" and color_b == "Blue":
        print("Blue")
    else:
        print("Error")
main()
