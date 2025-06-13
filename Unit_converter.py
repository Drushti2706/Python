def cm_to_inches(cm):
    return cm / 2.54

def inches_to_cm(inches):
    return inches * 2.54

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def show_menu():
    print("\nUNIT CONVERTER")
    print("1. Length (cm <-> inches)")
    print("2. Weight (kg <-> pounds)")
    print("3. Temperature (C <-> F)")
    print("4. Exit")

def length_converter():
    print("\nLength Conversion")
    print("1. cm to inches")
    print("2. inches to cm")
    choice = input("Choose: ")
    value = float(input("Enter value: "))
    if choice == "1":
        result = cm_to_inches(value)
        print(f"{value} cm = {result:.2f} inches")
    elif choice == "2":
        result = inches_to_cm(value)
        print(f"{value} inches = {result:.2f} cm")
    else:
        print("Invalid choice.")

def weight_converter():
    print("\nWeight Conversion")
    print("1. kg to pounds")
    print("2. pounds to kg")
    choice = input("Choose: ")
    value = float(input("Enter value: "))
    if choice == "1":
        result = kg_to_pounds(value)
        print(f"{value} kg = {result:.2f} pounds")
    elif choice == "2":
        result = pounds_to_kg(value)
        print(f"{value} pounds = {result:.2f} kg")
    else:
        print("Invalid choice.")

def temperature_converter():
    print("\nTemperature Conversion")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose: ")
    value = float(input("Enter value: "))
    if choice == "1":
        result = celsius_to_fahrenheit(value)
        print(f"{value}°C = {result:.2f}°F")
    elif choice == "2":
        result = fahrenheit_to_celsius(value)
        print(f"{value}°F = {result:.2f}°C")
    else:
        print("Invalid choice.")

def main():
    while True:
        show_menu()
        option = input("Select option: ")
        if option == "1":
            length_converter()
        elif option == "2":
            weight_converter()
        elif option == "3":
            temperature_converter()
        elif option == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
