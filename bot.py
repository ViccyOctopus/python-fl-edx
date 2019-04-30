print("Hi, I am Marvin, your personal bot.")
print("Let's get started")
users_name = input("What is your name? ")
print("Welcome " + users_name)

print("Let's add some numbers")
input1 = input("Number 1> ")
input2 = input("Number 2> ")
number1 = int(input1)
number2 = int(input2)
result = number1 + number2
#str function to cast the variable result to a string, like this:
output = str(result)
print(input1 + " + " + input2 + " = " + result)