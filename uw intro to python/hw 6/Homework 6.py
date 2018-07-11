# -------------------------------------------------#
# Title: Homework 6
# Dev:   Chris Turner
# Date: 07-16-2014
# Desc: To-do list
# ChangeLog: Added Function Support July 21, 2014
# -------------------------------------------------#
"""
Now that you have reviewed the websites and videos, try to do the following task. (This project is similar to the \
        last one!)

 1: Create new manages a "ToDo list." The ToDo file will contain two columns of data, separated by a comma, called: Task, Priority. Use a Python Dictionary to work with the data while the program is running. Also use Try - Catch blocks to manage user input errors.

When the program starts,

1. load the any data you have in a text file called ToDo.txt into a python Dictionary.
2. Display the contents of the file to the user.

3. Allow the user to Add tasks, Remove, and save the task to a file using numbered choices like this:


    print "1. Add task"

    print "2. Remove task"

    print "3. Save tasks to file"


******************


HOMEWORK 6 =     MAKE THIS WORK WITH FUNCTIONS.


******************
"""
#  -------------------------------------------------#




#-- Data --#
# declare variables and constants

toDo_list = {}
menu_choice = 0
#-- Processing --#
# perform tasks

def print_menu():
    print('      Task Menu: ')
    print ('         1. Print Tasks on the list')
    print ('         2. Add a task')
    print ('         3. Remove a task')
    print ('         4. Lookup a task')
    print ('         5. Save the list to the text file')
    print ('         6. Exit')

def read():
    with open('ToDo.txt') as f:
        for line in f:
            (tasks, priority) = line.split(',')
            toDo_list[(tasks)] = priority


#-- Presentation (I/O) --#
# get user input

def processing():
    menu_choice = None
    while menu_choice != "6":
        menu_choice = input("     Type in a number (1-6): ")
        if menu_choice == "1":
            read()
            print ("Tasks:")
            for x in toDo_list.keys():
                print (x, ": ", toDo_list[x].rstrip('\n'))
        elif menu_choice == "2":
            print ("Add task")
            name = input("Task: ")
            means = input("Priority: ")
            toDo_list[name] = means
        elif menu_choice == "3":
            print ("Remove word")
            name = input("Word: ")
            if name in toDo_list:
                del toDo_list[name]
                print (name, " was removed.")
            else:
                print (name, " was not found.")
        elif menu_choice == "4":
            print ("Lookup Task")
            name = input("Task: ")
            if name in toDo_list:
                print ("The priority of", name, "is: ", toDo_list[name])
            else:
                print ("No task called", name, "was found.")
        elif menu_choice == '5':
            clean_dict = toDo_list
            clean_dict = {key.strip(): item.strip() for key, item in toDo_list.items()}
            fob=open('ToDo.txt', 'w')
            for strKey, strValue in clean_dict.items():
                fob.write(strKey + "," + strValue + "\n")
            fob.close()
            print("Your task list was saved.")
        elif menu_choice != "6":
            print_menu()

print_menu()
processing()
