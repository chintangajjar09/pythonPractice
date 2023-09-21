"""
Print Fibonacci series : 0 1 1 2 3 5 8 13
"""

inpNum = input("Enter length of fibonacci Series : ")

startNum = 0
secondNum = 1

opLst = [str(startNum), str(secondNum)]

for i in range(1, int(inpNum) - 1):
    num = startNum + secondNum
    opLst.append(str(num))
    startNum = secondNum
    secondNum = num

print("Fibonacci series is : ", ' '.join(opLst))

# Recursive method

opLst1 = []


def fibonacci(funinnum):
    if funinnum == 0:
        return 0
    if funinnum == 1:
        return 1
    return fibonacci(funinnum - 1) + fibonacci(funinnum - 2)


for i in range(0, int(inpNum)):
    opLst1.append(str(fibonacci(i)))

print("Fibonacci series is : ", ' '.join(opLst1))
