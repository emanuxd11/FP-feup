def classify(weight, height):
    BMI = weight / height**2

    if BMI < 17.0:
        return "underweight"
    if BMI >= 17.0 and BMI < 18.5:
        return "mild_underweight"
    if BMI >= 18.5 and BMI < 25:
        return "normal"
    if BMI >= 25 and BMI < 30:
        return "overweight"
    if BMI > 30.0:
        return "obese"

print(classify(75, 1.75))