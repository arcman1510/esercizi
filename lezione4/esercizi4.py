#let's try to define a funciton named "subtract" ourselvese
#it should take 2 parameters
#inside the funciton, it should subtract the to
#then, return the result
#after you defined it, call the funciton with some arguments

def subtract(a, b):
    res = a - b
    return res

myresult = subtract(4, 1)
print(myresult)

def check_value(num:int):
    if num > 5:
        print("num is greater than 5")
    elif num < 5:
        print("num is less than 5")
    else:
        print("num is equal to 5")
check_value(10)