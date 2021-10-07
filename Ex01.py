import math


while True:
    try:
        year = int(input("Enter year: "))
        if year < 0 or year > 2005:
            print("Please input the year between 1 and 2005.")
            continue
        break
    except:
            print("Plese input interger only")

century = year/100
result = math.ceil(century)

print("Century is",result)
