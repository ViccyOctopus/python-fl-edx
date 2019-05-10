print("Hi, I am your personal bot.")
print("Please answer my questions with lower-case only, and without spaces after your answer.")
print("Let's get started")
users_name = input("What is your name? ")
if users_name == "Victoria":
    print("Hey, I know you! Welcome back!")
else:
    print("Hello, nice to meet you " + users_name + "!")

phrase = input("Talk to me about anything. ")
if phrase == "hi" or phrase == "hey":
    print("Hello!")
elif phrase == "what's your name" or phrase == "whats your name" or phrase == "what is your name" or phrase == "what's your name?" or phrase == "what is your name?":
    print("My name is Marvin!")
elif phrase == "what's up" or phrase == "whats up" or phrase == "what's up?" or phrase == "whats up?":
    print("Not much, just talking to you :)")
else:
    print("Sorry, I don't understand this :(")

command = input("I can add numbers, subtract numbers, find the area of a rectangle, or average numbers. What would you like to do? ")
if command == "add numbers" or command == "add" or "Add numbers":
    print("Lets add some numbers!")
    input1 = input("Number 1> ")
    input2 = input("Number 2> ")
    number1 = int(input1)
    number2 = int(input2)
    result = number1 + number2
    output = str(result)
    print(input1 + " + " + input2 + " = " + output)

if command == "subtract" or command == "subtract numbers" or "Subtract numbers":
    print("Let's subtract some numbers!")
    input1 = input("Number 1> ")
    input2 = input("Number 2> ")
    number1 = int(input1)
    number2 = int(input2)
    result = number1 - number2
    output = str(result)
    print(input1 + " - " + input2 + " = " + output)

if command == "find the area of a rectangle" or command == "Find the area of a rectangle" or command == "area" or command == "Area" or command == "Area of rectangle":    
    print("If you don't remember the formula for the area of a rectangle, I can help!") 
    print("Just measure any two sides that share a corner and I'll do the rest...") 
    input1 = input("Length of first side: ") 
    input2 = input("Length of other side: ") 
    side1 = int(input1) 
    side2 = int(input2) 
    area = side1 * side2 
    result = str(area) 
    print("The area of your rectangle is: " + result) 
    print("The forumula is Side 1 x Side 2: " + input1 + " x " + input2 + " = " + result)

if command == "average numbers" or command == "Average numbers":
    how_many = input("How many numbers? ")
    how_many = int(how_many)
    total = 0
    for number_count in range(how_many):
        number = input("Enter number "+ str(number_count +1) + "> ")
        total = total + int(number)
    result = total / how_many
    print("The average = " + str(result))
    
else:
    print("Sorry, I don't understand this :(")

print("Bye!")
