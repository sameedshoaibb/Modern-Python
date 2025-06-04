# Variable = A container for storing data values(String, Integer, Float, Boolean)
# A variable behaves as it was defined

first_name = "Sameed"
age = 20
price = 19.99
for_sale = True

print(f"{first_name} is a good name")
if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")

#Type Casting = The process of converting the value of one data type to another

#Logical Operators = and = both conditions must be true
                   # or= atleast one condition is true
                  #  not = negates the condition

# Comparison Operators = ==, !=, >, <, >=, <=
# Arithmetic Operators = +, -, *, /, %, **(exponent), //(floor division)
# Assignment Operators = =, +=, -=, *=, /=, %=, **=, //=
# Identity Operators = is, is not
# Membership Operators = in, not in
# Bitwise Operators = &, |, ^, ~, <<, >>
# format specifiers = {value:flags} format a value based on what flags are inserted
# While Loop = A loop that continues until a condition is false

while name == "":
    print("Please enter your name")
    name = input("Enter your name: ")
print(f"Hello, {name}!")

# collection = A collection is a data type that can hold multiple values
# List = A collection of ordered items that can be changed and allows duplicates
fruits = ["apple", "banana", "cherry"]
# Tuple = A collection of ordered items that cannot be changed and allows duplicates
fruits_tuple = ("apple", "banana", "cherry")
# Set = A collection of unordered items that cannot be changed and does not allow duplicates
fruits_set = {"apple", "banana", "cherry"}
# Dictionary = A collection of key-value pairs that can be changed and allows duplicates
fruits_dict = {
    "apple": 1,
    "banana": 2,
    "cherry": 3
}