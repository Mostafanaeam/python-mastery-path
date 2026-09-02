# ? ============================================================
# ? Python Lists - Exercises
# ? ============================================================
#
# Instructions:
# - Try to solve each exercise yourself.
# - Do not look at the solution before trying.
# - Run your code after every exercise.
# - Predict the output before running the code when possible.
# - If you get an error, try to understand it first.
# - Use only the concepts you have learned so far.
# ============================================================


#! ============================================================
#! Section 01 — Create Lists
#! ============================================================


#! ------------------------------------------------------------
#! Exercise 1 — Create a List
#! ------------------------------------------------------------
# Create a list called `fruits` containing:
#
# apple
# banana
# cherry
#
# Print the list.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 2 — Different Data Types
#! ------------------------------------------------------------
# Create a list containing:
#
# "Mostafa"
# 25
# True
# 85.5
#
# Print the list.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 3 — Duplicate Values
#! ------------------------------------------------------------
# Create a list containing:
#
# apple
# banana
# apple
# cherry
# banana
#
# Print the list.
#
# Observe that lists allow duplicate values.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 4 — List Length
#! ------------------------------------------------------------
# Create:
#
# languages = ["Python", "JavaScript", "TypeScript", "C++"]
#
# Print the number of items in the list.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 5 — Check List Type
#! ------------------------------------------------------------
# Create:
#
# mylist = ["Python", "JavaScript", "C++"]
#
# Print the type of `mylist`.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 6 — Create List Using list()
#! ------------------------------------------------------------
# Use the list() constructor to create a list containing:
#
# "apple"
# "banana"
# "cherry"
#
# Print the list.
#
# ------------------------------------------------------------


#! ============================================================
#! Section 02 — Access List Items
#! ============================================================


#! ------------------------------------------------------------
#! Exercise 7 — Access by Index
#! ------------------------------------------------------------
# Given:
#
# fruits = ["apple", "banana", "cherry"]
#
# Print:
#
# 1. The first item
# 2. The second item
# 3. The third item
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 8 — Predict the Index
#! ------------------------------------------------------------
# Given:
#
# languages = ["Python", "JavaScript", "TypeScript", "C++"]
#
# Without running the code, predict:
#
# print(languages[0])
# print(languages[2])
# print(languages[3])
#
# Then run it.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 9 — Negative Indexing
#! ------------------------------------------------------------
# Given:
#
# fruits = ["apple", "banana", "cherry", "orange"]
#
# Print:
#
# 1. The last item
# 2. The second-to-last item
#
# Use negative indexing.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 10 — Range of Indexes
#! ------------------------------------------------------------
# Given:
#
# fruits = [
#     "apple",
#     "banana",
#     "cherry",
#     "orange",
#     "kiwi",
#     "mango"
# ]
#
# Print:
#
# 1. Items from index 1 to 3
# 2. Items from index 2 to 5
#
# Use slicing.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 11 — Slice From the Start
#! ------------------------------------------------------------
# Given:
#
# numbers = [10, 20, 30, 40, 50]
#
# Print the first three items using slicing.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 12 — Slice To the End
#! ------------------------------------------------------------
# Given:
#
# numbers = [10, 20, 30, 40, 50]
#
# Print everything starting from index 2.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 13 — Negative Slicing
#! ------------------------------------------------------------
# Given:
#
# fruits = [
#     "apple",
#     "banana",
#     "cherry",
#     "orange",
#     "kiwi"
# ]
#
# Print the last three items using negative slicing.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 14 — Check if Item Exists
#! ------------------------------------------------------------
# Given:
#
# fruits = ["apple", "banana", "cherry"]
#
# Check whether "banana" exists in the list.
#
# If it exists, print:
#
# Banana exists.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 15 — Membership Challenge
#! ------------------------------------------------------------
# Given:
#
# languages = ["Python", "JavaScript", "C++"]
#
# Check whether:
#
# "Python" exists.
# "Java" exists.
#
# Print both results.
#
# ------------------------------------------------------------


#! ============================================================
#! Section 03 — Change List Items
#! ============================================================


