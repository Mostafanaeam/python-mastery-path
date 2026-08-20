# Python Quickstart

قبل ما نبدأ كتابة أول كود Python، لازم نجهز بيئة العمل بشكل صحيح وننظم ملفات المشاريع من البداية.

---

## 1. تثبيت Python

### تحميل Python

يمكنك تحميل Python من الموقع الرسمي:

https://www.python.org/downloads/

بعد فتح الموقع، حمّل أحدث إصدار من **Python 3** المناسب لنظام التشغيل الخاص بك.

> في هذا المستودع سنستخدم Python 3.

### تثبيت Python على Windows

بعد تحميل ملف التثبيت:

1. افتح ملف التثبيت.
2. في أول شاشة، فعّل الخيار:

```text
Add python.exe to PATH
```

3. اضغط:

```text
Install Now
```

4. انتظر حتى ينتهي التثبيت.
5. اضغط `Close`.

### التأكد من تثبيت Python

افتح **Command Prompt** أو **PowerShell** واكتب:

```bash
python --version
```

أو:

```bash
python -V
```

إذا كان التثبيت صحيحًا، ستظهر نسخة Python المثبتة، مثل:

```text
Python 3.x.x
```

يمكنك أيضًا تجربة تشغيل Python مباشرة:

```bash
python
```

إذا ظهر شيء مشابه لـ:

```text
>>>
```

فهذا يعني أن Python Interpreter يعمل بشكل صحيح.

لإغلاق الـ Interpreter:

```python
exit()
```

---

# 2. تنظيم مشاريع Python

من البداية، لا تضع كل ملفات Python في أماكن عشوائية.

أنشئ **مجلدًا رئيسيًا خاصًا بكل مشاريع وتاسكات Python**، وجميع مشاريعك وتدريباتك تكون بداخله.

مثال:

```text
D:\
└── Python\
    ├── projects\
    ├── tasks\
    ├── exercises\
    ├── experiments\
    └── notes\
```

أو يمكن أن يكون التنظيم أبسط:

```text
D:\
└── Python\
    ├── project-01\
    ├── project-02\
    ├── task-01\
    ├── task-02\
    └── exercises\
```

### لماذا ننظم الملفات بهذه الطريقة؟

لأن التنظيم من البداية يجعل الوصول إلى مشاريعك أسهل، ويمنع انتشار ملفات Python في أماكن مختلفة على جهازك.

والأهم: **لا تجعل كل ملفات Python الخاصة بك داخل مجلد واحد بدون تنظيم**.

---

## 3. أين أضع مجلد Python؟

يمكنك وضع مجلد المشاريع على أي Partition مناسب.

مثال:

```text
D:\Python
```

إذا كان لديك Partition مثل `D:` مخصص للبيانات والمشاريع، فهذا تنظيم جيد.

### ملاحظة مهمة

ليس من الضروري تثبيت Python أو VS Code على Partition غير `C:`.

يمكن أن يكون:

```text
Python → C:
VS Code → C:
Projects → D:
```

وهذا طبيعي تمامًا.

الفكرة الأساسية هي الفصل بين:

```text
Applications
    ↓
Python
VS Code

Projects / Data
    ↓
Python Projects
```

وبالتالي، إذا احتجت إلى إعادة تثبيت Windows مستقبلًا، تكون ملفات مشاريعك على Partition مستقل عن نظام التشغيل.

---

# 4. تثبيت Visual Studio Code

سنستخدم **Visual Studio Code (VS Code)** لكتابة وتشغيل كود Python.

### تحميل VS Code

يمكنك تحميل VS Code من الموقع الرسمي:

https://code.visualstudio.com/

قم بتحميل النسخة المناسبة لنظام التشغيل الخاص بك.

### تثبيت VS Code على Windows

بعد تحميل ملف التثبيت:

1. افتح ملف التثبيت.
2. وافق على اتفاقية الاستخدام.
3. اختر مكان التثبيت.
4. اضغط `Next`.
5. أكمل خطوات التثبيت.
6. اضغط `Install`.
7. بعد انتهاء التثبيت اضغط `Finish`.

