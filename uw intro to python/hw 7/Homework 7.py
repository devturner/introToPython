# -------------------------------------------------#
# Title: Homework 7
# Dev:   Chris Turner
# Date: July 24th
# Desc: Exception handling & Pickling
# ChangeLog: (Who, When, What) <Example: RRoot, 01/04/2012, Added more code>
#-------------------------------------------------#

"""
Now that you have reviewed the websites and videos, try to do the following task. (This project is similar to the last one!)

 1: Create an example of how you would use Python Exception Handling. Make sure to comment your code.

 2: Create an example of how you would use Python Pickling. Make sure to comment your code.

"""


#Python Exception Handling

#we ask the human for a number, but if we are given a none number we show them the error of their ways.

try:
    number = int(float(input("Put in a whole number:")))
    print(number)
except:
    print("There was an error, your entry:", (number), "was not a whole number!")



#Python Pickling


import pickle

CustID = int(input("Enter an Id Number: "))
CustName = str(input("Enter a Customer Name: "))
CustomerList = [CustID, CustName]
print(CustomerList)

objFile = open("Customers.dat", "ab")
pickle.dump(CustomerList, objFile)
objFile.close()

objFile = open("Customers.dat", "rb")
objFileData = pickle.load(objFile)
objFile.close()

print(objFileData)











