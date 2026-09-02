# ? ============================================================
# ? Python Lists - Exercises Solutions
# ? ============================================================


# ? ============================================================
# ? 01 - Create Lists
# ? ============================================================


#! ------------------------------------------------------------
#! Exercise 1 — Create a List
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry"]

print(fruits)


#! ------------------------------------------------------------
#! Exercise 2 — Different Data Types
#! ------------------------------------------------------------

my_list = ["Mostafa", 25, True, 85.5]

print(my_list)


#! ------------------------------------------------------------
#! Exercise 3 — Duplicate Values
#! ------------------------------------------------------------

numbers = [1, 2, 3, 2, 4, 2, 5]

print(numbers)


#! ------------------------------------------------------------
#! Exercise 4 — Find List Length
#! ------------------------------------------------------------

languages = ["Python", "JavaScript", "TypeScript", "C++"]

print(len(languages))


#! ------------------------------------------------------------
#! Exercise 5 — Check List Type
#! ------------------------------------------------------------

my_list = ["Python", "JavaScript", "C++"]

print(type(my_list))


#! ------------------------------------------------------------
#! Exercise 6 — Create List Using list()
#! ------------------------------------------------------------

fruits = list(("apple", "banana", "cherry"))

print(fruits)


# ? ============================================================
# ? 02 - Access List Items
# ? ============================================================


#! ------------------------------------------------------------
#! Exercise 7 — Access First, Second and Third Items
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry", "orange"]

print(fruits[0])
print(fruits[1])
print(fruits[2])


#! ------------------------------------------------------------
#! Exercise 8 — Predict the Index
#! ------------------------------------------------------------

languages = ["Python", "JavaScript", "TypeScript", "C++"]

print(languages[0])
print(languages[2])
print(languages[3])


#! ------------------------------------------------------------
#! Exercise 9 — Negative Indexing
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry", "orange"]

print(fruits[-1])
print(fruits[-2])


#! ------------------------------------------------------------
#! Exercise 10 — Slicing
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry", "orange", "mango"]

print(fruits[1:4])


#! ------------------------------------------------------------
#! Exercise 11 — First Three Items
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry", "orange", "mango"]

print(fruits[:3])


#! ------------------------------------------------------------
#! Exercise 12 — From Index 2 to the End
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry", "orange", "mango"]

print(fruits[2:])


#! ------------------------------------------------------------
#! Exercise 13 — Last Three Items
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry", "orange", "mango"]

print(fruits[-3:])


#! ------------------------------------------------------------
#! Exercise 14 — Check Membership
#! ------------------------------------------------------------

languages = ["Python", "JavaScript", "TypeScript"]

if "Python" in languages:
    print("Python is in the list")


#! ------------------------------------------------------------
#! Exercise 15 — Membership Results
#! ------------------------------------------------------------

languages = ["Python", "JavaScript", "TypeScript"]

print("Python" in languages)
print("Java" in languages)


# ? ============================================================
# ? 03 - Change List Items
# ? ============================================================


#! ------------------------------------------------------------
#! Exercise 16 — Change an Item
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry"]

fruits[1] = "orange"

print(fruits)


#! ------------------------------------------------------------
#! Exercise 17 — Change Multiple Items
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry", "orange"]

fruits[1:3] = ["mango", "kiwi"]

print(fruits)


#! ------------------------------------------------------------
#! Exercise 18 — Replace One Item with Two Items
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry"]

fruits[1:2] = ["mango", "kiwi"]

print(fruits)


#! ------------------------------------------------------------
#! Exercise 19 — Insert an Item
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry"]

fruits.insert(1, "orange")

print(fruits)


# ? ============================================================
# ? 04 - Add List Items
# ? ============================================================


#! ------------------------------------------------------------
#! Exercise 20 — Append
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry"]

fruits.append("orange")

print(fruits)


#! ------------------------------------------------------------
#! Exercise 21 — Insert
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry"]

fruits.insert(1, "orange")

print(fruits)


#! ------------------------------------------------------------
#! Exercise 22 — Extend a List
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry"]

tropical = ["mango", "pineapple", "papaya"]

fruits.extend(tropical)

print(fruits)


#! ------------------------------------------------------------
#! Exercise 23 — Extend Using a Tuple
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry"]

tropical = ("mango", "pineapple", "papaya")

fruits.extend(tropical)

print(fruits)


#! ------------------------------------------------------------
#! Exercise 24 — append() vs extend()
#! ------------------------------------------------------------

