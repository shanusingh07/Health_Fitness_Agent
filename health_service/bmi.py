def calculate_bmi(weight, height):
    # height cm me hai → convert to meters
    height_m = height / 100

    bmi = weight / (height_m ** 2)
    return round(bmi, 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal weight"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"