def length_converter(value, from_unit, to_unit):
    length_units = {
        'meter': 1,
        'kilometer': 1000,
        'feet': 0.3048,
        'mile': 1609.34
    }
    value_in_meters = value * length_units[from_unit]
    return value_in_meters / length_units[to_unit]


def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'gram': 1,
        'kilogram': 1000,
        'pound': 453.592
    }
    value_in_grams = value * weight_units[from_unit]
    return value_in_grams / weight_units[to_unit]


def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    # Convert from any to Celsius
    if from_unit == "fahrenheit":
        value = (value - 32) * 5 / 9
    elif from_unit == "kelvin":
        value = value - 273.15

    # Convert from Celsius to target
    if to_unit == "fahrenheit":
        return (value * 9 / 5) + 32
    elif to_unit == "kelvin":
        return value + 273.15
    else:
        return value


# Main Program
print("Unit Converter")
category = input("Choose category (length, weight, temperature): ").lower()

if category == "length":
    val = float(input("Enter value: "))
    from_u = input("From unit (meter, kilometer, feet, mile): ").lower()
    to_u = input("To unit (meter, kilometer, feet, mile): ").lower()
    result = length_converter(val, from_u, to_u)
    print(f"{val} {from_u} = {result:.2f} {to_u}")

elif category == "weight":
    val = float(input("Enter value: "))
    from_u = input("From unit (gram, kilogram, pound): ").lower()
    to_u = input("To unit (gram, kilogram, pound): ").lower()
    result = weight_converter(val, from_u, to_u)
    print(f"{val} {from_u} = {result:.2f} {to_u}")

elif category == "temperature":
    val = float(input("Enter value: "))
    from_u = input("From unit (celsius, fahrenheit, kelvin): ").lower()
    to_u = input("To unit (celsius, fahrenheit, kelvin): ").lower()
    result = temperature_converter(val, from_u, to_u)
    print(f"{val} {from_u} = {result:.2f} {to_u}")

else:
    print("Invalid category selected.")
