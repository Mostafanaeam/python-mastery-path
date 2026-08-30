# النصوص

تُحاط السلاسل النصية في لغة بايثون إما بعلامات اقتباس مفردة أو علامات اقتباس مزدوجة.

## اقتباسات من داخل الاقتباسات

يمكنك استخدام علامات الاقتباس داخل سلسلة نصية، طالما أنها لا تتطابق مع علامات الاقتباس المحيطة بالسلسلة النصية.

## إسناد سلسلة نصية إلى متغير

يتم إسناد سلسلة نصية إلى متغير عن طريق كتابة اسم المتغير متبوعًا بعلامة يساوي ثم السلسلة النصية.

## سلاسل متعددة الأسطر

يمكنك إسناد سلسلة نصية متعددة الأسطر إلى متغير باستخدام ثلاث علامات اقتباس.

## السلاسل النصية في مصفوفات

كما هو الحال في العديد من لغات البرمجة الشائعة الأخرى، تُعرَّف السلاسل النصية في بايثون على أنها مصفوفات من أحرف يونيكود.

مع ذلك، لا يوجد في بايثون نوع بيانات حرفي، فالحرف الواحد عبارة عن سلسلة نصية طولها 1.

يمكن استخدام الأقواس المربعة للوصول إلى عناصر السلسلة النصية.

## التكرار عبر النصوص

بما أن السلاسل النصية عبارة عن مصفوفات، فيمكننا المرور على الأحرف في السلسلة النصية باستخدام حلقة for.

## طول السلسلة النصية

أي عدد الحروف أو الرموز التي تتكون منها الكلمة أو الجملة

## فحص السلسلة النصية

هو التحقق من حالة أو محتوى نص معين للتأكد من أنه يطابق شروطاً محددة قبل اتخاذ خطوة أخرى في الكود.لا توجد دالة موحدة في البرمجة باسم "Check String"، بل هو مفهوم عام يشمل عمليات فحص متعددة.

## التشريح أو التقطيع في النصوص

استخراج جزء محدد من سلسلة بيانات (مثل القوائم أو النصوص) دون تعديل البيانات الأصلية.

#  تنسيق أو ترتيب النصوص

هو عملية دمج المتغيرات والقيم داخل النص (سلسلة الحروف) بطريقة منظمة وسهلة القراءة


## Escape Characters in Python

The table below lists common escape characters in Python, along with their functions and Arabic translations:

| Code | Result / Description | Arabic Translation |
| :--- | :--- | :--- |
| `\'` | Single Quote | علامة تنصيص فردية |
| `\\` | Backslash | شرطة مائلة للخلف |
| `\n` | New Line | سطر جديد |
| `\r` | Carriage Return | إرجاع المؤشر لبداية السطر |
| `\t` | Tab | مسافة بادئة (تاب) |
| `\b` | Backspace | مسح الحرف السابق |
| `\f` | Form Feed | الانتقال للصفحة التالية |
| `\ooo` | Octal value | قيمة بالنظام الثماني |
| `\xhh` | Hex value | قيمة بالنظام السداسي عشر |   


## Python String Methods

> **Note:** All string methods return new values. They do not change the original string.

