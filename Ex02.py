
while True:
    
    s = input("Input String: ")
    if not s.isalpha():
        print("Please input only String.")
        continue
    break
    
def Palindrome(s):
    return s == s[::-1]

result = Palindrome(s)


print(bool(result))
