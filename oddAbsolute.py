def calculateAbsolute():
    
    # This first line is provided for you
    in_num = int(input("Enter a number: "))
    n = in_num
    #print(n)
    x = n - 21
    #print(x)
    import math 
    abs_x = math.fabs(x)
    if n > 21:
        z = abs_x * 2
    else:
        z = abs_x
    z = int(z)
    print('Result:', z)

    # end assignment

## If you want to test locally run > python payCalculator.py

if __name__ == "__main__":
    calculateAbsolute()
