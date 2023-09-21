"""
Check input number is Prime or not
Prime number can be divided by 1 or itself
Example of Prime numbers are 2,3,5,7,13,17
"""

inpNum = int(input("Enter number to check Prime Number : "))

nonPrimeFlag = 0
divisonNum = 0

if inpNum == 2 or inpNum == 3:
    print("Given ", inpNum, " Prime")
else:
    for i in range(2, inpNum - 1):
        # print(i)
        if inpNum % i == 0:
            # print(i)
            nonPrimeFlag = 1
            divisonNum = i
            break

    if nonPrimeFlag == 1:
        print("Given ", inpNum, " is not Prime as got divided by ", divisonNum)
    else:
        print("Given ", inpNum, " is  Prime")



