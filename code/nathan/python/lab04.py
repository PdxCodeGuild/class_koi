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
    
for i in range(100):
     versionOne(i)

for i in range(1000):
    versionTwo(i)