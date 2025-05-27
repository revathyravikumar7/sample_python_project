
#--------------------------------------------
"""Built-in Data Types
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType"""
#--------------------------------------------
# Getting the Data Type
x = 5
print(type(x))
#--------------------------------------------
# Setting the Specific Data Type
x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j) # Complex numbers are written with a "j" as the imaginary part
#--------------------------------------------
# Type Conversion OR Type Casting

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3")
#--------------------------------------------
import random

print(random.randrange(1,10))

#--------------------------------------------
# Strings
print("Hello")
print('Hello')

#--------------------------------------------

# Quotes Inside Quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#--------------------------------------------
# Multiline Strings or docstrings or multiline comments (when used in functions) (three single quotes OR three double quotes)
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#--------------------------------------------
# Strings are Arrays
a = "Hello, World!"
print(a[1])

# Strings are Arrays
for x in "banana":
  print(x)

# String Length
a = "Hello, World!"
print(len(a))

# Check String
txt = "The best things in life are free!"
print("free" in txt)

# Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)

#------------------------------------------------

# slicing syntax -> sequence[start:stop:step]

b = "Hello, World!"
print(b[2:5]) # Get the characters from position 2 to position 5 (not included)

# Slice From the Start
b = "Hello, World!"
print(b[:5])

# Slice To the End
b = "Hello, World!"
print(b[2:])

# Negative Indexing
b = "Hello, World!"
print(b[-5:-2])
#------------------------------------------------
# Upper Case
a = "Hello, World!"
print(a.upper())
# Lower Case
a = "Hello, World!"
print(a.lower())

# Remove Whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

# Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
#------------------------------------------------
# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

# To add a space between them, add a " "
a = "Hello"
b = "World"
c = a + " " + b
print(c)