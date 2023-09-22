"""
Find out Prime Factors
"""

inpNum = input("Enter number to find out Prime Factors : ")


def find_prime(num):
    # print(num)
    if num == 1:
        return ""
    for i in range(2, num+1):
        if num % i == 0:
            return str(i) + " " + str(find_prime(num // i))


print("Prime Factors are : ", find_prime(int(inpNum)))
