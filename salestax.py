import math

print("What is the original price of the product?")
oriPrice = input()
intPrice = int(oriPrice)

totTax = (intPrice*0.006)
endPrice = (intPrice - totTax)
Price = str(endPrice)

print("Your total price after taxes would be " + Price + ".")