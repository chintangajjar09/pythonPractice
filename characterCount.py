"""
Find character count in string
"""

inpStr = input("Enter String to count each character : ")

strDct = {}

for chr in inpStr:
    if chr not in strDct.keys():
        strDct[chr] = 1
    else:
        strDct[chr] = int(strDct[chr]) + 1

print("Dictionary Sorted by values : ", sorted(strDct.items(), key=lambda x: x[1], reverse=True))  # Sorted by values
print("Dictionary Sorted by keys : ", sorted(strDct.items()))  # sorted by keys

for key in strDct.keys():
    print("Character ", key, " is present ", strDct[key], "times")
