"""
Check if input number is armstrong or not
Armstrong number is the number if it individual number cube sum is same as original number
"""

inpNum = input("Enter number to check number is armstrong or not : ")

numLen = len(inpNum)
numSum = sum([int(numChar) ** numLen for numChar in inpNum])

if numSum == int(inpNum):
    print("Given ", inpNum, " is armstrong as individual number cube sum is ", numSum)
else:
    print("Given ", inpNum, " is not armstrong as individual number cube sum is ", numSum)