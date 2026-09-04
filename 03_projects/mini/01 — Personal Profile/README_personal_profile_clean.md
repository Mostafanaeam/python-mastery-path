# 🧑‍💻 Personal Profile CLI

A simple Python CLI application that collects personal information from the user, validates the entered name, calculates the user's current age from their date of birth, and displays the information in a formatted personal profile.

---

## 🌐 Language

This README is available in two languages:

- 🇬🇧 [English](#english)
- 🇪🇬 [العربية](#arabic)

---

## 📑 Contents

### 🇬🇧 English

- [Project Overview](#project-overview)
- [Project Goals](#project-goals)
- [Features](#features)
  - [Name Validation](#1-name-validation)
  - [Date of Birth Input](#2-date-of-birth-input)
  - [Automatic Age Calculation](#3-automatic-age-calculation)
  - [Personal Information](#4-personal-information)
  - [Formatted Profile Output](#5-formatted-profile-output)
- [Concepts Applied](#concepts-applied)
- [Name Validation Logic](#name-validation-logic)
- [Age Calculation Logic](#age-calculation-logic)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
- [Example Run](#example-run)
- [Challenges](#challenges)
- [What I Learned](#what-i-learned)
- [Future Improvements](#future-improvements)
- [Bonus](#bonus)
- [Notes](#notes)

### 🇪🇬 العربية

- [نبذة عن المشروع](#نبذة-عن-المشروع)
- [أهداف المشروع](#أهداف-المشروع)
- [خصائص المشروع](#خصائص-المشروع)
  - [التحقق من صحة الاسم](#التحقق-من-صحة-الاسم)
  - [إدخال تاريخ الميلاد](#إدخال-تاريخ-الميلاد)
  - [حساب العمر تلقائيًا](#حساب-العمر-تلقائيًا)
  - [المعلومات الشخصية](#المعلومات-الشخصية)
  - [تنسيق البيانات](#تنسيق-البيانات)
- [منطق حساب العمر](#منطق-حساب-العمر)
- [منطق التحقق من الاسم](#منطق-التحقق-من-الاسم)
  - [التعامل مع الإدخال الفارغ](#التعامل-مع-الإدخال-الفارغ)
- [دورة التحقق من الاسم](#دورة-التحقق-من-الاسم)
- [البيانات التي يتم إدخالها](#البيانات-التي-يتم-إدخالها)
- [النتيجة النهائية](#النتيجة-النهائية)
- [المفاهيم التي تم تطبيقها](#المفاهيم-التي-تم-تطبيقها)
- [هيكل المشروع](#هيكل-المشروع)
- [تشغيل المشروع](#تشغيل-المشروع)
- [مثال على تشغيل البرنامج](#مثال-على-تشغيل-البرنامج)
- [التحديات التي واجهتها](#التحديات-التي-واجهتها)
- [ماذا تعلمت](#ماذا-تعلمت)
- [تحسينات مستقبلية](#تحسينات-مستقبلية)
- [Bonus](#bonus-1)
- [ملاحظات](#ملاحظات)

---

<a id="english"></a>

# 🇬🇧 English

<a id="project-overview"></a>

## 📌 Project Overview

The **Personal Profile CLI** is a beginner-friendly Python project designed to practice fundamental Python concepts through a small real-world application.

The program asks the user for:

- Name
- Date of birth
- Country
- Job
- Height
- Weight

It then processes the input, validates the name, calculates the current age, and displays the final profile in a clean format.

---

<a id="project-goals"></a>

## 🎯 Project Goals

The main goal of this project is to apply the following Python concepts in a practical project:

- Variables
- Data Types
- Type Casting
- Strings
- String Methods
- String Formatting
- User Input
- Conditional Statements
- Loops
- Boolean Logic
- Basic Date/Time handling

---

<a id="features"></a>

## ⚙️ Features

### 1. Name Validation

The program validates the user's name before continuing.

It checks that:

- The input is not empty.
- The input is not only whitespace.
- Every character is either a letter or a space.
- Invalid input causes the program to ask again.

Example:

```text
Enter your name: 123

Please enter a valid name.

Enter your name: Mostafa NAEAM
```

The name is then formatted using:

```python
name.title()
```

---

### 2. Date of Birth Input

The program asks the user to enter:

```text
Birth Year
Birth Month
Birth Day
```

The input is converted from strings to integers using:

```python
int()
```

Example:

```python
birth_year = int(input("Enter your birth year: "))
```

---

### 3. Automatic Age Calculation

The program gets the current date using Python's `datetime` module:

```python
datetime.datetime.now()
```

It calculates the age based on:

- Current year
- Current month
- Current day
- Birth year
- Birth month
- Birth day

The program also handles the case where the user's birthday has not happened yet this year.

For example:

```text
Current date: 2026-09-03

Birth date: 2004-10-10
```

The calculated age will be:

```text
21
```

instead of incorrectly returning `22`.

---

### 4. Personal Information

The program collects additional information:

```text
Country
Job
Height
Weight
```

Country and job are formatted using:

```python
.title()
```

Height and weight are converted to integers using:

```python
int()
```

---

### 5. Formatted Profile Output

After collecting all information, the program displays a formatted profile.

Example:

```text
=================================
       PERSONAL PROFILE
=================================
Name       : Mostafa Naeam
Age        : 22
Country    : Egypt
Job        : Software Engineer
Height     : 174 cm
Weight     : 88 kg
=================================
```

---

<a id="concepts-applied"></a>

## 🧠 Concepts Applied

| Concept | How It Is Used |
| --- | --- |
| Variables | Store user information |
| `input()` | Receive information from the user |
| `int()` | Convert numeric input |
| Strings | Handle names, country, and job |
| `.strip()` | Detect empty/whitespace input |
| `.isalpha()` | Validate name characters |
| `all()` | Validate all characters in the name |
| `.title()` | Format text |
| `while` | Repeat input until valid |
| `continue` | Restart validation when input is invalid |
| `break` | Exit the validation loop |
| `if` | Check validation and calculate age |
| `datetime` | Get the current date |
| f-strings | Format output |

---

<a id="name-validation-logic"></a>

## 🔍 Name Validation Logic

The project uses:

```python
is_valid = all(
    char.isalpha() or char == " "
    for char in name
)
```

This means that every character must satisfy at least one of these conditions:

```text
Character is a letter

OR

Character is a space
```

Before that, the program checks:

```python
if not name.strip():
```

This prevents accepting:

```text
""

"   "
```

because `all()` returns `True` for an empty iterable.

The overall validation flow is:

```text
User Input
    ↓
Empty / Whitespace?
    ↓ Yes
Invalid
    ↓ No
Check Every Character
    ↓
Letter or Space?
    ↓ No
Invalid
    ↓ Yes
Format Name
    ↓
Continue Program
```

---

<a id="age-calculation-logic"></a>

## 🧮 Age Calculation Logic

The initial age is calculated using:

```python
age = current_year - birth_year
```

Then the program checks whether the user's birthday has happened yet during the current year:

```python
if current_month < birth_month or (
    current_month == birth_month and current_day < birth_day
):
    age -= 1
```

This makes the calculation more accurate than simply subtracting the birth year from the current year.

---

<a id="project-structure"></a>

## 🗂️ Project Structure

```text
python-personal-profile/

│
├── README.md
│
└── main.py
```

---

<a id="how-to-run"></a>

## ▶️ How to Run

Make sure Python is installed:

```bash
python --version
```

Then run:

```bash
python main.py
```

---

<a id="example-run"></a>

## 💻 Example Run

```text
Enter your name: Mostafa NAEAM

Enter your birth year: 2004

Enter your birth month: 10

Enter your birth day: 10

Enter your country: Egypt

Enter your job: Software Engineer

Enter your height in cm: 174

Enter your weight in kg: 88

=================================
       PERSONAL PROFILE
=================================
Name       : Mostafa Naeam
Age        : 21
Country    : Egypt
Job        : Software Engineer
Height     : 174 cm
Weight     : 88 kg
=================================
```

---

<a id="challenges"></a>

## 🚧 Challenges

### Name Validation

One of the main challenges was validating the name correctly.

The validation needed to handle:

- Empty input
- Whitespace-only input
- Numbers
- Special characters
- Names containing spaces

The solution used `all()` with a generator expression:

```python
all(char.isalpha() or char == " " for char in name)
```

---

### Accurate Age Calculation

Simply calculating:

```python
current_year - birth_year
```

is not always accurate.

The user's birthday may not have occurred yet in the current year.

Therefore, the program compares the current month/day with the birth month/day and adjusts the age when necessary.

---

<a id="what-i-learned"></a>

## 📚 What I Learned

Through this project, I practiced turning basic Python concepts into a complete small CLI application.

The most important concepts I practiced were:

- Receiving and processing user input.
- Converting data between types.
- Validating user input.
- Using `while` loops for input validation.
- Using `all()` with generator expressions.
- Working with strings and string methods.
- Using conditional logic.
- Working with Python's `datetime` module.
- Formatting console output.
- Thinking about edge cases instead of only the happy path.

---

<a id="future-improvements"></a>

## 🚀 Future Improvements

Possible improvements for future versions:

- Add better validation for birth date.
- Prevent impossible dates such as month `13`.
- Validate height and weight.
- Automatically calculate the birth year from the user's age.
- Add Full Name support.
- Add BMI calculation.
- Save the profile to a file.
- Load an existing profile.
- Add a menu-based CLI.
- Split validation and calculation logic into functions.

---

<a id="bonus"></a>

## 🎁 Bonus

The original project specification includes an additional challenge:

Instead of asking for the birth year directly, allow the user to enter:

```text
Full Name
Age
Current Year
```

and calculate:

```text
Birth Year = Current Year - Age
```

A more accurate version can also consider whether the user's birthday has already occurred this year.

---

<a id="notes"></a>

## 📝 Notes

This project is part of my Python learning journey and focuses on practicing fundamental Python concepts by building a small project from scratch.

The objective is not only to make the program work, but also to understand **why each part of the code is needed and how the different Python concepts work together**.

---

<a id="arabic"></a>

# 🇪🇬 العربية

## 📌 نبذة عن المشروع

برنامج بسيط يعمل من خلال **Terminal / CLI** باستخدام Python، يقوم بجمع البيانات الشخصية من المستخدم، والتحقق من صحة الاسم، وحساب العمر الحالي بناءً على تاريخ الميلاد، ثم عرض البيانات في صورة **Personal Profile** منظمة.

---

## 🎯 أهداف المشروع

هذا المشروع من المشاريع التدريبية الأولى في رحلة تعلم Python، والهدف منه تطبيق مجموعة من المفاهيم الأساسية بشكل عملي بدلًا من دراستها بشكل منفصل.

الهدف الأساسي من المشروع هو تطبيق المفاهيم التالية من Python:

- Variables
- Data Types
- Type Casting
- Strings
- String Methods
- String Formatting
- User Input
- Conditional Statements
- Loops
- Boolean Logic
- Basic Date/Time Handling

---

## ⚙️ خصائص المشروع

### 1. التحقق من صحة الاسم

البرنامج لا يسمح بمتابعة التنفيذ إلا بعد إدخال اسم صالح.

يتم التأكد من أن:

- الإدخال ليس فارغًا.
- الإدخال ليس عبارة عن مسافات فقط.
- جميع الأحرف الموجودة في الاسم حروف أو مسافات.
- في حالة إدخال قيمة غير صحيحة، يتم طلب الاسم مرة أخرى.

مثال:

```text
Enter your name: 123

Please enter a valid name.

Enter your name: Mostafa NAEAM
```

بعد نجاح التحقق يتم تنسيق الاسم باستخدام:

```python
name.title()
```

---

### 2. إدخال تاريخ الميلاد

يطلب البرنامج من المستخدم إدخال:

```text
Birth Year
Birth Month
Birth Day
```

ويتم تحويل القيم المدخلة من `String` إلى `Integer` باستخدام:

```python
int()
```

مثال:

```python
birth_year = int(input("Enter your birth year: "))
```

---

### 3. حساب العمر تلقائيًا

يستخدم البرنامج مكتبة `datetime` للحصول على التاريخ الحالي:

```python
datetime.datetime.now()
```

ثم يحسب العمر بناءً على:

- السنة الحالية
- الشهر الحالي
- اليوم الحالي
- سنة الميلاد
- شهر الميلاد
- يوم الميلاد

ولا يعتمد البرنامج على طرح سنة الميلاد من السنة الحالية فقط.

فإذا كان عيد ميلاد المستخدم لم يأتِ بعد خلال السنة الحالية، يتم تقليل العمر سنة واحدة.

مثال:

```text
Current Date: 2026-09-03

Birth Date: 2004-10-10
```

العمر الصحيح:

```text
21
```

وليس:

```text
22
```

---

### 4. المعلومات الشخصية

يطلب البرنامج من المستخدم إدخال:

```text
Country
Job
Height
Weight
```

ويتم تنسيق الدولة والوظيفة باستخدام:

```python
.title()
```

كما يتم تحويل الطول والوزن إلى أعداد صحيحة باستخدام:

```python
int()
```

---

### 5. تنسيق البيانات

بعد إدخال جميع البيانات، يعرض البرنامج الملف الشخصي بشكل منظم:

```text
=================================
       PERSONAL PROFILE
=================================
Name       : Mostafa Naeam
Age        : 21
Country    : Egypt
Job        : Software Engineer
Height     : 174 cm
Weight     : 88 kg
=================================
```

---

## 🧮 منطق حساب العمر

في البداية يتم حساب العمر:

```python
age = current_year - birth_year
```

ثم يتم التحقق مما إذا كان عيد الميلاد قد حدث بالفعل خلال السنة الحالية:

```python
if current_month < birth_month or (
    current_month == birth_month and current_day < birth_day
):
    age -= 1
```

وبالتالي يكون حساب العمر أكثر دقة من مجرد طرح سنة الميلاد من السنة الحالية.

---

## 🔍 منطق التحقق من الاسم

يستخدم المشروع:

```python
is_valid = all(
    char.isalpha() or char == " "
    for char in name
)
```

المعنى هنا:

> يجب أن يكون **كل Character** في الاسم إما حرفًا أو مسافة.

مثال:

```text
Mostafa NAEAM
```

يعتبر صالحًا.

بينما:

```text
Mostafa123
```

أو:

```text
Mostafa@Naeam
```

يعتبر غير صالح.

---

### التعامل مع الإدخال الفارغ

هناك حالة خاصة يجب التعامل معها وهي:

```text
""

"   "
```

لذلك يتم استخدام:

```python
if not name.strip():
```

للتأكد من أن المستخدم أدخل اسمًا فعليًا وليس قيمة فارغة أو مسافات فقط.

---

## 🔄 دورة التحقق من الاسم

منطق البرنامج يعمل بالشكل التالي:

```text
إدخال الاسم
     ↓
هل الاسم فارغ أو يحتوي على Spaces فقط؟
     ↓ نعم
إدخال غير صالح
     ↓ لا
فحص جميع Characters
     ↓
هل كل Character حرف أو Space؟
     ↓ لا
إدخال غير صالح
     ↓ نعم
تنسيق الاسم
     ↓
متابعة البرنامج
```

ويتم استخدام:

```python
while True:
```

لإبقاء البرنامج في حلقة التحقق حتى يتم إدخال اسم صالح.

---

## 🧾 البيانات التي يتم إدخالها

| البيانات | نوع البيانات |
| --- | --- |
| Name | `str` |
| Birth Year | `int` |
| Birth Month | `int` |
| Birth Day | `int` |
| Country | `str` |
| Job | `str` |
| Height | `int` |
| Weight | `int` |

---

## 🎨 تنسيق البيانات

يتم استخدام:

```python
.title()
```

لتنسيق بعض البيانات النصية.

مثال:

```python
country = input("Enter your country: ").title()
```

إذا أدخل المستخدم:

```text
egypt
```

سيتم عرضها:

```text
Egypt
```

ونفس الفكرة يتم تطبيقها على الوظيفة والاسم.

---

## 🖥️ النتيجة النهائية

بعد إدخال البيانات، يعرض البرنامج Profile منظمًا:

```text
=================================
       PERSONAL PROFILE
=================================
Name       : Mostafa Naeam
Age        : 21
Country    : Egypt
Job        : Software Engineer
Height     : 174 cm
Weight     : 88 kg
=================================
```

---

## 🧩 المفاهيم التي تم تطبيقها

| المفهوم | استخدامه في المشروع |
| --- | --- |
| Variables | تخزين بيانات المستخدم |
| `input()` | استقبال البيانات من المستخدم |
| `int()` | تحويل البيانات الرقمية |
| Strings | التعامل مع النصوص |
| `.strip()` | التحقق من الإدخال الفارغ |
| `.isalpha()` | التحقق من الحروف |
| `all()` | التحقق من جميع Characters |
| `.title()` | تنسيق النصوص |
| `while` | تكرار طلب الإدخال |
| `continue` | إعادة محاولة الإدخال |
| `break` | الخروج من حلقة التحقق |
| `if` | تنفيذ الشروط |
| `datetime` | الحصول على التاريخ الحالي |
| f-strings | تنسيق النصوص عند الطباعة |

---

## 📂 هيكل المشروع

```text
python-personal-profile/

│
├── README.md
│
└── main.py
```

---

## ▶️ تشغيل المشروع

تأكد أولًا من تثبيت Python:

```bash
python --version
```

ثم قم بتشغيل البرنامج:

```bash
python main.py
```

---

## 🧪 مثال على تشغيل البرنامج

```text
Enter your name: Mostafa NAEAM

Enter your birth year: 2004

Enter your birth month: 10

Enter your birth day: 10

Enter your country: Egypt

Enter your job: Software Engineer

Enter your height in cm: 174

Enter your weight in kg: 88

=================================
       PERSONAL PROFILE
=================================
Name       : Mostafa Naeam
Age        : 21
Country    : Egypt
Job        : Software Engineer
Height     : 174 cm
Weight     : 88 kg
=================================
```

---

## 🚧 التحديات التي واجهتها

### التحقق من الاسم

كان من التحديات معرفة الطريقة الصحيحة للتأكد من أن الاسم:

- ليس فارغًا.
- ليس عبارة عن Spaces فقط.
- لا يحتوي على أرقام.
- لا يحتوي على Symbols.
- يسمح بوجود Spaces بين أجزاء الاسم.

تم حل ذلك باستخدام:

```python
all(
    char.isalpha() or char == " "
    for char in name
)
```

مع:

```python
name.strip()
```

---

### حساب العمر

الحساب البسيط:

```python
current_year - birth_year
```

قد يعطي عمرًا غير دقيق إذا كان عيد ميلاد المستخدم لم يأتِ بعد في السنة الحالية.

لذلك تمت إضافة مقارنة بين:

```text
Current Month / Day
```

و:

```text
Birth Month / Day
```

للحصول على العمر الفعلي.

---

## 📚 ماذا تعلمت؟

من خلال هذا المشروع تعلمت كيفية تحويل المفاهيم الأساسية في Python إلى برنامج صغير متكامل.

ومن أهم الأشياء التي تم تطبيقها:

- استقبال بيانات من المستخدم.
- التعامل مع أنواع البيانات المختلفة.
- استخدام Type Casting.
- التحقق من صحة User Input.
- استخدام `while` في Input Validation.
- استخدام `all()` مع Generator Expression.
- التعامل مع Strings وString Methods.
- استخدام Boolean Logic.
- استخدام Conditional Statements.
- التعامل مع التاريخ باستخدام `datetime`.
- تنسيق البيانات عند عرضها.
- التفكير في Edge Cases بدلًا من الاعتماد على الـ Happy Path فقط.

---

## 🚀 تحسينات مستقبلية

يمكن تطوير المشروع مستقبلًا بإضافة:

- التحقق من صحة تاريخ الميلاد.
- منع إدخال شهر غير صحيح مثل `13`.
- منع إدخال يوم غير صحيح.
- التحقق من الطول والوزن.
- إضافة Full Name بشكل أكثر تفصيلًا.
- حساب سنة الميلاد تلقائيًا من العمر.
- حساب BMI.
- حفظ البيانات في ملف.
- قراءة Profile محفوظ مسبقًا.
- إضافة Menu للبرنامج.
- تقسيم الكود إلى Functions.

---

## 🎁 Bonus

المطلوب الإضافي في فكرة المشروع هو جعل المستخدم يدخل:

```text
Full Name
Age
Current Year
```

بدلًا من إدخال سنة الميلاد مباشرة.

ثم يتم حساب:

```text
Birth Year = Current Year - Age
```

ويمكن تطوير الفكرة أكثر بحيث يتم أخذ تاريخ الميلاد الكامل في الاعتبار للحصول على نتيجة أدق.

---

## 📝 ملاحظات

هذا المشروع جزء من رحلة تعلم Python، والغرض منه ليس فقط كتابة برنامج يعمل، ولكن تطبيق المفاهيم التي تم تعلمها عمليًا.

الهدف الأساسي هو الانتقال من:

```text
Learning Concepts

       ↓

Writing Small Examples

       ↓

Building a Real Project

       ↓

Understanding the Code
```

المشروع لا يعتبر مكتملًا لمجرد أنه يعمل، وإنما يجب أن أفهم كل جزء من الكود وأعرف لماذا تم استخدامه وكيف يمكن تطويره.
