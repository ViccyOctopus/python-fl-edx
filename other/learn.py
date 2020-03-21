x = int(input("Enter an integer: "))
if x%2 == 0:
    print('')
    print("Even")
else:
    print('')
    print("Odd")
print("Done with conditional")

if x%2 == 0:
    if x%3 == 0:
        print("Divisible by 2 and 3")
    else:
        print("Divisible by 2 and not by 3")
elif x%3 == 0:
    print("Divisble by 3 and not by 2.")

if x < y and x < z:
    print("x is least")
elif y < z:
    print("y is least")
else:
    print("z is least")

x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))
if x == y:
    print("x and y are equal")
    if y != 0:
        print("therefore, x/y is ", x/y)
elif x < y:
    print("x is smaller")
else:
    print("y is smaller")
print("thanks!")

x = 1 #x = 1
y = 2 #y = 2
y = x #y = 1 now
x = y #x = 1 now, this is not the way to swap them.

x = 1
y = 2
temp = y
y = x
x = temp

hi = "hello there"
greetings = 'hello'

name = "eric"
greet = hi + name
greeting = hi + " " + name

name = 'eric'

3*'eric'
'ericericeric'

len('eric')
4

len('hi there')
8

'eric'[1]
'r'

'eric'[0]
'e'

name[0]
'e'

'eric'[1:3]
'ri'
# includes 2nd character [1] r and DOES NOT include the 4th character [3] c

'eric'[:3]
'eri'
# includes ALL character up to the 4th character [3], c

'eric'[1:]
'ric'
# includes ALL character from 2nd character onwards, not including 2nd character

'eric'[:]
'eric'
# gives you a copy of all the original characters