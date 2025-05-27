# Python - Format - Strings or fstrings
"""age = 36
txt = "My name is John, I am " + age
print(txt)""" # causes error

age = 36
txt = f"My name is John, I am {age}"
print(txt)

a = 37
txt = f"My father name is pope andavar, he died at the age of {a}"
print(txt)
# modifier
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
#math operations
txt = f"The price is {20 * 59} dollars"
print(txt)
#________________________________
# Escape Character
"""txt = "We are the so-called "Vikings" from the north."
print(txt)# error"""

#solution 1
txt = "We are the so-called 'Vikings' from the north."
print(txt)

#solution 2
txt = 'We are the so-called "Vikings" from the north.'
print(txt)

#solution 3 (escape characters)
txt = "we are the so-called \"Vikings\" from the north."
print(txt)

txt1 = txt.capitalize()

print(txt1)
print("inside print method: ", txt.capitalize())

#------------
#bool (Python also has many built-in functions that return a boolean value,
# like the isinstance() function,
# which can be used to determine if an object is of a certain data type:)
x = 200
print(isinstance(x, int))