def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def classify_temperature(f):
    if f >= 81:
        return "HOT"
    elif 65 <= f <= 80:
        return "WARM"
    else:
        return "COLD"

def display_result(temp_f, category):
    print(f"{temp_f}°F is {category}")

if __name__ == "__main__":
    c = float(input("Enter temperature in °C: "))
    f = celsius_to_fahrenheit(c)
    cat = classify_temperature(f)
    display_result(f, cat)
