# ? ============================================================
# ? Python Numbers — Solutions
# ? ============================================================


#! ------------------------------------------------------------
#! Exercise 1 — Identify Number Types
#! ------------------------------------------------------------

x = 25
y = 10.5
z = 3 + 5j

print(x, type(x))
print(y, type(y))
print(z, type(z))


#! ------------------------------------------------------------
#! Exercise 2 — Integer
#! ------------------------------------------------------------

positive_number = 100
negative_number = -50
large_number = 35656222554887711

print(positive_number, type(positive_number))
print(negative_number, type(negative_number))
print(large_number, type(large_number))


#! ------------------------------------------------------------
#! Exercise 3 — Float
#! ------------------------------------------------------------

positive_decimal = 10.5
decimal_with_zero = 20.0
negative_decimal = -35.59

print(positive_decimal, type(positive_decimal))
print(decimal_with_zero, type(decimal_with_zero))
print(negative_decimal, type(negative_decimal))


#! ------------------------------------------------------------
#! Exercise 4 — Complex Numbers
#! ------------------------------------------------------------

complex_number = 3 + 5j
imaginary_number = 5j
negative_imaginary_number = -5j

print(complex_number, type(complex_number))
print(imaginary_number, type(imaginary_number))
print(negative_imaginary_number, type(negative_imaginary_number))


#! ------------------------------------------------------------
#! Exercise 5 — Int to Float
#! ------------------------------------------------------------

x = 10

y = float(x)

print(x)
print(y)
print(type(y))


#! ------------------------------------------------------------
#! Exercise 6 — Float to Int
#! ------------------------------------------------------------

x = 15.8

y = int(x)

print(x)
print(y)
print(type(y))


#! ------------------------------------------------------------
#! Exercise 7 — Int to Complex
#! ------------------------------------------------------------

x = 7

y = complex(x)

print(x)
print(y)
print(type(y))


#! ------------------------------------------------------------
#! Exercise 8 — Convert Multiple Numbers
#! ------------------------------------------------------------

x = 10
y = 5.5

x_to_float = float(x)
y_to_int = int(y)
x_to_complex = complex(x)

print(x_to_float, type(x_to_float))
print(y_to_int, type(y_to_int))
print(x_to_complex, type(x_to_complex))


#! ------------------------------------------------------------
#! Exercise 9 — Random Number
#! ------------------------------------------------------------

import random

random_number = random.randrange(1, 10)

print(random_number)


#! ------------------------------------------------------------
#! Exercise 10 — Final Challenge
#! ------------------------------------------------------------

integer_number = 20
float_number = 10.5
complex_number = 3 + 2j

# 1. Print each number and its type

print(integer_number, type(integer_number))
print(float_number, type(float_number))
print(complex_number, type(complex_number))

# 2. Convert the integer to float

integer_to_float = float(integer_number)

# 3. Convert the float to int

float_to_int = int(float_number)

# 4. Convert the integer to complex

integer_to_complex = complex(integer_number)

# 5. Generate a random number between 1 and 100

random_number = random.randrange(1, 100)

print(integer_to_float, type(integer_to_float))
print(float_to_int, type(float_to_int))
print(integer_to_complex, type(integer_to_complex))
print(random_number, type(random_number))