from random import random, randint, choice
from string import whitespace

symbols = {
    # '؋': 'Afghanistan Afghani',
    'ƒ': 'Aruba Guilder',
    '₼': 'Azerbaijan Manat',
    '៛': 'Cambodia Riel',
    '₡': 'Costa Rica Colon',
    '₱': 'Cuba Peso',
    '€': 'Euro Member Countries',
    '¢': 'Ghana Cedi',
    # '﷼': 'Iran Rial',
    '₪': 'Israel Shekel',
    '¥': 'Japan Yen',
    '₩': 'Korea (South) Won',
    '₭': 'Laos Kip',
    '₮': 'Mongolia Tughrik',
    '₦': 'Nigeria Naira',
    '₽': 'Russia Ruble',
    '฿': 'Thailand Baht',
    '₴': 'Ukraine Hryvnia',
    '£': 'United Kingdom Pound',
    '$': 'United States Dollar',
    '₫': 'Viet Nam Dong',
}

def fill_wallet(operations):
    output = []
    for _ in range(operations):
        if random() < 0.25:
            output.append(get_currency())
        else:
            output.append(choice(whitespace))
    return output

def get_currency():
    return f'{choice(list(symbols.keys()))}{get_nums()}{get_cents()}'

def get_nums():
    return str(randint(0, 5000))

def get_cents():
    if random() < 0.5:
        return ''
    return '.' + str(randint(0, 99)).zfill(2)

with open('wallet.txt', 'w', encoding='utf-16') as f:
    f.writelines(fill_wallet(1000))


"""YOUR CODE TO CONVERT THE CURRENCIES INSIDE THE WALLET GOES BELOW"""