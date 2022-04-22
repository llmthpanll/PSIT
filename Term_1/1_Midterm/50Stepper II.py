"""Stepper II"""
def main():
    """Stepper II"""
    num_m = int(input())
    num_n = int(input())
    if num_n < num_m:
        for i in range(num_m, num_n-1, -1):
            print(i)
    elif num_n >= num_m:
        for i in range(num_m, num_n+1, 1):
            print(i)
main()
