# 📊 Text Analyzer | محلل النصوص

A versatile Python command-line application that analyzes user-provided text and generates a comprehensive breakdown of characters, words, cases, length extremes, and word frequencies.

أداة سطر أوامر تفاعلية بلغة بايثون تقوم بتحليل النصوص بدقة، وتقديم إحصائيات تفصيلية تشمل عدد الحروف، الكلمات، المسافات، حالة الأحرف، أطول وأقصر كلمة، بالإضافة إلى أكثر الكلمات تكراراً.

---

## 📑 Table of Contents | جدول المحتويات

* [Project Overview](#project-overview)
* [Supported Conversions](#supported-conversions)
* [Concepts Used](#concepts-used)
* [How It Works](#how-it-works)
* [Deep Dive: Most Frequent Words Explanation](#deep-dive-most-frequent-words-explanation)
* [Project Structure](#project-structure)
* [How to Run](#how-to-run)
* [Example](#example)
* [Bonus](#bonus)
* [Future Improvements](#future-improvements)

---

## Project Overview

**English:**  
The **Text Analyzer** inspects any input text and extracts valuable linguistic and statistical data. It verifies whether text was actually provided, parses character-level and word-level information, identifies extremes (longest and shortest words), and ranks word occurrences.

**العربية:**  
يقوم مشروع **محلل النصوص** بمعالجة أي نص يُدخله المستخدم واستخراج بيانات إحصائية ولغوية شاملة عنه. يتحقق البرنامج أولاً من صحة المدخلات، ثم يفحص تفاصيل الحروف والكلمات وحالاتها، ويستخرج أطول وأقصر كلمة، ويحسب الكلمات الأكثر تكراراً.

---

## Supported Conversions

*(Analyzed Metrics & Classifications | المقاييس والتحليلات المدعومة)*
**English:**  
The tool transforms raw input strings into the following structured statistical metrics:

* **Characters:** Total character count including punctuation and spaces.
* **Words:** Total count of whitespace-separated tokens.
* **Spaces:** Total number of single whitespace characters.
* **Numbers:** Total count of numeric digits (`0-9`).
* **Uppercase Letters:** Total count of capital letters (`A-Z`).
* **Lowercase Letters:** Total count of small letters (`a-z`).
* **Longest Word:** The word with the maximum character length.
* **Shortest Word:** The word with the minimum character length.
* **Top 5 Frequent Words:** Ranked frequency list of unique words.

**العربية:**  
يقوم البرنامج بتحويل النص الخام إلى تقرير إحصائي منظم يشمل:

* **عدد الحروف (Characters):** إجمالي عدد الخانات بما فيها الرموز والمسافات.
* **عدد الكلمات (Words):** عدد الكلمات المفصولة بمسافات.
* **عدد المسافات (Spaces):** عدد المسافات البيضاء.
* **عدد الأرقام (Numbers):** عدد الأرقام والرموز العددية (`0-9`).
* **الحروف الكبيرة (Uppercase):** عدد الأحرف الكبيرة (`A-Z`).
* **الحروف الصغيرة (Lowercase):** عدد الأحرف الصغيرة (`a-z`).
* **أطول كلمة (Longest Word):** الكلمة التي تحتوي على أكبر عدد أحرف.
* **أقصر كلمة (Shortest Word):** الكلمة التي تحتوي على أقل عدد أحرف.
* **أكثر 5 كلمات تكراراً (Top 5 Frequent Words):** ترتيب الكلمات الأكثر ظهوراً في النص.

---

## Concepts Used

**English:**

* **String Methods:** `.split()`, `.count()`, `.isspace()`, `.isdigit()`, `.isupper()`, `.islower()`.
* **Data Structures:** Lists (`list`), Sets (`set`), and Tuples (`tuple`).
* **Higher-Order & Built-in Functions:** `len()`, `sum()`, `max()`, `min()`, `sorted()`.
* **Functional Programming:** Lambda expressions (`lambda`), generator expressions, and key-based sorting.
* **Control Flow:** `while` loops, input validation, and conditional statements.

**العربية:**  

* **دوال النصوص (String Methods):** `.split()`، `.count()`، `.isspace()`، `.isdigit()`، `.isupper()`، `.islower()`.
* **هياكل البيانات:** القوائم (`list`)، المجموعات غير المكررة (`set`)، والأزواج المرتبة (`tuple`).
* **الدوال المدمجة:** `len()`، `sum()`، `max()`، `min()`، `sorted()`.
* **البرمجة الوظيفية:** الدوال المجهولة (`lambda`)، التكرار المولد (Generator expressions)، والترتيب المخصص (`key`).
* **التحكم في المسار:** حلقة التكرار `while`، التحقق من صحة المدخلات، والجمل الشرطية.

---

## How It Works

**English:**

1. **Validation Loop:** Prompts the user for text and checks if the entry is empty, contains only spaces, or is null.
2. **Text Metrics Calculation:** Uses string inspection methods alongside generators to count characters, spaces, uppercase, lowercase, and digits.
3. **Word Boundaries Evaluation:** Splits the text into a list of words to compute word count, and uses `max()` and `min()` with `key=len` to find length extremes.
4. **Frequency Ranking:** Leverages a lambda function combining sets, counting, and descending sorting to extract the top 5 most repeated words.

**العربية:**  

1. **التحقق من الإدخال:** يطلب البرنامج نصاً من المستخدم ويتأكد أنه ليس فارغاً أو يحتوي فقط على مسافات.
2. **حساب الإحصائيات:** يتم استخدام دوال السلاسل النصية ومولدات التكرار لعد الحروف، المسافات، الأرقام، وحالات الأحرف.
3. **تحليل الكلمات:** يتم تقسيم النص إلى قائمة كلمات، ثم تحديد أطول وأقصر كلمة بواسطة دالتي `max()` و `min()` مع تمرير معامل الطول `key=len`.
4. **حساب الكلمات الأكثر تكراراً:** يتم تطبيق دالة `lambda` تجمع بين المجموعات الفريدة والفرز التنازلي لاستخراج أكثر 5 كلمات تكراراً.

---

## Deep Dive: Most Frequent Words Explanation

*(شرح تفصيلي لكود استخراج أكثر الكلمات تكراراً)*

```python
most_frequent_words = lambda text: sorted(
    ((word, text.split().count(word)) for word in set(text.split())),
    key=lambda x: x[1],
    reverse=True
)[:5]

print(f"Most Frequent Words: {most_frequent_words(text)}")
```

### 🇬🇧 English Explanation (Step-by-Step)

1. **`lambda text:`**  
   Creates an anonymous inline function taking the raw string `text` as its parameter.

2. **`text.split()`**  
   Breaks down the text into a list of individual words by splitting on whitespaces.  
   *Example:* `"a b a"` becomes `['a', 'b', 'a']`.

3. **`set(text.split())`**  
   Converts the list into a `set` to eliminate duplicates. This ensures that each word is processed and counted **only once**.  
   *Example:* `set(['a', 'b', 'a'])` becomes `{'a', 'b'}`.

4. **`((word, text.split().count(word)) for word in set(text.split()))`**  
   A generator expression that iterates over every unique word from the set and constructs a tuple:  
   `(word, count_of_that_word_in_original_list)`.  
   *Example:* Yields `('a', 2)` and `('b', 1)`.

5. **`sorted(..., key=lambda x: x[1], reverse=True)`**  
   * `key=lambda x: x[1]`: Instructs Python to sort the tuples by their **second element** (the frequency count `x[1]`) instead of the word string (`x[0]`).  
   * `reverse=True`: Sorts descending from the highest count to the lowest count.

6. **`[:5]` (Slicing)**  
   Takes only the first 5 elements from the sorted list, effectively returning the top 5 most repeated words.

---

### 🇸🇦 الشرح باللغة العربية (خطوة بخطوة)

1. **`lambda text:`**  
   دالة مجهولة الاسم (Anonymous Function) تستقبل المتغير `text` (النص الأصلي) كمدخل لها.

2. **`text.split()`**  
   تقوم بتقسيم النص إلى قائمة من الكلمات بالاعتماد على المسافات بينها.  
   *مثال:* `"Python is easy and Python"` تتحول إلى `['Python', 'is', 'easy', 'and', 'Python']`.

3. **`set(text.split())`**  
   تحويل قائمة الكلمات إلى مجموعة (`set`) لإزالة أي تكرار. الفائدة هنا هي ضمان حساب تكرار كل كلمة **مرة واحدة فقط** وتجنب العمليات المكررة.  
   *مثال:* تتحول القائمة السابقة إلى `{'Python', 'is', 'easy', 'and'}`.

4. **`((word, text.split().count(word)) for word in set(text.split()))`**  
   مولد تعبيري (Generator Expression) يمر على كل كلمة فريدة، وينشئ زوجاً مرتباً (`tuple`) يحتوي على:  
   `(الكلمة, عدد مرات ظهورها في القائمة الأصلية)`.  
   *مثال:* سينتج `('Python', 2)` و `('is', 1)`.

5. **`sorted(..., key=lambda x: x[1], reverse=True)`**  
   * `key=lambda x: x[1]`: يخبر دالة الترتيب أن تعتمد على **العنصر الثاني** في الزوج وهو (الرقم أو عدد مرات التكرار) وليس على الكلمة نفسها.  
   * `reverse=True`: يجعل الترتيب **تنازلياً** من الأكثر تكراراً إلى الأقل تكراراً.

6. **`[:5]` (التقطيع - Slicing)**  
   اقتطاع أول 5 عناصر فقط من القائمة بعد ترتيبها، مما يعطينا أعلى 5 كلمات تكراراً في النص.

---

## Project Structure

```text
python-text-analyzer/
│
├── main.py          # Main application containing text analysis logic
└── README.md        # Comprehensive documentation (Arabic & English)
```

---

## How to Run

**English:**  

1. Ensure **Python 3.x** is installed.
2. Clone this repository:

   ```bash
   git clone https://github.com/your-username/python-text-analyzer.git
   cd python-text-analyzer
   ```

3. Run the script:

   ```bash
   python main.py
   ```

**العربية:**  

1. تأكد من تثبيت **Python 3.x**.
2. استنسخ المستودع:

   ```bash
   git clone https://github.com/your-username/python-text-analyzer.git
   cd python-text-analyzer
   ```

3. شغّل البرنامج:

   ```bash
   python main.py
   ```

---

## Example

### Input

```text
Python is easy and Python is powerful
```

### Output

```text
Characters : 37
Words      : 7
Spaces     : 6
Numbers    : 0
Uppercase  : 2
Lowercase  : 29

Longest Word : powerful
Shortest Word: is

Most Frequent Words: [('Python', 2), ('is', 2), ('easy', 1), ('and', 1), ('powerful', 1)]
```

---

## Bonus

**English:**  

* **Top 5 Word Frequency:** Automatically extracts and ranks the 5 most frequent words in descending order using advanced functional sorting.
* **Input Validation:** Prevents crashes and accidental inputs by verifying that empty lines or pure whitespace are rejected.

**العربية:**  

* **أكثر 5 كلمات تكراراً:** استخراج وترتيب أعلى 5 كلمات ظهوراً ترتيباً تنازلياً عبر تقنيات برمجية وظيفية متقدمة.
* **التحقق من صحة المدخلات:** منع حدوث أخطاء عن طريق رفض النصوص الفارغة أو المسافات دون توقف البرنامج.

---

## Future Improvements

**English:**  

- [ ] Ignore punctuation marks using the `string.punctuation` module.
- [ ] Implement case-insensitive matching (`.lower()`) so `"Python"` and `"python"` count as the same word.
- [ ] Exclude common stopwords (e.g., *is, and, the, a*).
- [ ] Format the most frequent words as a clean numbered list in the console.

**العربية:**

- [ ] تجاهل علامات الترقيم عند عد الكلمات باستخدام مكتبة `string.punctuation`.
- [ ] جعل مقارنة الكلمات غير حساسة لحالة الأحرف (بحيث تُعامل `"Python"` و `"python"` ككلمة واحدة).
- [ ] تصفية واستبعاد الكلمات الشائعة (Stopwords) مثل حروف الجر والعطف.
- [ ] تنسيق مخرجات الكلمات الأكثر تكراراً في قائمة مرقمة وأنيقة داخل شاشة الأوامر.
