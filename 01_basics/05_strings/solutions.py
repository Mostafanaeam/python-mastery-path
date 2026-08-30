# ? ============================================================
# ? Python Strings - Solutions
# ? ============================================================


#! ------------------------------------------------------------
#! Exercise 1 — Hello String
#! ------------------------------------------------------------

print("Hello, Python!")
print("I am learning Strings.")


#! ------------------------------------------------------------
#! Exercise 2 — Single vs Double Quotes
#! ------------------------------------------------------------

print("Python")
print('Python')

language = "Python"
print(language)


#! ------------------------------------------------------------
#! Exercise 3 — Quotes Inside Quotes
#! ------------------------------------------------------------

print("It's a beautiful day.")
print('He said "Hello".')
print("My teacher's name is \"John\".")


#! ------------------------------------------------------------
#! Exercise 4 — String Variable
#! ------------------------------------------------------------

name = "Mostafa"

print("My name is", name + ".")


#! ------------------------------------------------------------
#! Exercise 5 — Multiline String
#! ------------------------------------------------------------

languages = """Python
JavaScript
TypeScript
C++"""

print(languages)


#! ------------------------------------------------------------
#! Exercise 6 — String Indexing
#! ------------------------------------------------------------

word = "Python"

print(word[0])
print(word[1])
print(word[-1])


#! ------------------------------------------------------------
#! Exercise 7 — Find Characters
#! ------------------------------------------------------------

text = "Programming"

print(text[0])
print(text[3])
print(text[5])
print(text[9])


#! ------------------------------------------------------------
#! Exercise 8 — Loop Through a String
#! ------------------------------------------------------------

word = "Python"

for character in word:
    print(character)


#! ------------------------------------------------------------
#! Exercise 9 — String Length
#! ------------------------------------------------------------

language = "Python"
name = "Mostafa"

print(len(language))
print(len(name))


#! ------------------------------------------------------------
#! Exercise 10 — Check String
#! ------------------------------------------------------------

sentence = "Python is easy to learn"

print("Python" in sentence)
print("easy" in sentence)
print("Java" in sentence)


#! ------------------------------------------------------------
#! Exercise 11 — Check if NOT
#! ------------------------------------------------------------

sentence = "Python is powerful"

print("JavaScript" not in sentence)


#! ------------------------------------------------------------
#! Exercise 12 — String Check with if
#! ------------------------------------------------------------

message = "Python is easy to learn"

if "easy" in message:
    print("The word 'easy' is present.")


#! ------------------------------------------------------------
#! Exercise 13 — Basic Slicing
#! ------------------------------------------------------------

text = "Hello, World!"

print(text[0:5])
print(text[2:7])
print(text[7:12])


#! ------------------------------------------------------------
#! Exercise 14 — Slice From the Start
#! ------------------------------------------------------------

text = "Programming"

print(text[:5])


#! ------------------------------------------------------------
#! Exercise 15 — Slice To the End
#! ------------------------------------------------------------

text = "Programming"

print(text[6:])


#! ------------------------------------------------------------
#! Exercise 16 — Negative Indexing
#! ------------------------------------------------------------

text = "Python"

print(text[-1])
print(text[-2])
print(text[-3:])


#! ------------------------------------------------------------
#! Exercise 17 — Upper and Lower Case
#! ------------------------------------------------------------

text = "Python Programming"

print(text.upper())
print(text.lower())


#! ------------------------------------------------------------
#! Exercise 18 — Remove Whitespace
#! ------------------------------------------------------------

username = "   Mostafa   "

print(username.strip())


#! ------------------------------------------------------------
#! Exercise 19 — Replace String
#! ------------------------------------------------------------

message = "I like JavaScript"

print(message.replace("JavaScript", "Python"))


#! ------------------------------------------------------------
#! Exercise 20 — Split String
#! ------------------------------------------------------------

languages = "Python,JavaScript,TypeScript,Java"

print(languages.split(","))


#! ------------------------------------------------------------
#! Exercise 21 — String Concatenation
#! ------------------------------------------------------------

first_name = "Mostafa"
last_name = "Naeam"

full_name = first_name + " " + last_name

print(full_name)


#! ------------------------------------------------------------
#! Exercise 22 — Build a Sentence
#! ------------------------------------------------------------

name = "Mostafa"
language = "Python"
level = "beginner"

sentence = (
    "My name is "
    + name
    + " and I am a "
    + level
    + " in "
    + language
    + "."
)

print(sentence)


#! ------------------------------------------------------------
#! Exercise 23 — F-String
#! ------------------------------------------------------------

name = "Mostafa"
age = 25

print(f"My name is {name} and I am {age} years old.")


#! ------------------------------------------------------------
#! Exercise 24 — F-String with Price
#! ------------------------------------------------------------

product = "Laptop"
price = 25000

print(f"The {product} costs {price} EGP.")


#! ------------------------------------------------------------
#! Exercise 25 — F-String Formatting
#! ------------------------------------------------------------

price = 59

print(f"{price:.2f}")


#! ------------------------------------------------------------
#! Exercise 26 — Expression Inside F-String
#! ------------------------------------------------------------

price = 59
quantity = 3

print(f"Total price: {price * quantity}")


#! ------------------------------------------------------------
#! Exercise 27 — Escape Character
#! ------------------------------------------------------------

print("He said \"Python is easy\".")


#! ------------------------------------------------------------
#! Exercise 28 — String Information
#! ------------------------------------------------------------

language = "Python Programming"

print(language)
print(len(language))
print(language.upper())
print(language.lower())
print(language[0])
print(language[-1])


#! ------------------------------------------------------------
#! Exercise 29 — Mini Challenge
#! ------------------------------------------------------------

name = "Mostafa"
age = 25
country = "Egypt"
programming_language = "Python"

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Country: {country}")
print(f"Learning: {programming_language}")


#! ------------------------------------------------------------
#! Exercise 30 — Final Challenge
#! ------------------------------------------------------------

sentence = "Python is easy to learn and Python is powerful"

# 1. Original sentence
print(sentence)

# 2. Length
print(len(sentence))

# 3. Check whether "Python" exists
print("Python" in sentence)

# 4. Check whether "Java" does NOT exist
print("Java" not in sentence)

# 5. Uppercase
print(sentence.upper())

# 6. Lowercase
print(sentence.lower())

# 7. Replace "powerful" with "awesome"
print(sentence.replace("powerful", "awesome"))

# 8. First 6 characters
print(sentence[:6])

# 9. Last 8 characters
print(sentence[-8:])


# * ============================================================
# * End of Solutions
# * ============================================================