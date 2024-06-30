# Functions
# code Blocks
# while Loops

logo = """

       -=[ shortened thermometer ]=
                  __________________________________________________
           ____.-"":":":":":":":":":":":":":":":":":":":":":":":":":"-.
          (___:===='==='==='==='==='==='==='=A '   '   '   '   '   '   )
          jgs `'-._92____94____96____8__|_100____2_____4_____6_____8.-`
"""
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def main():
    print(logo)
    print("\nWelcome to the Temperature Converter!")
    print("\n")
    print("Choose an option to convert:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    
    choice = input("Enter the number of your choice: ")
    
    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius} Celsius is {celsius_to_fahrenheit(celsius)} Fahrenheit")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit} Fahrenheit is {fahrenheit_to_celsius(fahrenheit)} Celsius")
    elif choice == '3':
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius} Celsius is {celsius_to_kelvin(celsius)} Kelvin")
    elif choice == '4':
        kelvin = float(input("Enter temperature in Kelvin: "))
        print(f"{kelvin} Kelvin is {kelvin_to_celsius(kelvin)} Celsius")
    elif choice == '5':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit} Fahrenheit is {fahrenheit_to_kelvin(fahrenheit)} Kelvin")
    elif choice == '6':
        kelvin = float(input("Enter temperature in Kelvin: "))
        print(f"{kelvin} Kelvin is {kelvin_to_fahrenheit(kelvin)} Fahrenheit")
    else:
        print("Invalid choice. Please run the program again.")
    
    print("Thank you for using the Temperature Converter!")

if __name__ == "__main__":
    main()
