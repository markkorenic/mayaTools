"""
Comments are used to provide descriptions or notes 
in your code.
You can make large blocks of comments by surrounding your text
in sets of 3 quotation marks.
"""
# You can also use the pound sign.

""" 
A Variable is used to store data.
In this case 'h' is the varaible to which
we assign the value of the string 'Hello'
"""
h = 'Hello'
print h

"""
Variables can hold any data types.
For instance, a variable can hold a list.
A list is just like a grocery list.
In this example we will use a list of numbers 
also know as integers.
"""

l = (1, 2, 3)
print l

""" 
If we wanted to print every number in our 'l' list,
we need to use a loop.  In this example we will use
a for loop.
"""
for each in l:
	print each

""" 
Each item in a list can also be viewed as the
'index number' of that list
So on a grocery list you would have item 1: Milk, item 2: Bread,
and item 3: Eggs.  Python starts with 0 instead of 1.
"""
grocery_list = ('Milk', 'Bread', 'Eggs')


"""
We can use a differnt type of loop to know 
the number associated with each item on the list.
First lets look at len.  Len means length.
""" 
#This will tell us that we have 3 items in grocery_list.
print len(grocery_list)


# The number of items in a list is also called range.
# So to do something for each item in the range of the 
# length of grocery list we can do this.
for index in range(len(grocery_list)):
	print index # This will print the current items index number.
	""" If we want to find out if the current item
		is Milk, we can use a condition. """
	if grocery_list[index] == 'Milk':
		print grocery_list[index]



""" If you want to pick a paticular item from a list
you can refer to it's index number like this """
print grocery_list[2]

""" Python has many different libraries to handle
all sorts of functions.
For instance we can import Python's date and time library 
to get the time.
"""
import datetime
print datetime.datetime.now()

""" The same thing applies for maya commands.
In Maya Python serves as a wrapper for mel commands.
To use those commands we need to import that library into Maya.
When we import that library we will assign it to
a variable called "cmds".
"""
import maya.cmds as cmds

""" Now if we want to use a maya command,
we can call on it like this
"""
cmds.joint()

"""
Maya commands have 'flags',  Flags can be used to modify or query a command.
Lets name our joint and place it somewhere in our scene.
"""
cmds.joint(name='MyJoint', position=['1.0', '2.0', '0.0'])