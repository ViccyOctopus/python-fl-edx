print("GROCERY BOT")

ap = "Apples"
bna = "Bananas"
br = "Bread"
mk = "Milk"
eg = "Eggs"
chnk = "Chicken"

Gro = []
GroList = list(Gro)

def basic():
    command = input("What would you like to add? ")
    if command == ap:
        GroList.append(ap)
    if command == bna:
        GroList.append(bna)
    if command == br:
        GroList.append(br)
    if command == mk:
        GroList.append(mk)
    if command == eg:
        GroList.append(eg)
    if command == chnk:
        GroList.append(chnk)
    return command
    
def response(q1):
    print("Ok! We will add " + q1)
    print(GroList)

talking = True
while talking:
    command = basic()
    response(command)
    final_response = input("Do you want to add anything else? ")
    if final_response == "yes":
        talking = True
    else:
        talking = False


