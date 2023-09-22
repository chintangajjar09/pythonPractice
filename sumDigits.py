"""
Sum of Digits using recursion
"""

inpNum = int(input("Enter number wanted to sum each digit : "))


def sum_digit(num):
    print(num)
    if num < 10:
        return num
    else:
        return num % 10 + sum_digit(num//10)


print("Sum of each Digit : ", str(sum_digit(inpNum)))

