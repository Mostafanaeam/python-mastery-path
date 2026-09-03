import datetime

# name = input("Enter your name: ")

while True:
    name = input("Enter your name: ")
    if not name.strip():
       print("Please enter a valid name.")
       continue
    isvalid = all(char.isalpha() or char == " " for char in name)
    if not isvalid:
       print("Please enter a valid name.")
       #  break
    else:
       name = name.title()
       break

birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().month
current_day = datetime.datetime.now().day

age = current_year - birth_year
if current_month < birth_month or (current_month == birth_month and current_day < birth_day):
    age -= 1


country = input("Enter your country: ").title()
job = input("Enter your job: ").title()
height = int(input("Enter your height in cm: "))
weight = int(input("Enter your weight in kg: "))


print("\n" + 33 * "=")
print("       PERSONAL PROFILE")
print( 33 * "=")
print(f"Name       : {name}")
print(f"Age        : {age}")
print(f"Country    : {country}")
print(f"Job        : {job}")
print(f"Height     : {height} cm")
print(f"Weight     : {weight} kg")
print("\n" + 33 * "=" + "\n")

