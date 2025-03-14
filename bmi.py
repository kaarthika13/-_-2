def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    return round(bmi, 2), category
def main():
    print("🩺 BMI Calculator 🩺")
    try:
        weight = float(input("Enter your weight (kg): "))
        height_cm = float(input("Enter your height (cm): "))
        if weight <= 0 or height_cm <= 0:
            print("⚠️ Error: Weight and height must be positive numbers.")
            return
        bmi, category = calculate_bmi(weight, height_cm)
        print(f"\n📊 Your BMI: {bmi}")
        print(f"📌 Category: {category}")
    except ValueError:
        print("⚠️ Error: Please enter valid numerical values.")
if __name__ == "__main__":
    main()