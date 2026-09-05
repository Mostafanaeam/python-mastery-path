

print("\n" + 33 * "=")
print("       PASSWORD STRENGTH CHECKER")
print( 33 * "=")

print("""
     \nWelcome to the Password Strength Checker!
     
     This program will analyze your password and determine its strength based on the following criteria:
     1. Length: Password must be at least 8 characters long.
     2. Uppercase letters: Password must contain at least one uppercase letter.
     3. Lowercase letters: Password must contain at least one lowercase letter.
     4. Numbers: Password must contain at least one number.
     5. Special characters: Password must contain at least one special character.
     """)
while True:
     password = input("Enter your password: ")

     if len(password) < 8:
         print("Strength: WEAK")
         print("Problems:")
         print("- Password must contain at least 8 characters")
         continue
     elif not any(char.isupper() for char in password):
         print("Strength: WEAK")
         print("Problems:")
         print("- Password must contain at least one uppercase letter")
         continue
     elif not any(char.islower() for char in password):
         print("Strength: WEAK")
         print("Problems:")
         print("- Password must contain at least one lowercase letter")
         continue
     elif not any(char.isdigit() for char in password):
         print("Strength: WEAK")
         print("Problems:")
         print("- Password must contain at least one number")
         continue
     elif not any(char in "!@#$%^&*()-+" for char in password):
         print("Strength: WEAK")
         print("Problems:")
         print("- Password must contain at least one special character")
         continue
     else:
         print("Strength: STRONG")
         print("Length            :", len(password))
         print("Uppercase         :", any(char.isupper() for char in password))
         print("Lowercase         :", any(char.islower() for char in password))
         print("Numbers           :", any(char.isdigit() for char in password))
         print("Special Characters:", any(char in "!@#$%^&*()-+" for char in password))
     continue_choice = input("Do you want to test another password? (yes/no): ")
     if continue_choice.lower() != "yes":
          print("thank you for using the Password Strength Checker. Goodbye!")
          break