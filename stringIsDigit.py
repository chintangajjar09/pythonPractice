"""
Check input string is digit
"""
import re

inpStr = input("Enter String to check all numeric : ")

if inpStr.isdigit():
    print("String is all numeric")
else:
    print("String is not numeric")

# With Regular expression
if re.match(r"^[0-9]+$", inpStr):
    print("String is all numeric")
else:
    print("String is not numeric")
