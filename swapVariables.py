"""
Swap two variables value
"""

# Without using third variable and possible way in python
a = 2
b = 3

print(" a : ", a, " b : ", b)

a, b = b, a

print(" a : ", a, " b : ", b)

# With using third variable
t = a
a = b
b = t

print(" a : ", a, " b : ", b)

# Without using third variable
a = a + b
b = a - b
a = a - b

print(" a : ", a, " b : ", b)