fruits1 = ["apple", "banana"]
tropical = ["mango", "pineapple"]

fruits1.append(tropical)

print(fruits1)


fruits2 = ["apple", "banana"]

fruits2.extend(tropical)

print(fruits2)


# ? ============================================================
# ? 05 - Remove List Items
# ? ============================================================


#! ------------------------------------------------------------
#! Exercise 25 — Remove an Item
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry"]

fruits.remove("banana")

print(fruits)


#! ------------------------------------------------------------
#! Exercise 26 — Remove First Occurrence
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry", "banana"]

fruits.remove("banana")

print(fruits)


#! ------------------------------------------------------------
#! Exercise 27 — Pop by Index
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry"]

fruits.pop(1)

print(fruits)


#! ------------------------------------------------------------
#! Exercise 28 — Pop Last Item
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry"]

fruits.pop()

print(fruits)


#! ------------------------------------------------------------
#! Exercise 29 — Delete First Item
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry"]

del fruits[0]

print(fruits)


#! ------------------------------------------------------------
#! Exercise 30 — Clear the List
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry"]

fruits.clear()

print(fruits)


# ? ============================================================
# ? 06 - Loop Lists
# ? ============================================================


#! ------------------------------------------------------------
#! Exercise 31 — for Loop
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


#! ------------------------------------------------------------
#! Exercise 32 — Loop Using Indexes
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry"]

for i in range(len(fruits)):
    print(fruits[i])


#! ------------------------------------------------------------
#! Exercise 33 — while Loop
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry"]

i = 0

while i < len(fruits):
    print(fruits[i])
    i += 1


#! ------------------------------------------------------------
#! Exercise 34 — Print Index and Value
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry"]

for i in range(len(fruits)):
    print(i, fruits[i])


#! ------------------------------------------------------------
#! Exercise 35 — List Comprehension Printing
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry"]

[print(fruit) for fruit in fruits]


# ? ============================================================
# ? 07 - List Comprehension
# ? ============================================================


#! ------------------------------------------------------------
#! Exercise 36 — Fruits Containing "a"
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry", "orange", "kiwi"]

new_list = [fruit for fruit in fruits if "a" in fruit]

print(new_list)


#! ------------------------------------------------------------
#! Exercise 37 — Words Longer Than 5 Characters
#! ------------------------------------------------------------

words = ["Python", "Java", "JavaScript", "HTML", "Developer"]

new_list = [word for word in words if len(word) > 5]

print(new_list)


#! ------------------------------------------------------------
#! Exercise 38 — Numbers Greater Than 5
#! ------------------------------------------------------------

numbers = [1, 3, 5, 7, 9, 10]

new_list = [number for number in numbers if number > 5]

print(new_list)


#! ------------------------------------------------------------
#! Exercise 39 — Square Numbers
#! ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)


#! ------------------------------------------------------------
#! Exercise 40 — Even Numbers
#! ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)


# ? ============================================================
# ? 08 - Sort Lists
# ? ============================================================


#! ------------------------------------------------------------
#! Exercise 41 — Sort Strings
#! ------------------------------------------------------------

fruits = ["orange", "apple", "banana", "cherry"]

fruits.sort()

print(fruits)


#! ------------------------------------------------------------
#! Exercise 42 — Sort Numbers Ascending
#! ------------------------------------------------------------

numbers = [100, 50, 25, 75, 10]

numbers.sort()

print(numbers)


#! ------------------------------------------------------------
#! Exercise 43 — Sort Numbers Descending
#! ------------------------------------------------------------

numbers = [100, 50, 25, 75, 10]

numbers.sort(reverse=True)

print(numbers)


#! ------------------------------------------------------------
#! Exercise 44 — Case-Insensitive Sorting
#! ------------------------------------------------------------

fruits = ["banana", "Orange", "apple", "Cherry"]

fruits.sort(key=str.lower)

print(fruits)


#! ------------------------------------------------------------
#! Exercise 45 — Reverse a List
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry"]

fruits.reverse()

print(fruits)


#! ------------------------------------------------------------
#! Exercise 46 — Custom Sort
#! ------------------------------------------------------------

numbers = [10, 30, 45, 50, 70, 90]

numbers.sort(key=lambda number: abs(number - 50))

print(numbers)


# ? ============================================================
# ? 09 - Copy Lists
# ? ============================================================


