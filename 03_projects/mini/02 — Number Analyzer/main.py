"""
02 — Number Analyzer
اسم الريبو
python-number-analyzer
تفاصيل البروجيكت

اعمل برنامج يستقبل رقم من المستخدم ويحلله.

البرنامج يجب أن يعرف:

هل الرقم موجب أم سالب؟
هل الرقم صفر؟
هل الرقم زوجي أم فردي؟
الرقم في صورة int أو float
مربع الرقم
مكعب الرقم
باقي قسمته على رقم آخر

استخدم:

Numbers
Casting
Arithmetic Operators
Comparison Operators
Boolean
User Input
النتيجة النهائية
================================
       NUMBER ANALYZER
================================

Enter a number: 25

Number      : 25
Type        : int
Positive    : True
Negative    : False
Zero        : False
Even        : False
Odd         : True
Square      : 625
Cube        : 15625
Bonus إضافي

أضف تحليل:

Prime Number
Divisible by 3
Divisible by 5
Divisible by 10
"""


while True:
    Number = input("Enter a number: ")
    if not Number.isdigit():
       print("Please enter a valid number.")
       continue
    break

Number = int(Number)

print("\n" + 33 * "=")
print("       NUMBER ANALYZER")
print( 33 * "=")
print(f"Number      : {Number}")
print(f"Type        : {type(Number)}")
print(f"Positive    : {Number > 0}")
print(f"Negative    : {Number < 0}")
print(f"Zero        : {Number == 0}")
print(f"Even        : {Number % 2 == 0}")
print(f"Odd         : {Number % 2 != 0}")
print(f"Square      : {Number ** 2}")
print(f"Cube        : {Number ** 3}")
print(f"Divisible by 3: {Number % 3 == 0}")
print(f"Divisible by 5: {Number % 5 == 0}")
print(f"Divisible by 10: {Number % 10 == 0}")
print( 33 * "=")