| Method | Description | Arabic Translation |
| :--- | :--- | :--- |
| `capitalize()` | Converts the first character to upper case | تحويل الحرف الأول إلى حرف كبير |
| `casefold()` | Converts string into lower case | تحويل النص إلى حروف صغيرة (أقوى من lower) |
| `center()` | Returns a centered string | إرجاع نص في المنتصف |
| `count()` | Returns the number of times a specified value occurs in a string | حساب عدد تكرار قيمة محددة |
| `encode()` | Returns an encoded version of the string | إرجاع نسخة مشفرة من النص |
| `endswith()` | Returns true if the string ends with the specified value | التحقق إذا كان النص ينتهي بقيمة معينة |
| `expandtabs()` | Sets the tab size of the string | تحديد حجم المسافة البادئة (`Tab`) |
| `find()` | Searches the string for a specified value and returns the position | البحث عن قيمة وإرجاع موقعها |
| `format()` | Formats specified values in a string | تنسيق القيم داخل النص |
| `format_map()` | Formats specified values in a string | تنسيق القيم باستخدام قاموس (`Dictionary`) |
| `index()` | Searches the string for a specified value and returns the position | البحث عن قيمة وإرجاع موقعها (يرفع خطأ إن لم توجد) |
| `isalnum()` | Returns True if all characters in the string are alphanumeric | التحقق إذا كانت الحروف أبجدية رقمية |
| `isalpha()` | Returns True if all characters in the string are in the alphabet | التحقق إذا كانت الحروف أبجدية فقط |
| `isascii()` | Returns True if all characters in the string are ascii characters | التحقق إذا كانت الحروف من نطاق `ASCII` |
| `isdecimal()` | Returns True if all characters in the string are decimals | التحقق إذا كانت الحروف أرقاماً عشرية |
| `isdigit()` | Returns True if all characters in the string are digits | التحقق إذا كانت الحروف أرقاماً |
| `isidentifier()` | Returns True if the string is an identifier | التحقق إذا كان النص اسماً صالحاً لمتغير |
| `islower()` | Returns True if all characters in the string are lower case | التحقق إذا كانت الحروف كلها صغيرة |
| `isnumeric()` | Returns True if all characters in the string are numeric | التحقق إذا كانت الحروف ذات قيمة عددية |
| `isprintable()` | Returns True if all characters in the string are printable | التحقق إذا كان النص قابلاً للطباعة |
| `isspace()` | Returns True if all characters in the string are whitespaces | التحقق إذا كان النص عبارة عن مسافات |
| `istitle()` | Returns True if the string follows the rules of a title | التحقق إذا كان النص بصيغة عنوان |
| `isupper()` | Returns True if all characters in the string are upper case | التحقق إذا كانت الحروف كلها كبيرة |
| `join()` | Joins the elements of an iterable to the end of the string | دمج عناصر تكرار باستخدام النص كفاصل |
| `ljust()` | Returns a left justified version of the string | إرجاع نص بمحاذاة اليسار |
| `lower()` | Converts a string into lower case | تحويل النص إلى حروف صغيرة |
| `lstrip()` | Returns a left trim version of the string | إزالة المسافات من اليسار |
| `maketrans()` | Returns a translation table to be used in translations | إنشاء جدول ترجمة |
| `partition()` | Returns a tuple where the string is parted into three parts | تقسم النص إلى ثلاثة أجزاء (`Tuple`) |
| `replace()` | Returns a string where a specified value is replaced with a specified value | استبدال قيمة بأخرى |
| `rfind()` | Searches the string for a specified value and returns the last position | البحث عن قيمة من اليمين وإرجاع آخر موقع |
| `rindex()` | Searches the string for a specified value and returns the last position | البحث عن قيمة من اليمين (يرفع خطأ إن لم توجد) |
| `rjust()` | Returns a right justified version of the string | إرجاع نص بمحاذاة اليمين |
| `rpartition()` | Returns a tuple where the string is parted into three parts | تقسم النص إلى ثلاثة أجزاء من اليمين |
| `rsplit()` | Splits the string at the specified separator, and returns a list | تقسيم النص من اليمين وإرجاع قائمة |
| `rstrip()` | Returns a right trim version of the string | إزالة المسافات من اليمين |
| `split()` | Splits the string at the specified separator, and returns a list | تقسيم النص بناءً على فاصل وإرجاع قائمة |
| `splitlines()` | Splits the string at line breaks and returns a list | تقسيم النص عند الأسطر الجديدة وإرجاع قائمة |
| `startswith()` | Returns true if the string starts with the specified value | التحقق إذا كان النص يبدأ بقيمة معينة |
| `strip()` | Returns a trimmed version of the string | إزالة المسافات من الطرفين |
| `swapcase()` | Swaps cases, lower case becomes upper case and vice versa | عكس حالة الحروف (كبير لصغير والعكس) |
| `title()` | Converts the first character of each word to upper case | تحويل الحرف الأول من كل كلمة إلى كبير |
| `translate()` | Returns a translated string | إرجاع نص مترجم/مستبدل الأحرف |
| `upper()` | Converts a string into upper case | تحويل النص إلى حروف كبيرة |
| `zfill()` | Fills the string with a specified number of 0 values at the beginning | ملء النص بأصفار في البداية للوصول لطول معين |

====================================

# مصطلحات برمجية :-

| الكلمة | المعني |
| :-------- | :------------------------- |
| `` |  |
| `` | نوع من بيانات الحاسوب يُستخدم لتمثيل الأعداد التي تحتوي على كسور أو أجزاء عشرية |
| `` | تُكتب الأعداد المركبة باستخدام الحرف "j" كجزء تخيلي |


============================
### المصدر:-

- [Python Strings with w3schools](https://www.w3schools.com/python/python_strings.asp)
- [Python - Slicing Strings with w3schools](https://www.w3schools.com/python/python_strings_slicing.asp)
- [Python - Modify Strings with w3schools](https://www.w3schools.com/python/python_strings_modify.asp)
- [Python - String Concatenation with w3schools](https://www.w3schools.com/python/python_strings_concatenate.asp)
- [Python - Format - Strings with w3schools](https://www.w3schools.com/python/python_strings_concatenate.asp)
- [Python - Escape Characters with w3schools](https://www.w3schools.com/python/python_strings_escape.asp)
- [Python - String Methods with w3schools](https://www.w3schools.com/python/python_strings_methods.asp)