#! ------------------------------------------------------------
#! Exercise 16 — Change One Item
#! ------------------------------------------------------------
# Given:
#
# fruits = ["apple", "banana", "cherry"]
#
# Change "banana" to "orange".
#
# Print the list.
#
# Expected:
#
# ["apple", "orange", "cherry"]
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 17 — Change Multiple Items
#! ------------------------------------------------------------
# Given:
#
# fruits = [
#     "apple",
#     "banana",
#     "cherry",
#     "orange"
# ]
#
# Change "banana" and "cherry" to:
#
# "mango"
# "kiwi"
#
# Use range assignment.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 18 — Replace One Item with Two
#! ------------------------------------------------------------
# Given:
#
# fruits = ["apple", "banana", "cherry"]
#
# Replace "banana" with:
#
# "orange"
# "mango"
#
# Print the result.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 19 — Insert an Item
#! ------------------------------------------------------------
# Given:
#
# fruits = ["apple", "banana", "cherry"]
#
# Insert "orange" at index 1.
#
# Expected:
#
# ["apple", "orange", "banana", "cherry"]
#
# ------------------------------------------------------------


#! ============================================================
#! Section 04 — Add List Items
#! ============================================================


#! ------------------------------------------------------------
#! Exercise 20 — append()
#! ------------------------------------------------------------
# Given:
#
# fruits = ["apple", "banana", "cherry"]
#
# Add "orange" to the end of the list using append().
#
# Print the list.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 21 — insert()
#! ------------------------------------------------------------
# Given:
#
# fruits = ["apple", "banana", "cherry"]
#
# Insert "orange" at index 1.
#
# Print the list.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 22 — extend()
#! ------------------------------------------------------------
# Given:
#
# fruits = ["apple", "banana", "cherry"]
#
# tropical = ["mango", "pineapple", "papaya"]
#
# Add all items from `tropical` to `fruits`.
#
# Use extend().
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 23 — Extend with a Tuple
#! ------------------------------------------------------------
# Given:
#
# fruits = ["apple", "banana"]
#
# more_fruits = ("orange", "kiwi")
#
# Add the tuple items to the list using extend().
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 24 — append vs extend
#! ------------------------------------------------------------
# Create:
#
# fruits = ["apple", "banana"]
#
# Then create another list:
#
# tropical = ["mango", "kiwi"]
#
# First use append(tropical).
#
# Print the result.
#
# Then create the lists again and use extend(tropical).
#
# Print the result.
#
# Observe the difference.
#
# ------------------------------------------------------------


#! ============================================================
#! Section 05 — Remove List Items
#! ============================================================


#! ------------------------------------------------------------
#! Exercise 25 — remove()
#! ------------------------------------------------------------
# Given:
#
# fruits = ["apple", "banana", "cherry"]
#
# Remove "banana".
#
# Print the list.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 26 — Remove First Occurrence
#! ------------------------------------------------------------
# Given:
#
# fruits = [
#     "apple",
#     "banana",
#     "cherry",
#     "banana",
#     "kiwi"
# ]
#
# Use remove() to remove "banana".
#
# Print the result.
#
# Observe which "banana" was removed.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 27 — pop(index)
#! ------------------------------------------------------------
# Given:
#
# fruits = ["apple", "banana", "cherry"]
#
# Remove the item at index 1 using pop().
#
# Print the list.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 28 — pop()
#! ------------------------------------------------------------
# Given:
#
# fruits = ["apple", "banana", "cherry"]
#
# Use pop() without an index.
#
# Print the list.
#
# Which item was removed?
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 29 — del
#! ------------------------------------------------------------
# Given:
#
# fruits = ["apple", "banana", "cherry"]
#
# Delete the first item using del.
#
# Print the list.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 30 — clear()
#! ------------------------------------------------------------
# Given:
#
# fruits = ["apple", "banana", "cherry"]
#
# Remove all items from the list using clear().
#
# Print the list.
#
# ------------------------------------------------------------


#! ============================================================
#! Section 06 — Loop Lists
#! ============================================================


