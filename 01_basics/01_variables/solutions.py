# ? ============================================================
# ? Python Variables
# ? ============================================================


#! ------------------------------------------------------------
#! Exercise 1 — Creating Variables
#! ------------------------------------------------------------

name = "Mostafa"
age = 20
country = "Egypt"


#! ------------------------------------------------------------
#! Exercise 2 — Changing Variable Values
#! ------------------------------------------------------------
x = 10
x = 20
print(x)

# !------------------------------------------------------------
#! Exercise 3 — Casting
#! ------------------------------------------------------------
x = str(10)
y = int("20")
z = float(5)
print(x)
print(y)
print(z)

#! ------------------------------------------------------------
#! Exercise 4 — Get the Type
#! ------------------------------------------------------------
name = "Mostafa"
age = 20
height = 174.5

print(type(name))
print(type(age))
print(type(height))

#! ------------------------------------------------------------
#! Exercise 5 — Single or Double Quotes?
#! ------------------------------------------------------------
first_name = "Mostafa"
last_name = 'Naeam'

print(first_name)
print(last_name)

#! ------------------------------------------------------------
#! Exercise 6 — Case-Sensitive Variables
#! ------------------------------------------------------------
name = "Mostafa"
Name = "Ahmed"

print(name)
print(Name)


#! ------------------------------------------------------------
#! Exercise 7 — Valid Variable Names
#! ------------------------------------------------------------
myvar = "Mostafa"
my_var = "Ahmed"
_my_var = "John"
myVar = "Jane"
MYVAR = "Bob"
myvar2 = "Alice"

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)


#! ------------------------------------------------------------
#! Exercise 8 — Multi-Word Variable Names
#! ------------------------------------------------------------
# Camel Case
studentName = "Mostafa"

# Pascal Case
StudentName = "Ahmed"

# Snake Case
student_name = "John"

print(studentName)
print(StudentName)
print(student_name)


#! ------------------------------------------------------------
#! Exercise 9 — Assign Multiple Values
#! ------------------------------------------------------------
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


#! ------------------------------------------------------------
#! Exercise 10 — One Value to Multiple Variables
#! ------------------------------------------------------------
x = y = z = "Orange"
print(x)
print(y)
print(z)


#! ------------------------------------------------------------
#! Exercise 11 — Unpack a Collection
#! ------------------------------------------------------------
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#! ------------------------------------------------------------
#! Exercise 12 — Output Multiple Variables
#! ------------------------------------------------------------
x = "Python"
y = "is"
z = "awesome"
print(x+ y+ z)


#! ------------------------------------------------------------
#! Exercise 13 — Combining String Variables
#! ------------------------------------------------------------
first_name = "Mostafa"
last_name = "Naeam"
full_name = first_name + " " + last_name
print(full_name)

#! ------------------------------------------------------------
#! Exercise 14 — Adding Number Variables
#! ------------------------------------------------------------
x = 5
y = 10
print(x + y)


#! ------------------------------------------------------------
#! Exercise 15 — Different Data Types
#! ------------------------------------------------------------
x = 5
y = "John"
print(str(x) + y)


#! ------------------------------------------------------------
#! Exercise 16 — Global Variable
#! ------------------------------------------------------------
x = "awesome"
def myfunc():
  print("Python is " + x)

myfunc()


#! ------------------------------------------------------------
#! Exercise 17 — Local Variable
#! ------------------------------------------------------------
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()
print("Python is " + x) 

#! ------------------------------------------------------------
#! Exercise 18 — The global Keyword
#! ------------------------------------------------------------
def myfunc():
  global x
  x = "fantastic"
  
myfunc()
print("Python is " + x)


#! ------------------------------------------------------------
#! Exercise 19 — Variable Naming Challenge
#! ------------------------------------------------------------
my_variable = "valid"
_name = "valid"
name2 = "valid"
MyVariable = "valid"
MY_VARIABLE = "valid"



#! ------------------------------------------------------------
#! Exercise 20 — Final Challenge
#! ------------------------------------------------------------


name = "Mostafa"
age = 20
country = "Egypt"
favorite_language = "Python"
years_of_experience = 2

print("Name:", name)
print("Age:", age)
print("Country:", country)
print("Favorite Language:", favorite_language)
print("Years of Experience:", years_of_experience)