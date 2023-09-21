"""
Check number is Binary or not
Binary number is 0 1 01 010 111 ...
"""

inpNum = input("Enter number to check binary : ")


def binary_check(num):
    if num == '0' or num == '1':
        return 'Binary'
    else:
        return 'Non Binary'


isBinary = 0
for i in inpNum:
    if binary_check(i) == 'Non Binary':
        isBinary = 1
        break

if isBinary == 0:
    print("Given number is Binary")
else:
    print("Given number is not Binary")
