
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def main():
    print("Temperature Converter")
    print("Available conversions:")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")

    try:
        choice = int(input("Choose conversion option (1-6): "))
        temp = float(input("Enter temperature value: "))

        if choice == 1:
            result = celsius_to_fahrenheit(temp)
            print(f"{temp}°C = {result:.2f}°F")
        elif choice == 2:
            result = celsius_to_kelvin(temp)
            print(f"{temp}°C = {result:.2f}K")
        elif choice == 3:
            result = fahrenheit_to_celsius(temp)
            print(f"{temp}°F = {result:.2f}°C")
        elif choice == 4:
            result = fahrenheit_to_kelvin(temp)
            print(f"{temp}°F = {result:.2f}K")
        elif choice == 5:
            result = kelvin_to_celsius(temp)
            print(f"{temp}K = {result:.2f}°C")
        elif choice == 6:
            result = kelvin_to_fahrenheit(temp)
            print(f"{temp}K = {result:.2f}°F")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter numeric values only.")

if __name__ == "__main__":
    main()
