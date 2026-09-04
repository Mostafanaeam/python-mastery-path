# 🔄 Unit Converter CLI

A simple Python CLI application for converting values between different units of temperature, length, and weight.

---

## 🌐 Language

* 🇬🇧 [English](#english)
* 🇪🇬 [العربية](#arabic)

---

## 📑 Contents

### 🇬🇧 English

* [Project Overview](#project-overview)
* [Supported Conversions](#supported-conversions)
* [Concepts Used](#concepts-used)
* [How It Works](#how-it-works)
* [Project Structure](#project-structure)
* [How to Run](#how-to-run)
* [Example](#example)
* [Bonus](#bonus)
* [Future Improvements](#future-improvements)

### 🇪🇬 العربية

* [نبذة عن المشروع](#نبذة-عن-المشروع)
* [التحويلات المدعومة](#التحويلات-المدعومة)
* [المفاهيم المستخدمة](#المفاهيم-المستخدمة)
* [كيف يعمل المشروع](#كيف-يعمل-المشروع)
* [هيكل المشروع](#هيكل-المشروع)
* [تشغيل المشروع](#تشغيل-المشروع)
* [مثال](#مثال)
* [Bonus](#bonus-1)
* [تحسينات مستقبلية](#تحسينات-مستقبلية)

---

<a id="english"></a>

# 🇬🇧 English

## 📌 Project Overview

**Unit Converter CLI** is a simple Python project that converts values between different units.

The program provides conversions for:

* Temperature
* Length
* Weight

The user chooses a conversion, enters a value, and the program displays the result.

---

## 🔄 Supported Conversions

### Temperature

| Option | Conversion           |
| ------ | -------------------- |
| 1      | Celsius → Fahrenheit |
| 2      | Fahrenheit → Celsius |

### Length

| Option | Conversion          |
| ------ | ------------------- |
| 3      | Meters → Kilometers |
| 4      | Kilometers → Meters |

### Weight

| Option | Conversion        |
| ------ | ----------------- |
| 5      | Kilograms → Grams |
| 6      | Grams → Kilograms |

---

## 🧠 Concepts Used

The project uses basic Python concepts:

* Variables
* Numbers
* Type Casting
* Operators
* User Input
* Conditional Statements
* Loops

The input value is converted to `float` so the program can work with decimal values:

```python
value = float(input("Enter value: "))
```

---

## ⚙️ How It Works

The program first displays the conversion menu:

```text
1. Celsius → Fahrenheit
2. Fahrenheit → Celsius
3. Meters → Kilometers
4. Kilometers → Meters
5. Kilograms → Grams
6. Grams → Kilograms
```

The user chooses an option and enters a value.

The program then uses `if` / `elif` statements to select the correct conversion.

For example:

```python
if choice == "1":
    result = (value * 9/5) + 32
```

The result is then displayed to the user.

After each conversion, the program asks whether the user wants to perform another conversion.

---

## 📂 Project Structure

```text
python-unit-converter/

│
├── README.md
│
└── main.py
```

---

## ▶️ How to Run

Check that Python is installed:

```bash
python --version
```

Then run:

```bash
python main.py
```

---

## 💻 Example

```text
=================================
       UNIT CONVERTER
=================================

1. Celsius → Fahrenheit
2. Fahrenheit → Celsius
3. Meters → Kilometers
4. Kilometers → Meters
5. Kilograms → Grams
6. Grams → Kilograms

choose from the following options: 1

Enter value: 25

Result: 77.0 Fahrenheit

Do you want to perform another conversion? (yes/no): no

thank you for using the Unit Converter. Goodbye!
```

---

## 🎁 Bonus

The bonus requirement is to allow the user to perform multiple conversions during the same program execution.

This is implemented using:

```python
while True:
```

After every conversion, the program asks:

```text
Do you want to perform another conversion? (yes/no):
```

If the user enters anything other than `yes`, the program exits.

---

## 🚀 Future Improvements

Possible improvements:

* Validate the selected menu option.
* Validate the entered value.
* Add more temperature units.
* Add more length units.
* Add more weight units.
* Improve the menu design.
* Separate conversion logic into functions.
* Add more conversion categories.

---

<a id="arabic"></a>

# 🇪🇬 العربية

## 📌 نبذة عن المشروع

**Unit Converter CLI** هو مشروع Python بسيط لتحويل القيم بين وحدات مختلفة.

البرنامج يدعم التحويل بين:

* Temperature
* Length
* Weight

يقوم المستخدم باختيار نوع التحويل، وإدخال القيمة، ثم يعرض البرنامج النتيجة.

---

## 🔄 التحويلات المدعومة

### Temperature

| الاختيار | التحويل              |
| -------- | -------------------- |
| 1        | Celsius → Fahrenheit |
| 2        | Fahrenheit → Celsius |

### Length

| الاختيار | التحويل             |
| -------- | ------------------- |
| 3        | Meters → Kilometers |
| 4        | Kilometers → Meters |

### Weight

| الاختيار | التحويل           |
| -------- | ----------------- |
| 5        | Kilograms → Grams |
| 6        | Grams → Kilograms |

---

## 🧠 المفاهيم المستخدمة

المشروع يستخدم مجموعة من مفاهيم Python الأساسية:

* Variables
* Numbers
* Type Casting
* Operators
* User Input
* Conditional Statements
* Loops

يتم تحويل القيمة المدخلة إلى `float` حتى يستطيع البرنامج التعامل مع الأرقام العشرية:

```python
value = float(input("Enter value: "))
```

---

## ⚙️ كيف يعمل المشروع

في البداية يعرض البرنامج قائمة التحويلات:

```text
1. Celsius → Fahrenheit
2. Fahrenheit → Celsius
3. Meters → Kilometers
4. Kilometers → Meters
5. Kilograms → Grams
6. Grams → Kilograms
```

بعد ذلك يختار المستخدم عملية التحويل ويدخل القيمة.

يستخدم البرنامج `if` و`elif` لتحديد عملية التحويل المطلوبة.

مثال:

```python
if choice == "1":
    result = (value * 9/5) + 32
```

ثم يتم عرض النتيجة للمستخدم.

بعد الانتهاء من عملية التحويل، يسأل البرنامج المستخدم إذا كان يريد إجراء عملية تحويل أخرى.

---

## 📂 هيكل المشروع

```text
python-unit-converter/

│
├── README.md
│
└── main.py
```

---

## ▶️ تشغيل المشروع

تأكد من تثبيت Python:

```bash
python --version
```

ثم قم بتشغيل البرنامج:

```bash
python main.py
```

---

## 💻 مثال

```text
=================================
       UNIT CONVERTER
=================================

1. Celsius → Fahrenheit
2. Fahrenheit → Celsius
3. Meters → Kilometers
4. Kilometers → Meters
5. Kilograms → Grams
6. Grams → Kilograms

choose from the following options: 1

Enter value: 25

Result: 77.0 Fahrenheit

Do you want to perform another conversion? (yes/no): no

thank you for using the Unit Converter. Goodbye!
```

---

## 🎁 Bonus

المطلوب الإضافي في المشروع هو السماح للمستخدم بتنفيذ أكثر من عملية تحويل في نفس تشغيل البرنامج.

تم تنفيذ ذلك باستخدام:

```python
while True:
```

بعد كل عملية تحويل، يسأل البرنامج:

```text
Do you want to perform another conversion? (yes/no):
```

إذا أدخل المستخدم أي قيمة غير `yes`، يتم إنهاء البرنامج.

---

## 🚀 تحسينات مستقبلية

يمكن تطوير المشروع مستقبلًا من خلال:

* التحقق من اختيار المستخدم من القائمة.
* التحقق من القيمة المدخلة.
* إضافة وحدات أخرى لدرجة الحرارة.
* إضافة وحدات أخرى للطول.
* إضافة وحدات أخرى للوزن.
* تحسين شكل الـ Menu.
* تقسيم عمليات التحويل إلى Functions.
* إضافة تصنيفات تحويل جديدة.
