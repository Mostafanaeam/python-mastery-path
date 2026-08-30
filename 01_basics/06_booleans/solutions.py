# ? ============================================================
# ? Python Booleans - Solutions
# ? ============================================================


#! ------------------------------------------------------------
#! Exercise 1 — Boolean Comparisons
#! ------------------------------------------------------------

print(10 > 5)
print(10 == 10)
print(10 < 5)


#! ------------------------------------------------------------
#! Exercise 2 — Compare Variables
#! ------------------------------------------------------------

a = 50
b = 20

print(a > b)
print(a < b)
print(a == b)


#! ------------------------------------------------------------
#! Exercise 3 — Predict the Result
#! ------------------------------------------------------------

print(15 > 20)
print(15 == 15)
print(100 < 200)
print(50 == 40)


#! ------------------------------------------------------------
#! Exercise 4 — Boolean with if/else
#! ------------------------------------------------------------

age = 20

if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")


#! ------------------------------------------------------------
#! Exercise 5 — Compare Two Numbers
#! ------------------------------------------------------------

x = 100
y = 250

if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")


#! ------------------------------------------------------------
#! Exercise 6 — bool() with Strings
#! ------------------------------------------------------------

print(bool("Hello"))
print(bool("Python"))
print(bool(""))


#! ------------------------------------------------------------
#! Exercise 7 — bool() with Numbers
#! ------------------------------------------------------------

print(bool(10))
print(bool(100))
print(bool(0))
print(bool(-5))


#! ------------------------------------------------------------
#! Exercise 8 — bool() with Variables
#! ------------------------------------------------------------

name = "Mostafa"
age = 25
empty_name = ""

print(bool(name))
print(bool(age))
print(bool(empty_name))


#! ------------------------------------------------------------
#! Exercise 9 — Truthy Values
#! ------------------------------------------------------------

print(bool("abc"))
print(bool(123))
print(bool(["apple", "banana"]))


#! ------------------------------------------------------------
#! Exercise 10 — Falsy Values
#! ------------------------------------------------------------

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


#! ------------------------------------------------------------
#! Exercise 11 — Truthy or Falsy?
#! ------------------------------------------------------------

print(bool("Python"))
print(bool(""))
print(bool(0))
print(bool(1))
print(bool([]))
print(bool([1, 2, 3]))
print(bool({}))
print(bool(None))


#! ------------------------------------------------------------
#! Exercise 12 — Boolean with if
#! ------------------------------------------------------------

username = "Mostafa"

if bool(username):
    print("Username exists.")
else:
    print("Username is empty.")


#! ------------------------------------------------------------
#! Exercise 13 — Empty String
#! ------------------------------------------------------------

username = ""

if bool(username):
    print("Username exists.")
else:
    print("Username is empty.")


#! ------------------------------------------------------------
#! Exercise 14 — Function Returning Boolean
#! ------------------------------------------------------------

def is_python():
    return True


print(is_python())


#! ------------------------------------------------------------
#! Exercise 15 — Function with if
#! ------------------------------------------------------------

def is_logged_in():
    return True


if is_logged_in():
    print("User is logged in.")
else:
    print("User is not logged in.")


#! ------------------------------------------------------------
#! Exercise 16 — Change the Boolean
#! ------------------------------------------------------------

def is_admin():
    return False


if is_admin():
    print("User is an admin.")
else:
    print("User is not an admin.")


#! ------------------------------------------------------------
#! Exercise 17 — isinstance()
#! ------------------------------------------------------------

x = 200

print(isinstance(x, int))


#! ------------------------------------------------------------
#! Exercise 18 — Check Different Data Types
#! ------------------------------------------------------------

age = 25
name = "Mostafa"
price = 99.5

print(isinstance(age, int))
print(isinstance(name, str))
print(isinstance(price, float))


#! ------------------------------------------------------------
#! Exercise 19 — Boolean Decision
#! ------------------------------------------------------------

age = 22
has_id = True

if age >= 18:
    print("Age requirement passed.")
else:
    print("Age requirement failed.")


#! ------------------------------------------------------------
#! Exercise 20 — Boolean Variable
#! ------------------------------------------------------------

is_learning = True

if is_learning:
    print("Keep learning Python.")
else:
    print("You are not learning Python.")


#! ------------------------------------------------------------
#! Exercise 21 — Compare and Decide
#! ------------------------------------------------------------

password_length = 10

if password_length > 7:
    print("Password is long enough.")
else:
    print("Password is too short.")


#! ------------------------------------------------------------
#! Exercise 22 — bool() Challenge
#! ------------------------------------------------------------

value1 = "Python"
value2 = ""
value3 = 100
value4 = 0

print(bool(value1))
print(bool(value2))
print(bool(value3))
print(bool(value4))

if bool(value2):
    print("value2 contains a value.")
else:
    print("value2 is empty.")


#! ------------------------------------------------------------
#! Exercise 23 — Type + Boolean
#! ------------------------------------------------------------

x = 250

print(isinstance(x, int))
print(x > 100)


#! ------------------------------------------------------------
#! Exercise 24 — Mini Challenge
#! ------------------------------------------------------------

username = "Mostafa"
age = 25

if bool(username) and age >= 18:
    print("Access granted.")
else:
    print("Access denied.")


#! ------------------------------------------------------------
#! Exercise 25 — Final Challenge
#! ------------------------------------------------------------

name = "Mostafa"
age = 25
email = "mostafa@example.com"

name_exists = bool(name)
email_exists = bool(email)
age_is_integer = isinstance(age, int)
age_is_adult = age >= 18

if name_exists and email_exists and age_is_integer and age_is_adult:
    print("User information is valid.")
else:
    print("User information is invalid.")


# * ============================================================
# * End of Solutions
# * ============================================================