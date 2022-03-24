
usr_num = input('\nEnter a number to convert into a phrase:\n')

usr_num = int(usr_num)

ones_digit = usr_num%10
print(f'\nOnes place: {ones_digit}\n')

tens_digit = (usr_num//10)%10
print(f'\nTens place: {tens_digit}\n')

hundrds_digit = (usr_num//100)
print(f'\nHundreds place: {hundrds_digit}\n')

ones = { 0:'zero',1:'one',2:'two',3:'three',4:'four',
    5:'five',6:'six',7:'seven',8:'eight',9:'nine'}

teens = {10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen', 
    15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}

tens = {20:'twenty', 30:'thirty',40:'forty',50:'fifty',
    60:'sixty',70:'seventy',80:'eighty',90:'ninety'}

#----- Version 1 -----#

# while True:

if usr_num < 10:
    num_convr_wrd = ones[usr_num]
    print(f'\n{usr_num} is converted into : {num_convr_wrd}.\n')

elif usr_num >= 10 and usr_num <= 19:
    num_convr_wrd = teens[usr_num]
    print(f'\n{usr_num} is converted into : {num_convr_wrd}.\n')

elif usr_num >= 20 and usr_num <= 99:

    if ones_digit == 0 :
        num_convr_wrd = tens[usr_num]
        print(f'\n{usr_num} is converted into : {num_convr_wrd}.\n')
        
    else:
        num_convr_wrd = tens[tens_digit*10] + '-' + ones[ones_digit]
        print(f'\n{usr_num} is converted into : {num_convr_wrd}.\n')

    #----- Version 2 -----#

elif usr_num >= 100 and usr_num <= 999:

    if tens_digit == 0 and ones_digit == 0:
        num_convr_wrd = ones[hundrds_digit] + '-hundred'
        print(f'\n{usr_num} is converted into : {num_convr_wrd}.\n')
        
    elif tens_digit == 0 :
        num_convr_wrd = ones[hundrds_digit] + '-hundred and ' + ones[ones_digit]
        print(f'\n{usr_num} is converted into : {num_convr_wrd}.\n')
        
    elif tens_digit == 1:
        num_convr_wrd = ones[hundrds_digit] + '-hundred and ' + teens[ones_digit + 10]
        print(f'\n{usr_num} is converted into : {num_convr_wrd}.\n')
        
    elif ones_digit == 0:
        num_convr_wrd = ones[hundrds_digit] + '-hundred and ' + tens[tens_digit * 10]
        print(f'\n{usr_num} is converted into : {num_convr_wrd}.\n')
        
    elif tens_digit >= 2 and tens_digit <= 9:
        num_convr_wrd = ones[hundrds_digit] + '-hundred and ' + tens[tens_digit * 10] + '-' + ones[ones_digit]
        print(f'\n{usr_num} is converted into : {num_convr_wrd}.\n')
    
   
        