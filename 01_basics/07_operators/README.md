# معاملات بايثون

هي الرموز أو الكلمات الخاصة التي تُستخدم لإجراء عمليات على المتغيرات والقيم

## Arithmetic Operators in Python

Arithmetic operators are used with numeric values to perform common mathematical operations:

| Operator | Name | Description | Example | Arabic Translation |
| :--- | :--- | :--- | :--- | :--- |
| `+` | Addition | Adds two values together | `x + y` | الجمع |
| `-` | Subtraction | Subtracts one value from another | `x - y` | الطرح |
| `*` | Multiplication | Multiplies two values | `x * y` | الضرب |
| `/` | Division | Divides left operand by right operand (always returns a float) | `x / y` | القسمة (ترجع ناتج عشري) |
| `%` | Modulus | Returns the remainder of division | `x % y` | باقي القسمة |
| `**` | Exponentiation | Raises the left operand to the power of the right operand | `x ** y` | الأس / القوة |
| `//` | Floor division | Divides and rounds down to the nearest whole integer | `x // y` | القسمة الصحيحة (تقريب لأقل عدد صحيح) |

## Assignment Operators in Python

Assignment operators are used to assign values to variables:

| Operator | Example | Same As | Description | Arabic Translation |
| :--- | :--- | :--- | :--- | :--- |
| `=` | `x = 5` | `x = 5` | Assigns value to variable | إسناد قيمة للمتغير |
| `+=` | `x += 3` | `x = x + 3` | Adds and assigns | إضافة وإسناد |
| `-=` | `x -= 3` | `x = x - 3` | Subtracts and assigns | طرح وإسناد |
| `*=` | `x *= 3` | `x = x * 3` | Multiplies and assigns | ضرب وإسناد |
| `/=` | `x /= 3` | `x = x / 3` | Divides and assigns | قسمة وإسناد |
| `%=` | `x %= 3` | `x = x % 3` | Takes modulus and assigns | باقي قسمة وإسناد |
| `//=` | `x //= 3` | `x = x // 3` | Floor divides and assigns | قسمة صحيحة وإسناد |
| `**=` | `x **= 3` | `x = x ** 3` | Exponentiates and assigns | أس وإسناد |
| `&=` | `x &= 3` | `x = x & 3` | Bitwise AND and assigns | إسناد مع معالجة AND بتية |
| `\|=` | `x \|= 3` | `x = x \| 3` | Bitwise OR and assigns | إسناد مع معالجة OR بتية |
| `^=` | `x ^= 3` | `x = x ^ 3` | Bitwise XOR and assigns | إسناد مع معالجة XOR بتية |
| `>>=` | `x >>= 3` | `x = x >> 3` | Bitwise right shift and assigns | إزاحة بتية لليمن وإسناد |
| `<<=` | `x <<= 3` | `x = x << 3` | Bitwise left shift and assigns | إزاحة بتية لليسار وإسناد |
| `:=` | `print(x := 3)` | `x = 3`<br>`print(x)` | Walrus Operator: assigns value as part of an expression | معامل الإسناد التعبيري (Walrus) |

## المعامل الثلاثي
هو اختصار في سطر واحد لجملة الشرط التقليدية if/else

## Comparison Operators in Python

Comparison operators are used to compare two values and return a Boolean value (`True` or `False`):

| Operator | Name | Example | Description | Arabic Translation |
| :--- | :--- | :--- | :--- | :--- |
| `==` | Equal | `x == y` | Returns `True` if both values are equal | يساوي |
| `!=` | Not equal | `x != y` | Returns `True` if values are not equal | لا يساوي |
| `>` | Greater than | `x > y` | Returns `True` if left value is greater than right value | أكبر من |
| `<` | Less than | `x < y` | Returns `True` if left value is less than right value | أصغر من (أقل من) |
| `>=` | Greater than or equal to | `x >= y` | Returns `True` if left value is greater than or equal to right value | أكبر من أو يساوي |
| `<=` | Less than or equal to | `x <= y` | Returns `True` if left value is less than or equal to right value | أصغر من أو يساوي |

## Logical Operators in Python

Logical operators are used to combine conditional statements and evaluate to a Boolean value (`True` or `False`):

