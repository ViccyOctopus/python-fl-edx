shopping = []
count = 0

how_many = input("how many items of shopping do you have? ")
how_many = int(how_many)

for item_number in range(how_many):
    item = input("what is item number " + str(item_number +1) + "? ")
    shopping.append(item)

print("-----Your Shopping List-----")
for item in shopping:
    print(item)

total=len(shopping)

print("You have "+ str(total) + " items in your shopping list")

