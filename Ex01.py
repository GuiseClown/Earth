import math



while True:
    try:
        year = int(input("Enter year: "))
        break
    except:
            print("That's not a valid option!")

century = year/100
result = math.ceil(century)



print("Century is ",result)
