# 🔐 Password Strength Checker | فاحص قوة كلمة المرور

A lightweight and interactive Python command-line tool designed to evaluate the strength of passwords based on standard security rules.

أداة سطر أوامر بسيطة وتفاعلية بلغة بايثون، صُممت لفحص وتحديد مدى قوة كلمات المرور بناءً على معايير أمان محددة.

---

## 📑 Table of Contents | جدول المحتويات

* [Project Overview](#project-overview)
* [Supported Conversions](#supported-conversions)
* [Concepts Used](#concepts-used)
* [How It Works](#how-it-works)
* [Project Structure](#project-structure)
* [How to Run](#how-to-run)
* [Example](#example)
* [Bonus](#bonus)
* [Future Improvements](#future-improvements)

---

## Project Overview

**English:**  
The **Password Strength Checker** is an interactive CLI application that tests user passwords against core security criteria (length, letters, digits, and symbols). It provides immediate feedback to help users build stronger, safer credentials.

**العربية:**  
**فاحص قوة كلمة المرور** هو تطبيق تفاعلي يعمل عبر شاشة الأوامر (CLI) لاختبار كلمات مرور المستخدم ومطابقتها لمعايير الأمان الأساسية (الطول، الحروف، الأرقام، والرموز الخاصة). يوفر البرنامج للمستخدم نتيجة فورية لمساعدته في إنشاء كلمات مرور آمنة.

---

## Supported Conversions

*(Criteria & Strength Classifications | معايير التقييم والتحويل)*
**English:**  
The application evaluates raw input text and classifies/converts it into security ratings based on the following criteria:

* **Length Check:** Minimum 8 characters.
* **Uppercase Check:** At least one capital letter (`A-Z`).
* **Lowercase Check:** At least one small letter (`a-z`).
* **Numeric Check:** At least one digit (`0-9`).
* **Special Character Check:** At least one symbol from `!@#$%^&*()-+`.
* **Output Classification:** `WEAK` (fails one or more criteria) ➔ `STRONG` (passes all criteria).

**العربية:**  
يقوم البرنامج بتحليل ومعالجة النص المدخل وتحويله إلى تصنيف أمان محدد وفقاً للمعايير التالية:

* **فحص الطول:** لا يقل عن 8 خانات.
* **فحص الحروف الكبيرة:** يحتوي على حرف كبير واحد على الأقل (`A-Z`).
* **فحص الحروف الصغيرة:** يحتوي على حرف صغير واحد على الأقل (`a-z`).
* **فحص الأرقام:** يحتوي على رقم واحد على الأقل (`0-9`).
* **فحص الرموز:** يحتوي على رمز خاص واحد على الأقل من القائمة `!@#$%^&*()-+`.
* **تحويل الحالة:** `WEAK` (ضعيف في حال فشل أي معيار) ➔ `STRONG` (قوي عند تحقيق كل المعايير).

---

## Concepts Used

**English:**  
* **Strings & String Methods:** `.isupper()`, `.islower()`, `.isdigit()`, `.lower()`.
* **Control Flow:** `while` loop, `if-elif-else` conditional branching, and `break` / `continue`.
* **Boolean Logic & Generators:** Built-in `any()` function combined with generator expressions for character verification.
* **User Input & Formatting:** `input()` prompts and formatted text outputs.

**العربية:**  
* **السلاسل النصية والدوال التابعة لها:** `.isupper()`، `.islower()`، `.isdigit()`، `.lower()`.
* **التحكم في المسار:** حلقات التكرار `while`، الجمل الشرطية `if-elif-else`، وأوامر التحكم `break` و `continue`.
* **المنطق البولياني (Booleans) والتكرار المولد:** استخدام دالة `any()` للتحقق من أنواع الرموز في السلسلة.
* **استقبال المدخلات والتنسيق:** دالة `input()` لطلب البيانات وتنسيق المخرجات بالطباعة.

---

## How It Works

**English:**  

1. The program greets the user and displays the security criteria.
2. The user enters a password in an interactive loop.
3. The script checks each condition sequentially:

   - If a rule is violated, the loop outputs `Strength: WEAK`, specifies the problem, and asks again.
   - If all rules are satisfied, it prints `Strength: STRONG` alongside a full breakdown of the criteria.

4. The user is prompted to decide whether to check another password or exit the program.

**العربية:**  

1. يعرض البرنامج رسالة ترحيبية تشرح معايير قوة كلمة المرور.
2. يُدخل المستخدم كلمة المرور داخل حلقة تكرارية تفاعلية.
3. يتم فحص الشروط بالترتيب:
   - إذا لم يتحقق أحد الشروط، يطبع البرنامج `Strength: WEAK` مع توضيح سبب الضعف، ثم يطلب المحاولة مجدداً.
   - إذا تحققت جميع الشروط، يتم عرض `Strength: STRONG` مع تقرير تفصيلي بكل معيار.
4. يُسأل المستخدم عما إذا كان يريد تجربة كلمة مرور أخرى أو إنهاء البرنامج.

---

## Project Structure

```text
python-password-strength-checker/
│
├── main.py          # The core Python script containing the checker logic
└── README.md        # Documentation in Arabic and English
```

---

## How to Run

**English:**  

1. Make sure you have **Python 3.x** installed.
2. Clone this repository or download the files:

   ```bash
   git clone https://github.com/your-username/python-password-strength-checker.git
   cd python-password-strength-checker
   ```

3. Run the script:

   ```bash
   python main.py
   ```

**العربية:**  

1. تأكد من تثبيت **Python 3.x** على جهازك.
2. قم باستنساخ المستودع أو تحميل الملفات:

   ```bash
   git clone https://github.com/your-username/python-password-strength-checker.git
   cd python-password-strength-checker
   ```

3. شغّل البرنامج:

   ```bash
   python main.py
   ```

---

## Example

### 1. Weak Password Case | كلمة مرور ضعيفة:

```text
=================================
        PASSWORD STRENGTH CHECKER
=================================

Enter your password: password123
Strength: WEAK
Problems:
- Password must contain at least one uppercase letter
```

### 2. Strong Password Case | كلمة مرور قوية:

```text
Enter your password: Mostafa@2026!
Strength: STRONG
Length             : 13
Uppercase          : True
Lowercase          : True
Numbers            : True
Special Characters : True

Do you want to test another password? (yes/no): no
thank you for using the Password Strength Checker. Goodbye!
```

---

## Bonus

**English:**  

* **Feedback on Weak Passwords:** Rather than just returning "Invalid", the script clearly informs the user about the exact reason why their password failed (e.g., missing numbers, missing special characters, or short length).
* **Detailed Breakdown:** Strong passwords display a confirmation report showing `True` for each evaluated parameter.

**العربية:**  

* **توضيح أسباب الضعف:** بدلاً من مجرد رفض الإدخال، يوضح البرنامج للمستخدم السبب الدقيق لضعف كلمة المرور (مثل: نقص الأرقام، قصر الطول، أو عدم وجود رمز خاص).
* **تقرير تفصيلي:** عند إدخال كلمة مرور قوية، يتم عرض تقرير يوضح نجاح كل معيار بقيمة `True`.

---

## Future Improvements

**English:**  

* [ ] Add a multi-level scoring system (`VERY WEAK`, `WEAK`, `MEDIUM`, `STRONG`, `VERY STRONG`).
* [ ] Collect and display all failure reasons at once instead of failing on the first error.
* [ ] Implement a built-in secure password generator.
* [ ] Build a Graphical User Interface (GUI) using Tkinter or CustomTkinter.

**العربية:**  

* [ ] إضافة نظام تقييم متعدد المستويات (`ضعيف جداً`، `ضعيف`، `متوسط`، `قوي`، `خارق`).
* [ ] تجميع وعرض جميع المشاكل معاً دفعة واحدة بدلاً من التوقف عند أول مشكلة.
* [ ] إضافة ميزة توليد كلمات مرور قوية تلقائياً للمستخدم.
* [ ] بناء واجهة رسومية (GUI) باستخدام مكتبة Tkinter أو CustomTkinter.
