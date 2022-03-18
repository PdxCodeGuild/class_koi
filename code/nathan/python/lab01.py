
# Ask the user for the number of feet, and print out the equivalent distance in meters.
print("\n***\nLab01 Version 1:\n***\n")

def versionOne(num):
    # feet to meters
    return round(num * 0.3048, 4)

userInput = int(input("What is the distance in feet? "))
print(f"{userInput} ft is {versionOne(userInput)} m.")


# Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.
print("\n***\nLab01 Version 2:\n***\n")

def versionTwo(num, units):
    '''If Version

    # units to meters
    if(units == 'ft'):
        # convert to feet
        return round(num * 0.3048, 4)
    elif(units == 'mi'):
        # convert to miles
        return round(num * 1609.34, 4)
    elif(units == 'm'):
        # convert to meters
        return num * 1
    elif(units == 'km'):
        # convert to kilometers
        return num * 1000
    '''

    toMeters = {
        "ft" : 0.3048,
        "mi" : 1609.34,
        "m" : 1,
        "km" : 1000
    }

    return num * toMeters[units]

userInputDistance = int(input("What is the distance? "))
userInputUnits = input("What are the units? (ft, mi, m, km): ")
print(f"{userInputDistance} {userInputUnits} is {versionTwo(userInputDistance, userInputUnits)} m.")


# Add support for yards, and inches.
print("\n***\nLab01 Version 3:\n***\n")

def versionThree(num, units):
    ''' If Version
    # units to meters
    if(units == 'ft'):
        # convert to feet
        return num * 0.3048
    elif(units == 'mi'):
        # convert to miles
        return num * 1609.34
    elif(units == 'm'):
        # convert to meters
        return num * 1
    elif(units == 'km'):
        # convert to kilometers
        return num * 1000
    elif(units == 'yd'):
        # convert to yards
        return round(num * 0.9144, 4)
    elif(units == 'in'):
        # convert to inches
        return num * 0.0254
    '''
    toMeters = {
        "ft" : 0.3048,
        "mi" : 1609.34,
        "m" : 1,
        "km" : 1000,
        "yd" : 0.9144,
        "in" : 0.0254
    }

    return num * toMeters[units]

userInputDistance = int(input("What is the distance? "))
userInputUnits = input("What are the units? (ft, mi, m, km, yd, in): ")
print(f"{userInputDistance} {userInputUnits} is {versionThree(userInputDistance, userInputUnits)} m.")


# convert any unit to meters, then convert the distance in meters to any other unit.
print("\n***\nLab01 Version 4:\n***\n")

def versionFour(num, input, output):
    toMeters = {
        "ft" : 0.3048,
        "mi" : 1609.34,
        "m" : 1,
        "km" : 1000
    }
    num *= toMeters[input] # convert input to meters

    return num / toMeters[output] # convert meters to output

userInputDistance = int(input("What is the distance? "))
userInputUnitsFrom = input("What are the input units? (ft, mi, m, km): ")
userInputUnitsTo = input("What are the output units? (ft, mi, m, km): ")

print(f"{userInputDistance} {userInputUnitsFrom} is {versionFour(userInputDistance, userInputUnitsFrom, userInputUnitsTo)} {userInputUnitsTo}")