# Lab 4: Number to Phrase
# Mitch Chapman

ones_phrase_dict = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}
teens_phrase_dict = {
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
}
tens_phrase_dict = {
    "2": "twenty",
    "3": "thirty",
    "4": "fourty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety",
}


number_phrase = []

print("\nThis is the number to phrase machine!\n")
number_input = input("Please enter a two digit whole number (0-99): ")

if number_input in teens_phrase_dict.keys():
    number_phrase.append(teens_phrase_dict[number_input])

elif number_input in ones_phrase_dict.keys():
    number_phrase.append(ones_phrase_dict[number_input])


elif len(number_input) == 2:
    tens_str = str(int(number_input)//10)
    number_phrase.append(tens_phrase_dict[tens_str])
    ones_str = str(int(number_input)%10)
    if ones_str != "0":
        number_phrase.append(ones_phrase_dict[ones_str])


print("-".join(number_phrase))




