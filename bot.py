print("Hi, I am your personal bot.")
print("Please answer my questions with lower-case only, and without spaces after your answer.")
print("Let's get started")
users_name = input("What is your name? ")
if users_name == "Victoria":
    print("Hey, I know you! Welcome back!")
else:
    print("Hello, nice to meet you " + users_name + "!")

phrase = input("Talk to me about anything: ")
if phrase == "hi" or phrase == "hey":
    print("Hello!")
elif phrase == "what's your name" or phrase == "whats your name" or phrase == "what is your name" or phrase == "what's your name?" or phrase == "what is your name?":
    print("My name is Marvin!")
elif phrase == "what's up" or phrase == "whats up" or phrase == "what's up?" or phrase == "whats up?":
    print("Not much, just talking to you :)")
else:
    print("Sorry, I don't understand this :(")

command = input("How about we add some numbers? ")
if command == "okay" or command == "alright" or command == "let's do it" or command == "sure" or command == "ok":
    print("Lets add some numbers!")
    input1 = input("Number 1> ")
    input2 = input("Number 2> ")
    number1 = int(input1)
    number2 = int(input2)
    result = number1 + number2
    output = str(result)
    print(input1 + " + " + input2 + " = " + output)
else:
    print("Sorry, I don't understand this :(")

command2 = input("Wanna subtract some numbers? ")
if command2 == "sure" or command2 == "alright" or command2 == "okay" or command2 == "let's do it" or command2 == "ok" or command2 == "yes":
    print("Let's subtract some numbers!")
    input1 = input("Number 1> ")
    input2 = input("Number 2> ")
    number1 = int(input1)
    number2 = int(input2)
    result = number1 - number2
    output = str(result)
    print(input1 + " - " + input2 + " = " + output)
else:
    print("Sorry, I don't understand this :(")

command3 = input("I can help you find the area of a rectangle as well, wanna try? ")
if command3 == "sure" or command3 == "alright" or command3 == "okay" or command3 == "let's do it" or command3 == "ok" or command3 == "yes":    
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
elif command3 == "no" or command3 == "nah" or command3 == "x" or command3 == " ":
    print("Alright, take care")
else:
    print("Sorry, I don't understand this :(")

command4 = input("Would you like to learn how to average? ")
if command4 == "sure" or command4 == "alright" or command4 == "okay" or command4 == "let's do it" or command4 == "ok" or command4 == "yes":
    how_many = input("How many numbers? ")
    how_many = int(how_many)
    total = 0
    for number_count in range(how_many):
        number = input("Enter number "+ str(number_count +1) + "> ")
        total = total + int(number)
    result = total / how_many
    print("The average = " + str(result))



print("Bye!")
