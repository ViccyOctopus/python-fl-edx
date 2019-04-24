command = input("add or subtract ")

print("let's " + command + " some numbers")
magnitude1 = input("Number 1: ")
magnitude2 = input("Number 2: ")
number1 = int(magnitude1)
number2 = int(magnitude2)
if command == "add":
    result1 = number1 + number2
    outcome1 = str(result1)
elif command == "subtract":
    result2 = number1 - number2
    outcome2 = str(result2)
if command == "add":
    print(magnitude1 + "+" + magnitude2 + "=" + outcome1)
elif command == "subtract":
    print(magnitude1 + "-" + magnitude2 + "=" + outcome2)