# Lab 1: Unit Converter
# Mitch Chapman

# # Version 1 ---------------------------------------------------------------------

# value = float(input("What is the distance in feet? "))

# output = round((value * 0.3048), 4)


# print(f"{value} ft is {output} m")



# # Version 2 ---------------------------------------------------------------------
# conversion_ratios_to_m = {
#     "ft": 0.3048,
#     "mi": 1609.34,
#     "m": 1,
#     "km": 1000,
# }

# def conversion_to_m(value, unit):
#     """Converts input float to a float in meters. Accepts inputs: 'ft', 'mi', 'm', 'km'."""
#     meters_output = value * conversion_ratios_to_m[unit]
#     return round(meters_output, 4)

# value = float(input("What is the distance? "))
# unit = input("What are the units? ('ft', 'mi', 'm', 'km') ")

# output = conversion_to_m(value, unit)


# print(f"{value} {unit} is {output} m")



# # Version 3 ---------------------------------------------------------------------

# conversion_ratios_to_m = {
#     "ft": 0.3048,
#     "mi": 1609.34,
#     "m": 1,
#     "yd": 0.9144,
#     "in": 0.0254,
# }

# def conversion_to_m(value, unit):
#     """Converts input float to a float in meters. Accepts inputs: 'ft', 'mi', 'm', 'km', 'yd', or 'in'."""
#     meters_output = value * conversion_ratios_to_m[unit]
#     return round(meters_output, 4)

# value = float(input("What is the distance? "))
# unit = input("What are the units? ('ft', 'mi', 'm', 'km', 'yd', 'in') ")

# output = conversion_to_m(value, unit)


# print(f"{value} {unit} is {output} m")



# Version 4 ---------------------------------------------------------------------

conversion_ratios = {
    "ft": 0.3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000,
    "yd": 0.9144,
    "in": 0.0254,
}

def conversion_to_m(value, unit_from, unit_to):
    """Converts input float to a float of another unit. Accepts inputs/outputs: 'ft', 'mi', 'm', 'km', 'yd', or 'in'."""
    meters_output = value * conversion_ratios[unit_from]
    unit_output = meters_output / conversion_ratios[unit_to]
    return round(unit_output, 4)

value = float(input("What is the distance? "))
unit_from = input("What are the input units? ('ft', 'mi', 'm', 'km', 'yd', 'in') ")
unit_to = input("What are the output units? ('ft', 'mi', 'm', 'km', 'yd', 'in') ")

output = conversion_to_m(value, unit_from, unit_to)


print(f"{value} {unit_from} is {output} {unit_to}")



