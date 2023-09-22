"""
Find LCM of two given number
"""
inpNum = input("Enter two number separated by space : ").split(" ")
inpNum1 = int(inpNum[0])
inpNum2 = int(inpNum[1])


def find_lcm(num1, num2):
    if num1 == 1 and num2 == 1:
        return 1
    for i in range(2, (num1 * num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            return i * find_lcm(num1 // i, num2 // i)
        elif num1 % i == 0:
            return i * find_lcm(num1 // i, num2)
        elif num2 % i == 0:
            return i * find_lcm(num1, num2 // i)


print("LCM for ", inpNum1, "and ", inpNum2, " is ", str(find_lcm(inpNum1, inpNum2)))
