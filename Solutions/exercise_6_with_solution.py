values = input("Input soma come seprated numbers: ")
list = values.split(",")
tuple = tuple(list)
print("List: ", list)
print("Tuple: ", tuple)

"""
1. The first line values = input("Input some comma seprated numbers : ") gets a string of numbers separated by commas from the user using the input()
function and assigns it to the variable 'values'.
2. The second line splits the string of numbers into a list of individual numbers using the split() method and assigns it to the variable 'list'.
This method takes a separator as input, in this case ',' (comma) and returns a list of substrings that were separated by the separator.
3. The third line converts the list into a tuple using the tuple() function and assigns it to the variable 'tuple'.
4. The fourth line prints the list to the console.
5. The fifth line prints the tuple to the console.
"""
