"""computational thinking exam"""
print("Various commands you can perform\nA) Add\nE) Edit\nQ) Quit")
item = []
command= ""

while True:
    command = input("Enter a command from the available commands: ")

    if command.upper() == "A":
        print("you are in Add mode")

        item_name = input("Enter the name of the item: ")
        item_price = int(input("Enter the price of the item: "))
        item_quantity = int(input("Enter quantity of item: "))

        new_item = {"name": item_name, "price": item_price, "quantity": item_quantity}
        item.append(new_item)

    elif command.upper() == "E":
        print("you are in Edit mode")

    elif command.upper() == "V":
        print("Items in the list are:\n")
        print("Name\tPrice\tQuantity")
        for i in item:
            print(i["name"] + "\t" + str(i["price"]) + "\t" + str(i["quantity"]))

    elif command.upper() == "Q":
        print("Exiting.......")
        break
    else:
        print("Wrong command ... Enter valid command")
    print("\n\n")

print(item)
