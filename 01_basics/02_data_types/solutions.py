# ? ============================================================
# ? Python Data Types
# ? ============================================================

#! ------------------------------------------------------------
#! Exercise 1 — String
#! ------------------------------------------------------------

name = "mostafa"
print(type(name))

#! ------------------------------------------------------------
#! Exercise 2 — Integer
#! ------------------------------------------------------------
age = 20

print(age)
print(type(age))


#! ------------------------------------------------------------
#! Exercise 3 — Float
#! ------------------------------------------------------------
height = 174.5

print(height)
print(type(height))


#! ------------------------------------------------------------
#! Exercise 4 — Complex
#! ------------------------------------------------------------
z = 3 + 2j

print(z)
print(type(z))


#! ------------------------------------------------------------
#! Exercise 5 — List
#! ------------------------------------------------------------
fruits = ["apple", "banana", "cherry"]

print(fruits)
print(type(fruits))


#! ------------------------------------------------------------
#! Exercise 6 — Tuple
#! ------------------------------------------------------------
colors = ("red", "green", "blue")

print(colors)
print(type(colors))



#! ------------------------------------------------------------
#! Exercise 7 — Range
#! ------------------------------------------------------------
numbers = range(6)

print(numbers)
print(type(numbers))


#! ------------------------------------------------------------
#! Exercise 8 — Dictionary
#! ------------------------------------------------------------
student = {
    "name": "Mostafa",
    "age": 20
}

print(student)
print(type(student))


#! ------------------------------------------------------------
#! Exercise 9 — Set
#! ------------------------------------------------------------
fruits = {"apple", "banana", "cherry"}

print(fruits)
print(type(fruits))



#! ------------------------------------------------------------
#! Exercise 10 — Frozenset
#! ------------------------------------------------------------
fruits = frozenset({"apple", "banana", "cherry"})

print(fruits)
print(type(fruits))


#! ------------------------------------------------------------
#! Exercise 11 — Boolean
#! ------------------------------------------------------------
is_student = True
is_working = False

print(is_student)
print(type(is_student))

print(is_working)
print(type(is_working))


#! ------------------------------------------------------------
#! Exercise 12 — Bytes
#! ------------------------------------------------------------
data = b"Hello"

print(data)
print(type(data))


#! ------------------------------------------------------------
#! Exercise 13 — Bytearray
#! ------------------------------------------------------------
data = bytearray(5)

print(data)
print(type(data))


#! ------------------------------------------------------------
#! Exercise 14 — Memoryview
#! ------------------------------------------------------------
data = memoryview(bytes(5))

print(data)
print(type(data))


#! ------------------------------------------------------------
#! Exercise 15 — None
#! ------------------------------------------------------------
result = None

print(result)
print(type(result))


#! ------------------------------------------------------------
#! Exercise 16 — Identify the Data Types
#! ------------------------------------------------------------
print(type("Python"))
print(type(100))
print(type(10.5))
print(type(2j))
print(type(["Python", "JavaScript"]))
print(type(("Python", "JavaScript")))
print(type(range(5)))
print(type({"name": "Mostafa"}))
print(type({"Python", "JavaScript"}))
print(type(True))
print(type(None))


#! ------------------------------------------------------------
#! Exercise 17 — Create Different Data Types
#! ------------------------------------------------------------
string_value = "Python"
integer_value = 100
float_value = 10.5
complex_value = 2j
list_value = ["Python", "JavaScript"]
tuple_value = ("Python", "JavaScript")
range_value = range(5)
dictionary_value = {"name": "Mostafa"}
set_value = {"Python", "JavaScript"}
frozenset_value = frozenset({"Python", "JavaScript"})
boolean_value = True
bytes_value = b"Hello"
bytearray_value = bytearray(5)
memoryview_value = memoryview(bytes(5))
none_value = None

print(string_value, type(string_value))
print(integer_value, type(integer_value))
print(float_value, type(float_value))
print(complex_value, type(complex_value))
print(list_value, type(list_value))
print(tuple_value, type(tuple_value))
print(range_value, type(range_value))
print(dictionary_value, type(dictionary_value))
print(set_value, type(set_value))
print(frozenset_value, type(frozenset_value))
print(boolean_value, type(boolean_value))
print(bytes_value, type(bytes_value))
print(bytearray_value, type(bytearray_value))
print(memoryview_value, type(memoryview_value))
print(none_value, type(none_value))


#! ------------------------------------------------------------
#! Exercise 18 — Data Types Challenge
#! ------------------------------------------------------------
name = "Mostafa"
age = 20
height = 174.5
is_student = True
favorite_fruits = ["apple", "banana", "cherry"]
coordinates = (10, 20)
skills = {"Python", "JavaScript", "Angular"}

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))
print(favorite_fruits, type(favorite_fruits))
print(coordinates, type(coordinates))
print(skills, type(skills))

#! ------------------------------------------------------------
#! Exercise 19 — Type Identification Challenge
#! ------------------------------------------------------------
value_one = 25
value_two = "25"
value_three = 25.0
value_four = True
value_five = None

print(value_one, type(value_one))
print(value_two, type(value_two))
print(value_three, type(value_three))
print(value_four, type(value_four))
print(value_five, type(value_five))

#! ------------------------------------------------------------
#! Exercise 20 — Final Challenge
#! ------------------------------------------------------------
student_name = "Mostafa"
student_age = 20
student_height = 174.5
is_student = True
favorite_fruits = ["apple", "banana", "cherry"]
programming_languages = {"Python", "JavaScript", "TypeScript"}
number_range = range(5)
student_information = {
    "name": student_name,
    "age": student_age
}

print(student_name, type(student_name))
print(student_age, type(student_age))
print(student_height, type(student_height))
print(is_student, type(is_student))
print(favorite_fruits, type(favorite_fruits))
print(programming_languages, type(programming_languages))
print(number_range, type(number_range))
print(student_information, type(student_information))