| Operator | Description | Example | Behavior | Arabic Translation |
| :--- | :--- | :--- | :--- | :--- |
| `and` | Returns `True` if both statements are true | `x < 5 and x < 10` | Evaluates to `True` only when all conditions are met | و (معامل الربط "و") |
| `or` | Returns `True` if one of the statements is true | `x < 5 or x < 4` | Evaluates to `True` if at least one condition is met | أو (معامل الربط "أو") |
| `not` | Reverse the result, returns `False` if the result is true | `not(x < 5 and x < 10)` | Inverts the Boolean state of the expression | ليس (معامل النفي) |

## Identity Operators in Python

Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object in memory (sharing the same memory location / `id()`):

| Operator | Description | Example | Behavior | Arabic Translation |
| :--- | :--- | :--- | :--- | :--- |
| `is` | Returns `True` if both variables are the same object | `x is y` | Checks if `id(x) == id(y)` | مطابقة الهوية (نفس الكائن في الذاكرة) |
| `is not` | Returns `True` if both variables are not the same object | `x is not y` | Checks if `id(x) != id(y)` | عدم مطابقة الهوية (كائنان مختلفان) |

## Membership Operators in Python

Membership operators are used to test if a sequence (such as a string, list, tuple, set, or dictionary) is present in an object:

| Operator | Description | Example | Behavior | Arabic Translation |
| :--- | :--- | :--- | :--- | :--- |
| `in` | Returns `True` if a sequence with the specified value is present in the object | `x in y` | Evaluates to `True` if element exists within the target object | موجود في |
| `not in` | Returns `True` if a sequence with the specified value is not present in the object | `x not in y` | Evaluates to `True` if element does not exist within the target object | غير موجود في |

## Bitwise Operators in Python

Bitwise operators are used to compare and manipulate numbers at their binary level:

| Operator | Name | Description | Example | Arabic Translation |
| :--- | :--- | :--- | :--- | :--- |
| `&` | AND | Sets each bit to 1 if both bits are 1 | `x & y` | و (Bitwise AND) |
| `\|` | OR | Sets each bit to 1 if one of two bits is 1 | `x \| y` | أو (Bitwise OR) |
| `^` | XOR | Sets each bit to 1 if only one of two bits is 1 | `x ^ y` | أو الحصرية (Bitwise XOR) |
| `~` | NOT | Inverts all the bits (returns `-(x + 1)`) | `~x` | النفي البتي (Bitwise NOT) |
| `<<` | Zero fill left shift | Shift left by pushing zeros from right (multiplies by $2^n$) | `x << 2` | إزاحة للبيسار |
| `>>` | Signed right shift | Shift right by pushing copies of leftmost bit from left (divides by $2^n$) | `x >> 2` | إزاحة لليمين |

## أسبقية أو أولوية عوامل التشغيل

## Operator Precedence in Python

The precedence order is described in the table below, starting with the highest precedence at the top (evaluated first):

| Precedence | Operator | Description | Arabic Translation |
| :---: | :--- | :--- | :--- |
| **1** | `()` | Parentheses | أقواس التجميع (الأعلى أولوية) |
| **2** | `**` | Exponentiation | الأس والرفع |
| **3** | `+x`, `-x`, `~x` | Unary plus, unary minus, and bitwise NOT | الإشارات الأحادية والنفي البتي |
| **4** | `*`, `/`, `//`, `%` | Multiplication, division, floor division, and modulus | الضرب، القسمة، القسمة الصحيحة، وباقي القسمة |
| **5** | `+`, `-` | Addition and subtraction | الجمع والطرح |
| **6** | `<<`, `>>` | Bitwise left and right shifts | الإزاحة البتية (يمين ويسار) |
| **7** | `&` | Bitwise AND | معامل AND البتي |
| **8** | `^` | Bitwise XOR | معامل XOR البتي |
| **9** | `\|` | Bitwise OR | معامل OR البتي |
| **10** | `==`, `!=`, `>`, `>=`, `<`, `<=`, `is`, `is not`, `in`, `not in` | Comparisons, identity, and membership operators | معاملات المقارنة، الهوية، والأنتماء |
| **11** | `not` | Logical NOT | النفي المنطقي |
| **12** | `and` | Logical AND | العطف المنطقي |
| **13** | `or` | Logical OR | التخيير المنطقي (الأدنى أولوية) |

====================================

# مصطلحات برمجية :-

| الكلمة | المعني |
| :-------- | :------------------------- |
| `` | |
| `` | |
| `` | |

============================

## المصدر:-

- [Python Operators with w3schools](https://www.w3schools.com/python/python_operators.asp)