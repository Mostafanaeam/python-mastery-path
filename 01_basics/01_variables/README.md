# متغيرات بايثون

**المتغيرات** هي عبارة عن حاوية بضع فيها البيانات

## إنشاء المتغيرات

- مافيش امر معين اكتبه علشان اعرف متغير 
- المتغير بينشأ تلقائيا لما احط جواه البيانات اللي عايز اخزنها

```python
x = 5
y = "John"
print(x)
print(y)
```
مش محتاج اني اقول للكومبيوتر ان في متغير و مش لازم اني اعرف المتغير دا اي نوعه و كمان بعد ما اكتب المتغير و اديله قيمه اقدر اغيرها بقيمة تاني لما اعرفها مرة تانية

```python
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
```
## تحويل أنواع البيانات
لو انت عايز تحدد نوع البيانات دي تقدر عاديمن خلال تحويل البيانات

```python
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
```
## احصل على النوع

اقدر اعرف موع البيانات من خلال دالة 
[type()](https://www.w3schools.com/python/ref_func_type.asp)

```python
x = 5
y = "John"
print(type(x))
print(type(y))
```

## علامات اقتباس مفردة أم مزدوجة؟

اقدر اعرف المتفير النصي سواء علامات تنصيص مفرده او مزوج
```python
x = "John"
# is the same as
x = 'John'
```

## Case-Sensitive
اسماء المتغيرات Case-Sensitive
```python
a = 4
A = "Sally"
#A will not overwrite a
```
## اسماء المتغيرات 
يمكن أن يكون للمتغير اسم قصير (مثل x و y) أو اسم أكثر وصفًا (العمر، اسم السيارة، الحجم الكلي).

### Rules for Python variables:

- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (age, Age and AGE are three different variables)
- A variable name cannot be any of the [Python keywords](https://www.w3schools.com/python/python_ref_keywords.asp)

====================================

# مصطلحات برمجية :-

| الكلمة | المعني |
| :-------- | :------------------------- |
| `declare` | إخبار الحاسوب بوجود متغير، أو دالة، أو صنف جديد وتحديد اسمه ونوعه قبل استخدامه في الشيفرة |
| `Casting` | عملية تغيير نوع قيمة أو متغير من نوع بيانات إلى نوع آخر داخل دليل مبرمج، مثل تحويل رقم صحيح إلى رقم عشري. |
| `Case-Sensitive`|يعني أن اللغة أو النظام يفرق تماماً بين الأحرف الكبيرة والأحرف الصغيرة ويعتبرها رموزاً مختلفة |
| `unpacking` | التفكيك أو الاستخراج في البرمجة يشير إلى عملية أخذ العناصر داخل هيكل بيانات مجمع مثل المصفوفات، القوائم، أو القواميس وتوزيعها أو تفكيكها إلى متغيرات مستقلة بمرة واحدة. |