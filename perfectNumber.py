"""
Check Number is Perfect or not
Example 6 - Divisors are 1 2 3 6 - Exclude 6 - 1+2+3 = 6 - 6 is Perfect Number
Example 28 - Divisors are 1 2 4 7 14 28 - Exclude 28 - 1+2+4+7+14 = 28 - 28 is Perfect Number
"""

inpNum = int(input("Enter number to check Perfect Number : "))

sumNum = 0

for i in range(1, inpNum):
    if inpNum % i == 0:
        sumNum += i

if inpNum == sumNum:
    print("Given number is Perfect")
else:
    print("Given number is Not Perfect")