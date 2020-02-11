ans = 0
neg_num = False
x = int(input("Enter an integer: "))
if x < 0:
    neg_num = True
while ans**2 < x:
    ans = ans + 1
if ans**2 == x:
    print("Square root of", x, "is", ans)
else: 
    print(x, "is not a perfect square")
    if neg_num:
        print("Just checking... did you mean", -x, "?")