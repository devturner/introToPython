__author__ = 'christurner'
"""
1: Create new program that asks the user for the name of a household item, and then asks for its estimated value.

When the program starts, load the any data you have in the text file called HomeInventory.txt (from homework 3) into a list. Think of it as creating a database table or spreadsheet in Memory.
Ask the user for new entries and store them in the tuple;.
Ask the user, when the program exits, if they would like to save/add the data to a text file called, HomeInventory.txt.

"""
#create a list of the txt file.
#list the data that is already in the txt file:

print("Reading the inventory into lists")
fob=open('Homeinventory.txt','r')
lines = fob.readlines()
for i in lines:
    print(i)
fob.close()

#print(lines) - this was test code

#ask the user for their input
#householdItem = input(str("List another thing you keep in your house. "))
#price = input(str("What is the value of the item? "))

while (True):
    householdItem = input("List another thing you keep in your house. Type exit to quit ")
    if householdItem == "exit": break
    price = input("What is the value of the item? Type exit to quit")
    lines += ("{},{} \n" .format(householdItem, price))


#if(input("Type EXIT to stop or enter to add another item") == "EXIT"): break

#.append works the same as += in this case. I had to use the {} because if I didn't it would add the 2 items separately to the end of the list, this is not what I wanted.

#print(i) #- this was test code

#ask if the user wants to store their new data into the file


choice = input("Yes or No - Would you like to store your new item to the list?")


if (choice == "Yes" or "yes"):
    fob=open('Homeinventory.txt', 'w') #on my mac, this just saves/ creates the file in the same directory as the python file.
    for i in lines:
        fob.write(i)
    #fob.write(str("{},{} \n" .format(householdItem, price))) --- this is a relic from older code that did not add the items to the list. It worked to add the item to the txt file, but not the list.
    fob.close()
    print("Your item was saved!")
    input("\n\nPress the enter key to exit.")
elif (choice == "No" or "no"):
    print("No data was saved!")
    input("\n\nPress the enter key to exit.")

