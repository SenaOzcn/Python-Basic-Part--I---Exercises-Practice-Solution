"""
To assign the user's name to a variable "y" you can use following command :

y = input('Input your name: ') 
"""

fname = input("Input your first name: ")
lname = input("Input your last name: ")
print("Hello " + lname + " " + fname)

"""
This code prompts the user to input their first and last name, and then it prints a message that combines the first name and last name in a specific order.

1. The first line fname = input("Input your First Name : ") gets the user's first name using the input() function and assigns it to the variable 'fname'.
2. The second line lname = input("Input your Last Name : ") gets the user's last name using the input() function and assigns it to the variable 'lname'.
3. The third line print ("Hello " + lname + " " + fname) prints a message that combines the last name and first name, 
concatenating them with the + operator and separated by a space.
"""
