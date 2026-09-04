"""
03 — Unit Converter
اسم الريبو
python-unit-converter
تفاصيل البروجيكت

اعمل برنامج لتحويل الوحدات.

في البداية خلي البرنامج يدعم:

Temperature
Celsius → Fahrenheit
Fahrenheit → Celsius
Length
Meters → Kilometers
Kilometers → Meters
Meters → Centimeters
Centimeters → Meters
Weight
Kilograms → Grams
Grams → Kilograms

استخدم:

Variables
Numbers
Casting
Operators
User Input
النتيجة النهائية

مثلاً:

================================
        UNIT CONVERTER
================================

1. Celsius → Fahrenheit
2. Fahrenheit → Celsius
3. Meters → Kilometers
4. Kilometers → Meters
5. Kilograms → Grams
6. Grams → Kilograms

Choose: 1

Enter value: 25

Result: 77.0 Fahrenheit
Bonus إضافي

اعمل Menu حقيقي يسمح للمستخدم يعمل أكثر من عملية تحويل في نفس التشغيل.
"""
print("\n" + 33 * "=")
print("       UNIT CONVERTER")
print( 33 * "=")

menu = """
1. Celsius → Fahrenheit
2. Fahrenheit → Celsius
3. Meters → Kilometers
4. Kilometers → Meters
5. Kilograms → Grams
6. Grams → Kilograms
"""
while True:
        choice = input(menu + "\n choose from the following options: ")
        value = float(input("Enter value: "))
        if choice == "1":
                # Conversion logic for Celsius to Fahrenheit
                result = (value * 9/5) + 32
                print(f"Result: {result} Fahrenheit")
        elif choice == "2":
                # Conversion logic for Fahrenheit to Celsius
                result = (value - 32) * 5/9
                print(f"Result: {result} Celsius")
        elif choice == "3":
                # Conversion logic for Meters to Kilometers
                result = value / 1000
                print(f"Result: {result} Kilometers")
        elif choice == "4":
                # Conversion logic for Kilometers to Meters
                result = value * 1000
                print(f"Result: {result} Meters")
        elif choice == "5":
                # Conversion logic for Kilograms to Grams
                result = value * 1000
                print(f"Result: {result} Grams")
        elif choice == "6":
                # Conversion logic for Grams to Kilograms
                result = value / 1000
                print(f"Result: {result} Kilograms")
        # Add more elif blocks for other conversion options
        continue_choice = input("Do you want to perform another conversion? (yes/no): ")
        if continue_choice.lower() != "yes":
            print("thank you for using the Unit Converter. Goodbye!")
            break
            