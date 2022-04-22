"""BMIAgain"""
def main():
    """BMIAgain"""
    www = int(input())
    hhh = int(input())
    bmi = www/(hhh/100)**2
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi < 25:
        print("Normal")
    elif 25 <= bmi < 30:
        print("Overweight")
    elif bmi >= 30:
        print("Obese")
main()
