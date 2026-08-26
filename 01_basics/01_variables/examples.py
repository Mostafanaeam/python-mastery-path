# ? ============================================================
# ? Python Variables
# ? ============================================================

#* Creating Variables
x = 5
y = "John"
print(x)
print(y)


x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#* Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#* Get the Type
x = 5
y = "John"
print(type(x))
print(type(y))

#*Single or Double Quotes?
x = "John"
# is the same as
x = 'John'

#* Case-Sensitive
a = 4
A = "Sally"
# A will not overwrite a

#* Variable Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#! Multi Words Variable Names
#? Camel Case
myVariableName = "John"
#? Pascal Case
MyVariableName = "John"
#? Snake Case
my_variable_name = "John"


#* Assign Multiple Values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# * One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# * Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# * Output Variables

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python is "
y = "awesome"
z =  x + y
print(z)

x = 5
y = 10
print(x + y)

# ! wrong way
# x = 5
# y = "John"
# print(x + y)

# ! The best way

x = 5
y = "John"
print(x, y)


# * Global Variables
print("=============way one=============")
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

print("=============way two=============")

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#* The global Keyword
print("=============way one=============")
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

print("=============way two=============")
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
