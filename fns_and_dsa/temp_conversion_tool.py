

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    temperature = (fahrenheit -32) * FAHRENHEIT_TO_CELSIUS_FACTOR

    print(f"{fahrenheit}°F is {temperature}°C")

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    temperature = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

    print(f"{celsius}°C is {temperature}°F")


tempertaure = float(input("Enter the temperature to convert: ").lower())

is_c_or_f = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
if is_c_or_f == 'c':
    convert_to_fahrenheit(celsius=tempertaure)
elif is_c_or_f == 'f':
    convert_to_celsius(fahrenheit=tempertaure)
else:
    print("Invalid temperature. Please enter a numeric value.")