print("let's learn how to make milk tea! ")
question1 = input("do you know how to make milk tea? ")
if question1 == "no":
    print("it's milk added onto tea")
    tea = input("do you know how to make tea? ")
    if tea == "no":
        print("boil water first, then add a tea packet into the water and let it sit for a couple minutes")
elif question1 == "yes":
    print("that's great to hear! ")
else:
    print("i'm sorry, i don't understand, please reply with either 'yes' or 'no'.")
    
