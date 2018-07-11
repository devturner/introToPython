__author__ = 'christurner'
author = "Chris Turner"
nameLength = len (author)
print "my name is " + str(nameLength) + " characters long"

nameParts = author.split(" ")
print len (nameParts)

print nameParts[1] + ", " + nameParts[0]