يمكنك تثبيت VS Code على `C:` بشكل طبيعي.

---

# 5. تشغيل VS Code

بعد تثبيت VS Code يمكنك تشغيله من:

```text
Start Menu
    ↓
Visual Studio Code
```

أو البحث عنه من Windows Search:

```text
VS Code
```

ثم تشغيل البرنامج.

---

# 6. فتح Folder معين داخل VS Code

أفضل طريقة للعمل على مشروع هي فتح **المجلد الخاص بالمشروع بالكامل** داخل VS Code، وليس فتح ملف Python منفردًا فقط.

مثلًا، إذا كان لديك:

```text
D:\Python\project-01
```

افتح VS Code ثم:

```text
File
    ↓
Open Folder
```

ثم اختر:

```text
D:\Python\project-01
```

واضغط:

```text
Select Folder
```

سيظهر المشروع داخل Explorer في الجانب الأيسر.

---

## 7. فتح Folder باستخدام Terminal

يمكنك أيضًا فتح مجلد مباشرة باستخدام Terminal.

انتقل أولًا إلى مجلد المشروع:

```bash
cd D:\Python\project-01
```

ثم اكتب:

```bash
code .
```

النقطة `.` تعني:

```text
Current Folder
```

وبالتالي:

```bash
code .
```

تعني:

> افتح المجلد الحالي باستخدام VS Code.

إذا ظهر أن الأمر `code` غير معروف، يمكنك فتح VS Code بالطريقة العادية ثم استخدام:

```text
File → Open Folder
```

---

# 8. إنشاء أول ملف Python

بعد فتح مجلد المشروع داخل VS Code:

1. من Explorer اضغط **New File**.
2. سمِّ الملف:

```text
main.py
```

3. اكتب:

```python
print("Hello, Python!")
```

4. احفظ الملف.

يمكنك تشغيله من Terminal باستخدام:

```bash
python main.py
```

ويجب أن يظهر:

```text
Hello, Python!
```

---

# 9. الشكل النهائي المقترح

في البداية حاول أن يكون عندك تنظيم مشابه:

```text
D:\
└── Python\
    ├── exercises\
    │   ├── exercise-01\
    │   ├── exercise-02\
    │   └── exercise-03\
    │
    ├── tasks\
    │   ├── task-01\
    │   └── task-02\
    │
    ├── projects\
    │   ├── project-01\
    │   └── project-02\
    │
    └── experiments\
```

كل مشروع أو Task له مجلده الخاص، وداخل كل مجلد توجد الملفات الخاصة به.

بهذه الطريقة تكون بيئة العمل منظمة من البداية، ويصبح من السهل لاحقًا استخدام Git وGitHub وإدارة المشاريع بشكل احترافي.

## 10. تثبيت إضافة Better Comments Next

لتنظيم وكتابة التعليقات داخل كود Python بشكل أوضح، يجب تثبيت إضافة **Better Comments Next** في VS Code.

الإضافة تساعدك على تمييز أنواع مختلفة من التعليقات، مثل:

* التنبيهات `Alert`
* المعلومات `Informational`
* المهام `TODO`
* وغيرها من أنواع التعليقات

### تثبيت الإضافة

يمكنك فتح صفحة الإضافة من خلال الرابط:

https://marketplace.visualstudio.com/items?itemName=EdwinHuiSH.better-comments-next

أو من داخل VS Code:

```text
Extensions
    ↓
Search
    ↓
Better Comments Next
```

ابحث عن:

```text
Better Comments Next
```

ثم ثبّت الإضافة المقدمة من:

```text
Edwin Xu
```

### لماذا نستخدمها؟

لأنها تجعل التعليقات داخل الكود أكثر وضوحًا، خصوصًا عندما يحتوي المشروع على عدد كبير من الملاحظات والمهام.

مثال:

```python
# TODO: Improve this function

# NOTE: This value comes from the database

# FIXME: This needs to be fixed

# IMPORTANT: Do not modify this value
```

استخدام هذه الطريقة يساعدك على قراءة الكود ومراجعة المهام والملاحظات بسرعة أكبر.
