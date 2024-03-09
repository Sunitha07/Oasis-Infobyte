def calculate_bmi(weight, height):
    """
    Calculate BMI (Body Mass Index) using weight (in kilograms) and height (in meters).
    Formula: BMI = weight (kg) / (height (m) * height (m))
    """
    height_meters = height / 100  # Convert height from centimeters to meters
    bmi = weight / (height_meters ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Interpret BMI value and provide corresponding category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator!")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in centimeters: "))
    
    bmi = calculate_bmi(weight, height)
    print("Your BMI is:", bmi)
    
    interpretation = interpret_bmi(bmi)
    print("Interpretation:", interpretation)

if __name__ == "__main__":
    main()