#! ------------------------------------------------------------
#! Exercise 31 — Basic for Loop
#! ------------------------------------------------------------
# Given:
#
# fruits = ["apple", "banana", "cherry"]
#
# Use a for loop to print every fruit on a separate line.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 32 — Loop Through Indexes
#! ------------------------------------------------------------
# Given:
#
# languages = ["Python", "JavaScript", "C++"]
#
# Use:
#
# range()
# len()
#
# to print every item using its index.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 33 — while Loop
#! ------------------------------------------------------------
# Given:
#
# numbers = [10, 20, 30, 40, 50]
#
# Use a while loop to print every item.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 34 — Print Index and Value
#! ------------------------------------------------------------
# Given:
#
# fruits = ["apple", "banana", "cherry"]
#
# Use a loop to print:
#
# apple
# banana
# cherry
#
# Then modify your program so that it prints the index
# before each item.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 35 — List Comprehension Printing
#! ------------------------------------------------------------
# Given:
#
# fruits = ["apple", "banana", "cherry"]
#
# Use list comprehension to print every item.
#
# ------------------------------------------------------------


#! ============================================================
#! Section 07 — List Comprehension
#! ============================================================


#! ------------------------------------------------------------
#! Exercise 36 — Create a New List
#! ------------------------------------------------------------
# Given:
#
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#
# Create a new list containing only fruits that contain
# the letter "a".
#
# Use list comprehension.
#
# Expected:
#
# ["apple", "banana", "mango"]
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 37 — Filter Long Words
#! ------------------------------------------------------------
# Given:
#
# words = ["cat", "elephant", "dog", "programming", "car"]
#
# Create a new list containing only words that have
# more than 5 characters.
#
# Use list comprehension.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 38 — Filter Numbers
#! ------------------------------------------------------------
# Given:
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# Create a new list containing only numbers greater than 5.
#
# Use list comprehension.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 39 — Create Squared Numbers
#! ------------------------------------------------------------
# Given:
#
# numbers = [1, 2, 3, 4, 5]
#
# Create a new list containing the square of every number.
#
# Expected:
#
# [1, 4, 9, 16, 25]
#
# Use list comprehension.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 40 — List Comprehension Challenge
#! ------------------------------------------------------------
# Given:
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# Create a new list containing only even numbers.
#
# Use list comprehension.
#
# ------------------------------------------------------------


#! ============================================================
#! Section 08 — Sort Lists
#! ============================================================


#! ------------------------------------------------------------
#! Exercise 41 — Sort Strings
#! ------------------------------------------------------------
# Given:
#
# fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
#
# Sort the list alphabetically.
#
# Print the result.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 42 — Sort Numbers
#! ------------------------------------------------------------
# Given:
#
# numbers = [100, 50, 65, 82, 23]
#
# Sort the numbers from smallest to largest.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 43 — Sort Descending
#! ------------------------------------------------------------
# Given:
#
# numbers = [100, 50, 65, 82, 23]
#
# Sort the numbers from largest to smallest.
#
# Use reverse=True.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 44 — Case-Insensitive Sort
#! ------------------------------------------------------------
# Given:
#
# fruits = ["banana", "Orange", "Kiwi", "cherry"]
#
# First sort normally.
#
# Then create the list again and sort it using:
#
# key=str.lower
#
# Compare the results.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 45 — Reverse Order
#! ------------------------------------------------------------
# Given:
#
# fruits = ["apple", "banana", "cherry", "orange"]
#
# Reverse the order of the list using reverse().
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 46 — Custom Sort Function
#! ------------------------------------------------------------
# Create this function:
#
# def myfunc(n):
#     return abs(n - 50)
#
# Given:
#
# numbers = [100, 50, 65, 82, 23]
#
# Sort the list using:
#
# key=myfunc
#
# Print the result.
#
# Try to understand why the result has this order.
#
# ------------------------------------------------------------


#! ============================================================
#! Section 09 — Copy Lists
#! ============================================================


#! ------------------------------------------------------------
#! Exercise 47 — Copy with copy()
#! ------------------------------------------------------------
# Given:
#
# fruits = ["apple", "banana", "cherry"]
#
# Create a copy using copy().
#
# Store it in a variable called `new_fruits`.
#
# Print both lists.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 48 — Copy with list()
#! ------------------------------------------------------------
# Given:
#
# fruits = ["apple", "banana", "cherry"]
#
# Create a copy using list().
#
# Print the copied list.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 49 — Copy with Slicing
#! ------------------------------------------------------------
# Given:
#
# fruits = ["apple", "banana", "cherry"]
#
# Create a copy using:
#
# [:]
#
# Print the copied list.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 50 — Copy Challenge
#! ------------------------------------------------------------
# Create:
#
# fruits = ["apple", "banana", "cherry"]
#
# Create a copy of the list.
#
# Then add "orange" only to the copied list.
#
# Print both lists.
#
# Question:
#
# Did the original list change?
#
# ------------------------------------------------------------


