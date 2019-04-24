import math
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))

delta=(b**2)-(4*a*c)
num1 = float((-b-math.sqrt(delta))/(2*a))
num2 = float((-b+math.sqrt(delta))/(2*a))

print(num1)
print(num2)