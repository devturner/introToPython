__author__ = 'christurner'

"""1: Create a new program that asks the user for the name of a household item, and then asks for its estimated value. Store, both pieces of data in a text file called, HomeInventory.txt"""

"""this works!!!

householdItem = input("Name something you keep in your house. ")
price = input("What is the value of the item? ")

fob=open('test.txt','w') #on my mac, this just saves/ creates the file in the same directory as the python file.
fob.write(str("Your household product is a {} & it is worth {}.\n" .format(householdItem, price)))
fob.write("{}, {}" .format(householdItem, price))
fob.close()


"""


householdItem = ""
price = ""

while(True):
    householdItem = input("Name something you keep in your house. ")
    price = input("What is the value of the item? ")
    if(householdItem.lower()== "exit"): break
    else:
        fob=open('test.txt','a') #on my mac, this just saves/ creates the file in the same directory as the python file.
        fob.write(str("Your household product is a {} & it is worth {}.\n" .format(householdItem, price)))
        #fob.write("{}, {}" .format(householdItem, price))
        fob.close()
