def calculateAbsolute():

    # This first line is provided for you
    import math
    n = int(input("Enter a number: "))
    if n <= 21:
        x = abs(n-21)
    else:
        x = (abs(n-21))*2
    print(f"Result: {x}")

    # end assignment

## If you want to test locally run > python payCalculator.py

if __name__ == "__main__":
    calculateAbsolute()