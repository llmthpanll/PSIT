"""Fever"""
def main():
    """Fever"""
    temp = float(input())
    ans = ""
    if temp >= 36.0 and temp < 38.0:
        ans = "No Fever"
    elif temp >= 38.0 and temp < 39.0:
        ans = "Mild Fever"
    elif temp >= 39.0 and temp < 40.0:
        ans = "High Fever"
    elif temp >= 40.0:
        ans = "Very High Fever"
    print(ans)
main()
