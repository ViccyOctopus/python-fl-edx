import math
while True:
    sidesq = input("what is the side of the square?: ")
    sidesq = int(sidesq)
    sidestri = 2*sidesq
    sidestri = int(sidestri)
    ans = math.sqrt((((sidesq*sidesq)*4)/math.sqrt(3)))
    mean = ((sidestri + sidesq)/2)
    difference = float(ans - mean)
    difference = str(difference)

    mean = str(mean)

    ans = str(ans)


    print("the mean is " + mean)
    print("the estimated area of the equilateral triangle is " + ans)

    print("the difference would be " + difference)