def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5 / 9 + 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9 / 5 + 32

def display_menu():
    print("\n🌡️ Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

def main():
    print("🎯 Welcome to the Multi-Mode Temperature Converter!")

    while True:
        display_menu()
        choice = input("Choose an option (1-7): ").strip()

        try:
            if choice == '1':
                c = float(input("Enter temperature in °C: "))
                print(f"{c:.2f}°C = {celsius_to_fahrenheit(c):.2f}°F")

            elif choice == '2':
                f = float(input("Enter temperature in °F: "))
                print(f"{f:.2f}°F = {fahrenheit_to_celsius(f):.2f}°C")

            elif choice == '3':
                c = float(input("Enter temperature in °C: "))
                print(f"{c:.2f}°C = {celsius_to_kelvin(c):.2f} K")

            elif choice == '4':
                k = float(input("Enter temperature in K: "))
                print(f"{k:.2f} K = {kelvin_to_celsius(k):.2f}°C")

            elif choice == '5':
                f = float(input("Enter temperature in °F: "))
                print(f"{f:.2f}°F = {fahrenheit_to_kelvin(f):.2f} K")

            elif choice == '6':
                k = float(input("Enter temperature in K: "))
                print(f"{k:.2f} K = {kelvin_to_fahrenheit(k):.2f}°F")

            elif choice == '7':
                print("👋 Exiting... Thank you for using the converter!")
                break

            else:
                print("❌ Invalid choice. Please select from 1 to 7.")

        except ValueError:
            print("❌ Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
