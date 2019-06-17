def basic():
    print("I can do many things!")
    print("I can:")
    print("- add numbers")
    print("- subtract numbers")
    print("- find the area of a rectangle")
    print("- average numbers")
    command = input("What would you like to do? ")
    handleReponse(command)

def handleReponse(command):
    print("TODO: deal with what they said: " + command)

i = 0
while i < 5:
    basic()
    i += 1