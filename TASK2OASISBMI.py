def get_user_input():
    while True:
        try:
            weight = float(input("Enter your weight (in kg): "))
            height = float(input("Enter your height (in meters): "))
            if weight <= 0 or height <= 0:
                raise ValueError("Weight and height must be positive numbers.")
            return weight, height
        except ValueError as e:
            print(f"Invalid input: {e}")

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    weight, height = get_user_input()
    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)
    print(f"Your BMI is {bmi:.2f} and you are {category}.")

if __name__ == "__main__":
    main()