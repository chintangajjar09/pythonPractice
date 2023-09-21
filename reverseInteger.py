"""
Reverse Integer value
"""


inpNum = input("Enter number to reverse : ")
newNum = inpNum[::-1]
print("Reverse Number is : ", newNum)

lenNum = len(inpNum) - 1
reverseLst = []
while lenNum >= 0:
    # print(lenNum)
    reverseLst.append(inpNum[lenNum])
    lenNum -= 1

print("Reverse Number is : ", ''.join(reverseLst))
