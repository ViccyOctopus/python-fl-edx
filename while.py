#while statement == True:
#    print("do this")

guess = input("Guess my name: ")
count = int(0)
while guess != "Victoria":
    guess = input("wrong - guess again: ")
    count +=1
    total = str(count)
print("Well done, it only took you " + total + " attempts to guess the right name")
