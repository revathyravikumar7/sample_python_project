# variable names

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

"""# Illegal variable names

2myvar = "John"
my-var = "John"
my var = "John" """

# Camel Case
commandLine = "command Line"

# Pascal Case
CommandLine = "command Line"

# Snake Case
command_line = "command Line"

# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

veggies = ["carrot", "beetroot", "cabbage", "brinjal", "okra"]
a, b = veggies[:2]
# a, b = veggies[1,2] # not a valid syntax
print("veggies: ", a,b)

"""# slicing
[start: stop: step]
start -> default 0
stop -> stop -1 values
step -> default 1"""


print("Python is awesome")
x = "Python "
y = "is "
z = "awesome."
print(x+y+z)

x = 5
y = "John"
print(x, y) # output 5 John

print('Hello', 'World') # output -> Hello World
print('Hello'+ 'World') # output -> HelloWorld

# Global Variables

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
# Global and local variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# global keyword
x = "awesome"


def myfunc():
  # global x
  x = "fantastic"
  print("Python is inside method " + x)


print("Python is after function call " + x)
myfunc()
print("Python is outside method after function call " + x)


