# 🔢 Number Analyzer CLI

A simple Python CLI application that receives a number from the user and analyzes it using basic Python concepts such as numbers, casting, arithmetic operators, comparison operators, boolean logic, and user input.

---

## 🌐 Language

This README is available in two languages:

* 🇬🇧 [English](#english)
* 🇪🇬 [العربية](#arabic)

---

## 📑 Contents

### 🇬🇧 English

* [Project Overview](#project-overview)
* [Project Goals](#project-goals)
* [Features](#features)

  * [Number Input](#number-input)
  * [Number Type](#number-type)
  * [Number Sign](#number-sign)
  * [Even and Odd](#even-and-odd)
  * [Square and Cube](#square-and-cube)
  * [Divisibility Analysis](#divisibility-analysis)
* [Concepts Applied](#concepts-applied)
* [Input Validation Logic](#input-validation-logic)
* [Number Analysis Logic](#number-analysis-logic)
* [Project Structure](#project-structure)
* [How to Run](#how-to-run)
* [Example Run](#example-run)
* [Challenges](#challenges)
* [What I Learned](#what-i-learned)
* [Future Improvements](#future-improvements)
* [Bonus](#bonus)
* [Notes](#notes)

### 🇪🇬 العربية

* [نبذة عن المشروع](#نبذة-عن-المشروع)
* [أهداف المشروع](#أهداف-المشروع)
* [خصائص المشروع](#خصائص-المشروع)

  * [إدخال الرقم](#إدخال-الرقم)
  * [نوع الرقم](#نوع-الرقم)
  * [تحديد إشارة الرقم](#تحديد-إشارة-الرقم)
  * [الرقم زوجي أم فردي](#الرقم-زوجي-أم-فردي)
  * [مربع ومكعب الرقم](#مربع-ومكعب-الرقم)
  * [تحليل قابلية القسمة](#تحليل-قابلية-القسمة)
* [المفاهيم التي تم تطبيقها](#المفاهيم-التي-تم-تطبيقها)
* [منطق التحقق من الإدخال](#منطق-التحقق-من-الإدخال)
* [منطق تحليل الرقم](#منطق-تحليل-الرقم)
* [هيكل المشروع](#هيكل-المشروع)
* [تشغيل المشروع](#تشغيل-المشروع)
* [مثال على تشغيل البرنامج](#مثال-على-تشغيل-البرنامج)
* [التحديات](#التحديات)
* [ماذا تعلمت](#ماذا-تعلمت)
* [تحسينات مستقبلية](#تحسينات-مستقبلية)
* [Bonus](#bonus-1)
* [ملاحظات](#ملاحظات)

---

<a id="english"></a>

# 🇬🇧 English

## 📌 Project Overview

**Number Analyzer CLI** is a small Python project that receives a number from the user and performs several basic analyses on it.

The project is designed to practice fundamental Python concepts by applying them to a simple CLI application.

The program analyzes:

* Whether the number is positive.
* Whether the number is negative.
* Whether the number is zero.
* Whether the number is even or odd.
* The number's type.
* The square of the number.
* The cube of the number.
* Whether the number is divisible by 3.
* Whether the number is divisible by 5.
* Whether the number is divisible by 10.

---

## 🎯 Project Goals

The main goal of this project is to practice the following Python concepts:

* Numbers
* Casting
* Arithmetic Operators
* Comparison Operators
* Boolean
* User Input
* Input Validation
* Loops
* Modulo Operator
* Exponentiation

The project focuses on taking a value from the user and using Python expressions to derive useful information from it.

---

## ⚙️ Features

### 1. Number Input

The program asks the user to enter a number:

```text
Enter a number:
```

The input is initially received as a string because Python's `input()` function returns a `str`.

The program validates the input before converting it.

---

### 2. Number Type

After validation, the entered value is converted to an integer:

```python
Number = int(Number)
```

The program then displays the type of the resulting value:

```python
type(Number)
```

Example:

```text
Type : <class 'int'>
```

---

### 3. Number Sign

The program checks whether the number is:

* Positive
* Negative
* Zero

Using comparison operators:

```python
Number > 0
```

```python
Number < 0
```

```python
Number == 0
```

Each expression returns a Boolean value:

```text
True
False
```

---

### 4. Even and Odd

The program determines whether the number is even or odd using the modulo operator `%`.

Even:

```python
Number % 2 == 0
```

Odd:

```python
Number % 2 != 0
```

For example:

```text
25 % 2 = 1
```

Therefore, `25` is odd.

---

### 5. Square and Cube

The program calculates the square and cube of the number using the exponentiation operator `**`.

Square:

```python
Number ** 2
```

Cube:

```python
Number ** 3
```

For example:

```text
25² = 625

25³ = 15625
```

---

### 6. Divisibility Analysis

The program also checks whether the number is divisible by:

* 3
* 5
* 10

This is done using the modulo operator:

```python
Number % 3 == 0
```

```python
Number % 5 == 0
```

```python
Number % 10 == 0
```

If the remainder is `0`, the number is divisible by that value.

---

## 🧠 Concepts Applied

| Concept      | How It Is Used                        |
| ------------ | ------------------------------------- |
| `input()`    | Receive the number from the user      |
| `.isdigit()` | Validate numeric input                |
| `int()`      | Convert the input from `str` to `int` |
| `type()`     | Determine the type of the number      |
| Numbers      | Store and analyze numeric values      |
| `>`          | Check whether the number is positive  |
| `<`          | Check whether the number is negative  |
| `==`         | Check whether the number is zero      |
| `%`          | Check even/odd and divisibility       |
| `**`         | Calculate square and cube             |
| Boolean      | Store and display analysis results    |
| `while`      | Repeat input until valid              |
| `continue`   | Restart the input process             |
| `break`      | Exit the validation loop              |
| `print()`    | Display the analysis results          |

---

## 🔍 Input Validation Logic

The project validates the input before converting it into an integer.

The validation uses:

```python
while True:
    Number = input("Enter a number: ")

    if not Number.isdigit():
        print("Please enter a valid number.")
        continue

    break
```

The flow is:

```text
User Input
    ↓
Check if input contains only digits
    ↓
    No
    ↓
Invalid Input
    ↓
Ask Again
```

If the input is valid:

```text
Valid Input
    ↓
Exit Loop
    ↓
Convert to int
    ↓
Analyze Number
```

After validation:

```python
Number = int(Number)
```

---

## 🧮 Number Analysis Logic

The program uses comparison operators and arithmetic operators to analyze the number.

### Positive

```python
Number > 0
```

Returns `True` when the number is greater than zero.

### Negative

```python
Number < 0
```

Returns `True` when the number is less than zero.

### Zero

```python
Number == 0
```

Returns `True` when the number equals zero.

### Even

```python
Number % 2 == 0
```

### Odd

```python
Number % 2 != 0
```

### Square

```python
Number ** 2
```

### Cube

```python
Number ** 3
```

### Divisible by 3

```python
Number % 3 == 0
```

### Divisible by 5

```python
Number % 5 == 0
```

### Divisible by 10

```python
Number % 10 == 0
```

---

## 🗂️ Project Structure

```text
python-number-analyzer/

│
├── README.md
│
└── main.py
```

---

## ▶️ How to Run

Make sure Python is installed:

```bash
python --version
```

Then run the program:

```bash
python main.py
```

---

## 💻 Example Run

```text
Enter a number: 25

=================================
       NUMBER ANALYZER
=================================
Number          : 25
Type            : <class 'int'>
Positive        : True
Negative        : False
Zero            : False
Even            : False
Odd             : True
Square          : 625
Cube            : 15625
Divisible by 3  : False
Divisible by 5  : True
Divisible by 10 : False
=================================
```

---

## 🚧 Challenges

### Input Validation

One of the challenges in the project is making sure that the user enters a valid numeric value before converting it with `int()`.

The program uses:

```python
Number.isdigit()
```

to check the input before performing the conversion.

If the input is invalid, the program asks the user to enter the value again.

---

### Understanding Boolean Expressions

Another important part of the project is understanding that expressions such as:

```python
Number > 0
```

do not return a number.

They return a Boolean value:

```text
True
```

or:

```text
False
```

The same idea is used for checking zero, even/odd numbers, and divisibility.

---

### Using the Modulo Operator

The `%` operator is important in this project because it allows the program to determine the remainder of a division.

For example:

```python
25 % 2
```

returns:

```text
1
```

Therefore, `25` is not divisible by `2`, which means it is odd.

---

## 📚 What I Learned

Through this project, I practiced how to turn basic numeric operations into a complete CLI application.

The main concepts I practiced were:

* Receiving user input.
* Validating numeric input.
* Converting strings into integers.
* Using comparison operators.
* Using Boolean expressions.
* Using the modulo operator.
* Checking whether a number is even or odd.
* Checking divisibility.
* Calculating powers.
* Using loops for input validation.
* Displaying calculated results in a structured format.

The project also helped me understand how several simple Python concepts can work together to build a useful program.

---

## 🚀 Future Improvements

Possible improvements for future versions:

* Support negative numbers such as `-25`.
* Support floating-point numbers such as `25.5`.
* Display the input as `int` or `float`.
* Add validation for empty input.
* Add better numeric input handling.
* Add more divisibility checks.
* Add a prime number checker.
* Move the analysis logic into functions.
* Add a menu-based CLI.
* Add automated tests.

---

## 🎁 Bonus

The original project specification includes additional analysis:

### Prime Number

Check whether the entered number is a prime number.

### Divisible by 3

```python
Number % 3 == 0
```

### Divisible by 5

```python
Number % 5 == 0
```

### Divisible by 10

```python
Number % 10 == 0
```

The current implementation already includes the divisibility checks for `3`, `5`, and `10`.

---

## 📝 Notes

This project is part of my Python learning journey.

The goal is not only to write a program that produces the correct output, but also to understand how:

```text
User Input
    ↓
Validation
    ↓
Type Casting
    ↓
Arithmetic Operations
    ↓
Comparison Operations
    ↓
Boolean Results
    ↓
Formatted Output
```

work together inside a Python CLI application.

---

<a id="arabic"></a>

# 🇪🇬 العربية

## 📌 نبذة عن المشروع

**Number Analyzer CLI** هو مشروع Python بسيط يستقبل رقمًا من المستخدم ثم يقوم بإجراء مجموعة من التحليلات الأساسية عليه.

الهدف من المشروع هو تطبيق مجموعة من مفاهيم Python الأساسية بشكل عملي من خلال برنامج يعمل من خلال الـ **Terminal / CLI**.

يقوم البرنامج بتحليل:

* هل الرقم موجب؟
* هل الرقم سالب؟
* هل الرقم يساوي صفر؟
* هل الرقم زوجي أم فردي؟
* نوع الرقم.
* مربع الرقم.
* مكعب الرقم.
* هل الرقم يقبل القسمة على 3؟
* هل الرقم يقبل القسمة على 5؟
* هل الرقم يقبل القسمة على 10؟

---

## 🎯 أهداف المشروع

الهدف الأساسي من المشروع هو تطبيق المفاهيم التالية:

* Numbers
* Casting
* Arithmetic Operators
* Comparison Operators
* Boolean
* User Input
* Input Validation
* Loops
* Modulo Operator
* Exponentiation

الفكرة الأساسية هي استقبال قيمة من المستخدم ثم استخدام العمليات والتعبيرات الموجودة في Python لاستخراج معلومات مختلفة عنها.

---

## ⚙️ خصائص المشروع

### 1. إدخال الرقم

يطلب البرنامج من المستخدم إدخال رقم:

```text
Enter a number:
```

في البداية تكون القيمة المدخلة من النوع `str` لأن:

```python
input()
```

تُرجع دائمًا قيمة نصية.

لذلك يتم التحقق من الإدخال أولًا قبل تحويله إلى رقم.

---

### 2. نوع الرقم

بعد التحقق من الإدخال، يتم تحويل القيمة إلى `int`:

```python
Number = int(Number)
```

ثم يتم عرض نوع الرقم باستخدام:

```python
type(Number)
```

مثال:

```text
Type : <class 'int'>
```

---

### 3. تحديد إشارة الرقم

يقوم البرنامج بتحديد هل الرقم:

* موجب.
* سالب.
* يساوي صفر.

باستخدام Comparison Operators:

```python
Number > 0
```

```python
Number < 0
```

```python
Number == 0
```

وكل تعبير من هذه التعبيرات يرجع قيمة Boolean:

```text
True
```

أو:

```text
False
```

---

### 4. الرقم زوجي أم فردي

يستخدم البرنامج الـ Modulo Operator `%` لمعرفة هل الرقم زوجي أم فردي.

الرقم الزوجي:

```python
Number % 2 == 0
```

الرقم الفردي:

```python
Number % 2 != 0
```

مثال:

```text
25 % 2 = 1
```

لذلك الرقم `25` فردي.

---

### 5. مربع ومكعب الرقم

يتم حساب مربع الرقم ومكعبه باستخدام الـ Exponentiation Operator `**`.

المربع:

```python
Number ** 2
```

المكعب:

```python
Number ** 3
```

مثال:

```text
25² = 625

25³ = 15625
```

---

### 6. تحليل قابلية القسمة

يقوم البرنامج أيضًا بالتحقق من قابلية الرقم للقسمة على:

* 3
* 5
* 10

باستخدام `%`:

```python
Number % 3 == 0
```

```python
Number % 5 == 0
```

```python
Number % 10 == 0
```

إذا كان باقي القسمة يساوي `0`، فهذا يعني أن الرقم يقبل القسمة على الرقم المحدد.

---

## 🧠 المفاهيم التي تم تطبيقها

| المفهوم      | استخدامه في المشروع                |
| ------------ | ---------------------------------- |
| `input()`    | استقبال الرقم من المستخدم          |
| `.isdigit()` | التحقق من أن الإدخال أرقام         |
| `int()`      | تحويل الإدخال من `str` إلى `int`   |
| `type()`     | معرفة نوع الرقم                    |
| Numbers      | تخزين وتحليل الأرقام               |
| `>`          | التحقق من أن الرقم موجب            |
| `<`          | التحقق من أن الرقم سالب            |
| `==`         | التحقق من أن الرقم يساوي صفر       |
| `%`          | معرفة الزوجي/الفردي وقابلية القسمة |
| `**`         | حساب مربع ومكعب الرقم              |
| Boolean      | عرض نتائج التحليل                  |
| `while`      | تكرار الإدخال حتى يكون صالحًا      |
| `continue`   | إعادة محاولة الإدخال               |
| `break`      | الخروج من حلقة التحقق              |
| `print()`    | عرض نتائج التحليل                  |

---

## 🔍 منطق التحقق من الإدخال

يقوم المشروع بالتحقق من الرقم قبل تحويله إلى `int`.

يتم استخدام:

```python
while True:
    Number = input("Enter a number: ")

    if not Number.isdigit():
        print("Please enter a valid number.")
        continue

    break
```

ويكون تدفق البرنامج:

```text
إدخال الرقم
    ↓
هل الإدخال يحتوي على أرقام فقط؟
    ↓
    لا
    ↓
إدخال غير صالح
    ↓
إعادة طلب الإدخال
```

أما إذا كان الإدخال صالحًا:

```text
إدخال صالح
    ↓
الخروج من الحلقة
    ↓
تحويل القيمة إلى int
    ↓
تحليل الرقم
```

وبعد انتهاء عملية التحقق:

```python
Number = int(Number)
```

---

## 🧮 منطق تحليل الرقم

يستخدم البرنامج Comparison Operators وArithmetic Operators لتحليل الرقم.

### الرقم الموجب

```python
Number > 0
```

ترجع `True` إذا كان الرقم أكبر من صفر.

### الرقم السالب

```python
Number < 0
```

ترجع `True` إذا كان الرقم أقل من صفر.

### الرقم صفر

```python
Number == 0
```

ترجع `True` إذا كان الرقم يساوي صفر.

### الرقم الزوجي

```python
Number % 2 == 0
```

### الرقم الفردي

```python
Number % 2 != 0
```

### مربع الرقم

```python
Number ** 2
```

### مكعب الرقم

```python
Number ** 3
```

### قابلية القسمة على 3

```python
Number % 3 == 0
```

### قابلية القسمة على 5

```python
Number % 5 == 0
```

### قابلية القسمة على 10

```python
Number % 10 == 0
```

---

## 📂 هيكل المشروع

```text
python-number-analyzer/

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
Enter a number: 25

=================================
       NUMBER ANALYZER
=================================
Number          : 25
Type            : <class 'int'>
Positive        : True
Negative        : False
Zero            : False
Even            : False
Odd             : True
Square          : 625
Cube            : 15625
Divisible by 3  : False
Divisible by 5  : True
Divisible by 10 : False
=================================
```

---

## 🚧 التحديات

### التحقق من الإدخال

من التحديات في المشروع التأكد من أن المستخدم أدخل قيمة رقمية صحيحة قبل محاولة تحويلها باستخدام `int()`.

تم استخدام:

```python
Number.isdigit()
```

للتحقق من الإدخال قبل عملية التحويل.

إذا كان الإدخال غير صالح، يعيد البرنامج طلب الرقم من المستخدم.

---

### فهم الـ Boolean Expressions

من النقاط المهمة في المشروع فهم أن التعبيرات مثل:

```python
Number > 0
```

لا ترجع رقمًا.

ولكنها ترجع قيمة Boolean:

```text
True
```

أو:

```text
False
```

ونفس الفكرة يتم استخدامها عند التحقق من الصفر، والزوجي والفردي، وقابلية القسمة.

---

### استخدام Modulo Operator

الـ `%` من أهم العمليات المستخدمة في المشروع، لأنه يسمح بمعرفة باقي القسمة.

مثال:

```python
25 % 2
```

النتيجة:

```text
1
```

وبالتالي `25` لا يقبل القسمة على `2`، ولذلك فهو رقم فردي.

---

## 📚 ماذا تعلمت؟

من خلال هذا المشروع تعلمت كيفية تحويل العمليات الحسابية البسيطة إلى برنامج CLI متكامل.

ومن أهم المفاهيم التي تم تطبيقها:

* استقبال User Input.
* التحقق من الإدخال الرقمي.
* تحويل `str` إلى `int`.
* استخدام Comparison Operators.
* استخدام Boolean Expressions.
* استخدام Modulo Operator.
* تحديد هل الرقم زوجي أم فردي.
* التحقق من قابلية القسمة.
* حساب القوى.
* استخدام Loops في التحقق من الإدخال.
* عرض النتائج بشكل منظم.

كما ساعدني المشروع على فهم كيفية تعاون مجموعة من المفاهيم البسيطة معًا لبناء برنامج Python مفيد.

---

## 🚀 تحسينات مستقبلية

يمكن تطوير المشروع مستقبلًا بإضافة:

* دعم الأرقام السالبة مثل `-25`.
* دعم الأرقام العشرية مثل `25.5`.
* عرض الرقم على هيئة `int` أو `float`.
* إضافة Validation للإدخال الفارغ.
* تحسين طريقة التعامل مع الإدخال الرقمي.
* إضافة المزيد من اختبارات قابلية القسمة.
* إضافة فحص Prime Number.
* تقسيم منطق التحليل إلى Functions.
* إضافة Menu للبرنامج.
* إضافة Automated Tests.

---

## 🎁 Bonus

المطلوب الإضافي في فكرة المشروع هو إضافة تحليلات أخرى للرقم.

### Prime Number

إضافة فحص لمعرفة هل الرقم Prime Number أم لا.

### Divisible by 3

```python
Number % 3 == 0
```

### Divisible by 5

```python
Number % 5 == 0
```

### Divisible by 10

```python
Number % 10 == 0
```

والنسخة الحالية من المشروع تحتوي بالفعل على فحوصات قابلية القسمة على `3` و`5` و`10`.

---

## 📝 ملاحظات

هذا المشروع جزء من رحلة تعلم Python.

الهدف ليس فقط كتابة برنامج يعطي نتيجة صحيحة، ولكن فهم كيفية عمل المفاهيم معًا:

```text
User Input
    ↓
Validation
    ↓
Type Casting
    ↓
Arithmetic Operations
    ↓
Comparison Operations
    ↓
Boolean Results
    ↓
Formatted Output
```

وبالتالي الانتقال من تعلم المفهوم بشكل منفصل إلى استخدامه داخل برنامج حقيقي صغير.
