

a = input("Enter you number: ")
# a = [8, 1, 4, 8, 10, 1, 5, 7, 8, 7] 
# a = [28, 19, 13, 6, 34, 48, 50, 3, 47, 18, 15, 34, 16, 11, 13, 3, 2, 4, 46,
# 6, 7, 3, 18, 9, 32, 21, 3, 21, 50, 10, 45, 13, 22, 1, 27, 18, 3, 27, 30,
# 44, 12, 30, 40, 1, 1, 31, 6, 18, 33, 5]

def firstDuplicateSet(a):
    myset = set()
    for i in a:
        if i in myset:
            return i
        myset.add(i)

    return -1
print(firstDuplicateSet(a))