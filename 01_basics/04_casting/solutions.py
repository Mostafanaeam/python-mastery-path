# ? ============================================================
# ? Python Casting
# ? ============================================================

#! ------------------------------------------------------------
#! Exercise 1 — Convert to Integer
#! ------------------------------------------------------------

value_one = int(10.8)
value_two = int("25")
value_three = int(50)

print(value_one, type(value_one))
print(value_two, type(value_two))
print(value_three, type(value_three))


#! ------------------------------------------------------------
#! Exercise 2 — Convert to Float
#! ------------------------------------------------------------

value_one = float(10)
value_two = float("25")
value_three = float("4.2")

print(value_one, type(value_one))
print(value_two, type(value_two))
print(value_three, type(value_three))


#! ------------------------------------------------------------
#! Exercise 3 — Convert to String
#! ------------------------------------------------------------

value_one = str(10)
value_two = str(25.5)
value_three = str("Python")

print(value_one, type(value_one))
print(value_two, type(value_two))
print(value_three, type(value_three))


#! ------------------------------------------------------------
#! Exercise 4 — Casting Challenge
#! ------------------------------------------------------------

x = "100"
y = 20.5
z = 50

x = int(x)
y = int(y)
z_to_float = float(z)
z_to_string = str(z)

print(x, type(x))
print(y, type(y))
print(z_to_float, type(z_to_float))
print(z_to_string, type(z_to_string))