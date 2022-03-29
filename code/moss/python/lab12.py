#path_to_folder = 'code/class_koi/code/moss/python/data/'

with open('family_location.csv', 'r') as file:
    lines = file.read().split('\n')

print(lines)

rows_list = []

for line in lines:
    rows_list.append(line.split(','))

print('-'*72)

print(rows_list)

print('-'*72)

key_list = rows_list.pop(0)

print(key_list)

print('-'*72)

contact_list = []

for row in rows_list:
    contact_list.append({key_list[0]:row[0],key_list[2]:row[2],key_list[3]:row[3]})

print(contact_list)
