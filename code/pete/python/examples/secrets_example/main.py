from secrets import SUPER_SECRET_KEY

print(SUPER_SECRET_KEY)


def login(key):
    if key == '12345':
        print('login successful')
    else:
        print('try again')

login(SUPER_SECRET_KEY)