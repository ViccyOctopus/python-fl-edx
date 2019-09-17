import math

print("What is the original price of the product?")
oriPrice = input()
intPrice = int(oriPrice)

totTax = (intPrice*1.06)
endPrice1 = (totTax - intPrice)
endPrice2 = (endPrice1 + intPrice)
Price = str(endPrice2)

print("Your total price after taxes would be " + Price + ".")