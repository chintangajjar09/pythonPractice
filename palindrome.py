"""
Check number is palindrome or not
Palindrome number os string is Reverse of string is same as original string
Palindrome number is 121 1221 111 1223221
"""

inpNum = input("Enter number to check Palindrome : ")

revNum = inpNum[::-1]

if inpNum == revNum:
    print("Entered Number is Palindrome")
else:
    print("Entered Number is not Palindrome")

# Iterative method

revNum1 = ''
lenNum = len(inpNum) - 1

while lenNum >= 0:
    revNum1 = revNum1 + inpNum[lenNum]
    lenNum -= 1

if inpNum == revNum1:
    print("Entered Number is Palindrome")
else:
    print("Entered Number is not Palindrome")