#! ------------------------------------------------------------
#! Exercise 47 — copy()
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry"]

new_fruits = fruits.copy()

print(new_fruits)


#! ------------------------------------------------------------
#! Exercise 48 — list()
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry"]

new_fruits = list(fruits)

print(new_fruits)


#! ------------------------------------------------------------
#! Exercise 49 — Copy Using Slicing
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry"]

new_fruits = fruits[:]

print(new_fruits)


#! ------------------------------------------------------------
#! Exercise 50 — Copy Challenge
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry"]

new_fruits = fruits.copy()

new_fruits.append("orange")

print("Original:", fruits)
print("Copy:", new_fruits)


# ? ============================================================
# ? 10 - Join Lists
# ? ============================================================


#! ------------------------------------------------------------
#! Exercise 51 — Join Using +
#! ------------------------------------------------------------

frontend = ["HTML", "CSS", "JavaScript"]

backend = ["Python", "Node.js"]

skills = frontend + backend

print(skills)


#! ------------------------------------------------------------
#! Exercise 52 — Join Using Loop + append()
#! ------------------------------------------------------------

frontend = ["HTML", "CSS", "JavaScript"]

backend = ["Python", "Node.js"]

skills = frontend.copy()

for skill in backend:
    skills.append(skill)

print(skills)


#! ------------------------------------------------------------
#! Exercise 53 — Join Using extend()
#! ------------------------------------------------------------

frontend = ["HTML", "CSS", "JavaScript"]

backend = ["Python", "Node.js"]

skills = frontend.copy()

skills.extend(backend)

print(skills)


# ? ============================================================
# ? 11 - Combined Practice
# ? ============================================================


#! ------------------------------------------------------------
#! Exercise 54 — Fruit Manager
#! ------------------------------------------------------------

fruits = ["apple", "banana", "cherry"]

fruits.append("orange")
fruits.append("mango")

fruits.remove("banana")

fruits[0] = "kiwi"

print(fruits)


#! ------------------------------------------------------------
#! Exercise 55 — Programming Languages
#! ------------------------------------------------------------

languages = ["Python", "JavaScript", "TypeScript", "C++"]

print(languages[0])

print("Python" in languages)

languages.append("Java")

languages.remove("C++")

print(languages)


#! ------------------------------------------------------------
#! Exercise 56 — Student Scores
#! ------------------------------------------------------------

scores = [85, 70, 95, 60, 90]

print(scores)

print(scores[0])

print(scores[-1])

scores.sort()

print("Ascending:", scores)

scores.sort(reverse=True)

print("Descending:", scores)


#! ------------------------------------------------------------
#! Exercise 57 — Passing Scores
#! ------------------------------------------------------------

scores = [35, 80, 45, 90, 60, 30, 75]

passing_scores = [score for score in scores if score >= 50]

print(passing_scores)


#! ------------------------------------------------------------
#! Exercise 58 — Shopping List
#! ------------------------------------------------------------

shopping = ["milk", "bread", "eggs"]

shopping.append("cheese")

shopping.remove("bread")

print("milk" in shopping)

print(shopping)


#! ------------------------------------------------------------
#! Exercise 59 — Frontend + Backend
#! ------------------------------------------------------------

frontend = ["HTML", "CSS", "JavaScript", "React"]

backend = ["Python", "Node.js", "Express"]

skills = frontend + backend

skills.sort()

print("All Skills:", skills)

print("Python" in skills)

print("First 3:", skills[:3])


#! ------------------------------------------------------------
#! Exercise 60 — Programming Skills Manager
#! ------------------------------------------------------------

skills = [
    "HTML",
    "CSS",
    "JavaScript",
    "Python",
    "Git"
]

# ? List Length
print("Length:", len(skills))


# ? First Item
print("First:", skills[0])


# ? Last Item
print("Last:", skills[-1])


# ? Membership
print("Python" in skills)


# ? Add TypeScript
skills.append("TypeScript")


# ? Remove CSS
skills.remove("CSS")


# ? Replace Git with GitHub
skills[skills.index("Git")] = "GitHub"


# ? Skills Containing "t"
skills_with_t = [skill for skill in skills if "t" in skill.lower()]

print("Skills containing 't':", skills_with_t)


# ? Sort Skills
skills.sort()

print("Sorted Skills:", skills)


# ? Copy Skills
skills_copy = skills.copy()


# ? Modify Copy
skills_copy.append("React")


# ? Print Both
print("Original:", skills)
print("Copy:", skills_copy)