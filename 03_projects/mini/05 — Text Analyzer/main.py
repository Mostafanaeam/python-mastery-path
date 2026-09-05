"""
05 — Text Analyzer
اسم الريبو
python-text-analyzer
تفاصيل البروجيكت

اعمل برنامج يستقبل Text من المستخدم ويعمل عليه Analysis.

احسب:

عدد الحروف
عدد الكلمات
عدد الـ spaces
عدد الأرقام
عدد الحروف الكبيرة
عدد الحروف الصغيرة
أطول كلمة
أقصر كلمة
عدد مرات تكرار كلمة معينة

استخدم:

Strings
String Methods
Lists
Loops
Operators
النتيجة النهائية
================================
          TEXT ANALYZER
================================

Enter text:
Python is easy and Python is powerful

Characters : 37
Words      : 7
Spaces     : 6
Numbers    : 0
Uppercase  : 2
Lowercase  : 29

Longest Word : powerful
Shortest Word: is

Python appears: 2 times
Bonus إضافي

اعرض أكثر 5 كلمات تكراراً:

Most Frequent Words:

1. Python   → 2
2. is       → 2
3. easy     → 1
4. and      → 1
5. powerful → 1
"""

print("\n" + 33 * "=")
print("       TEXT ANALYZER")
print( 33 * "=")

while True:
    text = input("\nEnter text: ")
    if text == "" or text.isspace() or text is None or text == "\n":
        print("No text entered. Please try again.")
        continue
    else:
        # Count characters
        num_characters = len(text)
        
        # Count words
        words = text.split()
        num_words = len(words)

        # Count spaces
        num_spaces = text.count(' ')

        # Count numbers
        num_numbers = sum(char.isdigit() for char in text)

        # Count uppercase letters
        num_uppercase = sum(char.isupper() for char in text)

        # Count lowercase letters
        num_lowercase = sum(char.islower() for char in text)

        # Find longest and shortest words
        longest_word = max(words, key=len) if words else ""
        shortest_word = min(words, key=len) if words else ""

        print(f"\nCharacters : {num_characters}")
        print(f"Words      : {num_words}")
        print(f"Spaces     : {num_spaces}")
        print(f"Numbers    : {num_numbers}")
        print(f"Uppercase  : {num_uppercase}")
        print(f"Lowercase  : {num_lowercase}")
        print(f"\nLongest Word : {longest_word}")
        print(f"Shortest Word: {shortest_word}")
        most_frequent_words = lambda text: sorted(((word, text.split().count(word)) for word in set(text.split())), key=lambda x: x[1], reverse=True)[:5]
        print(f"Most Frequent Words: {most_frequent_words(text)}")