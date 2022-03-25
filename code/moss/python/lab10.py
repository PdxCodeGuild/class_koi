print('\nWelcome to ROT Cipher!\n')

user_string = input('Enter a string to encode:')

user_string_list = list(user_string)

output_list = []

eng_to_rot = {'a':'n','b':'o','c':'p','d':'q','e':'r','f':'s',
'g':'t','h':'u','i':'v','j':'w','k':'x','l':'y','m':'z','o':'b',
'p':'c','q':'d','r':'e','s':'f','t':'g','u':'h','v':'i','w':'j',
'x':'k','y':'l','z':'m',}

