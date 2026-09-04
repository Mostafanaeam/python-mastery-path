while True:
    Number = input("Enter a number: ")
    if not Number.isdigit():
       print("Please enter a valid number.")
       continue
    break

Number = int(Number)

print("\n" + 33 * "=")
print("       NUMBER ANALYZER")
print( 33 * "=")
print(f"Number      : {Number}")
print(f"Type        : {type(Number)}")
print(f"Positive    : {Number > 0}")
print(f"Negative    : {Number < 0}")
print(f"Zero        : {Number == 0}")
print(f"Even        : {Number % 2 == 0}")
print(f"Odd         : {Number % 2 != 0}")
print(f"Square      : {Number ** 2}")
print(f"Cube        : {Number ** 3}")
print(f"Divisible by 3: {Number % 3 == 0}")
print(f"Divisible by 5: {Number % 5 == 0}")
print(f"Divisible by 10: {Number % 10 == 0}")
print( 33 * "=")