#! ============================================================
#! Section 10 — Join Lists
#! ============================================================


#! ------------------------------------------------------------
#! Exercise 51 — Join with +
#! ------------------------------------------------------------
# Given:
#
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
#
# Create a third list containing both lists.
#
# Use +.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 52 — Join with append()
#! ------------------------------------------------------------
# Given:
#
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
#
# Use a for loop and append() to add every item
# from list2 to list1.
#
# Print list1.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 53 — Join with extend()
#! ------------------------------------------------------------
# Given:
#
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
#
# Use extend() to add list2 to list1.
#
# Print list1.
#
# ------------------------------------------------------------


#! ============================================================
#! Section 11 — Combined Practice
#! ============================================================


#! ------------------------------------------------------------
#! Exercise 54 — Fruit Manager
#! ------------------------------------------------------------
# Create:
#
# fruits = ["apple", "banana", "cherry"]
#
# Then:
#
# 1. Add "orange"
# 2. Add "mango"
# 3. Remove "banana"
# 4. Change "cherry" to "watermelon"
# 5. Print the final list
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 55 — Programming Languages
#! ------------------------------------------------------------
# Create:
#
# languages = [
#     "Python",
#     "JavaScript",
#     "TypeScript",
#     "Java",
#     "C++"
# ]
#
# Your program should:
#
# 1. Print the first language.
# 2. Print the last language.
# 3. Print the first three languages.
# 4. Check whether "Python" exists.
# 5. Add "C#".
# 6. Remove "Java".
# 7. Print the final list.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 56 — Student Scores
#! ------------------------------------------------------------
# Create:
#
# scores = [85, 70, 92, 60, 78, 95]
#
# Your program should:
#
# 1. Print the scores.
# 2. Print the first score.
# 3. Print the last score.
# 4. Sort the scores.
# 5. Sort them in descending order.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 57 — Filter Students
#! ------------------------------------------------------------
# Given:
#
# scores = [45, 80, 60, 30, 95, 72, 40]
#
# Create a new list containing only scores >= 50.
#
# Use list comprehension.
#
# Expected:
#
# [80, 60, 95, 72]
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 58 — Shopping List
#! ------------------------------------------------------------
# Create:
#
# shopping = [
#     "Laptop",
#     "Mouse",
#     "Keyboard"
# ]
#
# Then:
#
# 1. Add "Monitor".
# 2. Add "Headphones".
# 3. Remove "Mouse".
# 4. Check whether "Laptop" exists.
# 5. Print the final list.
#
# ------------------------------------------------------------


#! ------------------------------------------------------------
#! Exercise 59 — Combine Everything
#! ------------------------------------------------------------
# Create two lists:
#
# frontend = [
#     "HTML",
#     "CSS",
#     "JavaScript"
# ]
#
# backend = [
#     "Python",
#     "Node.js",
#     "PHP"
# ]
#
# Your program should:
#
# 1. Join both lists.
# 2. Print the combined list.
# 3. Sort the combined list alphabetically.
# 4. Check whether "Python" exists.
# 5. Print the first three items.
# 6. Print the last three items.
#
# ------------------------------------------------------------


#! ============================================================
#! Exercise 60 — FINAL CHALLENGE
#! ============================================================
#
# Build a small "Programming Skills Manager".
#
# Create:
#
# skills = [
#     "HTML",
#     "CSS",
#     "JavaScript",
#     "Python",
#     "Git",
#     "Angular"
# ]
#
# Your program should:
#
# 1. Print the original skills.
#
# 2. Print the number of skills.
#
# 3. Print the first skill.
#
# 4. Print the last skill.
#
# 5. Check whether "Python" exists.
#
# 6. Add "TypeScript".
#
# 7. Remove "CSS".
#
# 8. Replace "Git" with "GitHub".
#
# 9. Create a new list containing only skills
#    that contain the letter "t".
#
#    Use list comprehension.
#
# 10. Sort the skills alphabetically.
#
# 11. Create a copy of the skills list.
#
# 12. Add "Docker" to the copied list only.
#
# 13. Print the original list.
#
# 14. Print the copied list.
#
# ------------------------------------------------------------


#* ============================================================
#* End of Exercises
#* ============================================================