'''
Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.
'''
def versionOne(number):
    tens = {
        10 : "ten",
        11 : "eleven",
        12 : "twelve",
        13 : "thirteen",
        14 : "fourteen",
        15 : "fifteen",
        16 : "sixteen",
        17 : "seventeen",
        18 : "eighteen",
        19 : "nineteen"
    }

    onesPlace = {
        0 : "",
        1 : "one",
        2 : "two",
        3 : "three",
        4 : "four",
        5 : "five",
        6 : "six",
        7 : "seven",
        8 : "eight",
        9 : "nine"
    }

    tensPlace = {
        0 : "tenszero",
        1 : "tensone",
        2 : "twenty",
        3 : "thirty",
        4 : "fourty",
        5 : "fifty",
        6 : "sixty",
        7 : "seventy",
        8 : "eighty",
        9 : "ninety"
    }

    if(number == 0):
        print("zero")
        return

    if(number >= 10 and number < 20):
        print(tens[number])
        return

    tensDigit = number // 10
    onesDigit = number % 10
    
    if(tensDigit == 0):
        print(onesPlace[onesDigit])
        return

    if(onesDigit == 0):
        print(tensPlace[tensDigit])
        return

    print(tensPlace[tensDigit] + '-' + onesPlace[onesDigit])
    return

def versionTwo(number):
    tens = {
        10 : "ten",
        11 : "eleven",
        12 : "twelve",
        13 : "thirteen",
        14 : "fourteen",
        15 : "fifteen",
        16 : "sixteen",
        17 : "seventeen",
        18 : "eighteen",
        19 : "nineteen"
    }

    onesAndHundreds = {
        0 : "",
        1 : "one",
        2 : "two",
        3 : "three",
        4 : "four",
        5 : "five",
        6 : "six",
        7 : "seven",
        8 : "eight",
        9 : "nine"
    }

    tensPlace = {
        0 : "",
        1 : "",
        2 : "twenty",
        3 : "thirty",
        4 : "fourty",
        5 : "fifty",
        6 : "sixty",
        7 : "seventy",
        8 : "eighty",
        9 : "ninety"
    }

    hundredsDigit = number // 100
    tensDigit = number // 10
    tensDigit %= 10
    onesDigit = number % 10

    # print(f"hundred = {hundredsDigit}")
    # print(f"ten = {tensDigit}")
    # print(f"one = {onesDigit}")

    if(number == 0):
        print("zero")
        return

    if(number < 100):
        if(tensDigit == 0):
            print(onesAndHundreds[onesDigit])
            return

        if(number >= 10 and number < 20):
            print(tens[number])
            return

        if(onesDigit == 0):
            print(tensPlace[tensDigit])
            return
    
        print(tensPlace[tensDigit] + '-' + onesAndHundreds[onesDigit])
        return
    
    if(number - 100 * hundredsDigit >= 10 and number - 100 * hundredsDigit < 20):
        print(f"{onesAndHundreds[hundredsDigit]} hundred {tens[number - 100 * hundredsDigit]}")
        return

    if(tensDigit == 0 and onesDigit == 0):
        print(f"{onesAndHundreds[hundredsDigit]} hundred")
        return
    
    if(onesDigit == 0):
        print(f"{onesAndHundreds[hundredsDigit]} hundred {tensPlace[tensDigit]}")
        return

    if(tensDigit == 0):
        print(f"{onesAndHundreds[hundredsDigit]} hundred {onesAndHundreds[onesDigit]}")
        return
    
    print(f"{onesAndHundreds[hundredsDigit]} hundred {tensPlace[tensDigit]}-{onesAndHundreds[onesDigit]}")
    return

# Convert a number to roman numerals.
def versionThree(number):
    '''
    i = 1
    iv = 4
    v = 5
    ix = 9
    x = 10
    xl = 40
    l = 50
    xc = 90
    c = 100

    3 = iii
    14 = xiv

    numerals = {
        1 : "i",
        4 : "iv",
        5 : "v",
        9 : "ix",
        10 : "x",
        40 : "xl",
        50 : "l",
        90 : "xc",
        100 : "c",
    }
    DICTIONARIES ARE NOT ORDERED
    FOR LOOPS NO WORKY
    '''

    numerals = [
        (100, "c"),
        (90, "xc"),
        (50, "l"),
        (40, "xl"),
        (10, "x"),
        (9, "ix"),
        (5, "v"),
        (4, "iv"),
        (3, "iii"),
        (2, "ii"),
        (1, "i"),
    ]

    tempList = []

    for i in numerals:
        temp = number // i[0]
        number -= temp * i[0]

        if(temp > 0):
            tempList.append(i[1])

    tempList = ''.join(tempList)
    print(tempList)
    return tempList # If they want it I guess

# Convert a time given in hours and minutes to a phrase.
def versionFour(time):
    time = time.split(':')
    versionOne(int(time[0])), versionOne(int(time[1]))
    


# for i in range(100):
#      versionOne(i)

# for i in range(1000):
#     versionTwo(i)

# versionThree(12)

versionFour("12:30")