
while True:
    
    s = input("Input String: ")
    if not s.isalpha():
        print("Please input only String.")
        continue
    if len(s) > 10000:
        print("Please input the length String between 1 and 10000")
        continue
    break
    
def Palindrome(s):
    return s == s[::-1]

result = Palindrome(s)

print(result)
