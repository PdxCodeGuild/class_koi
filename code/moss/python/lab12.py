path_to_folder = './data/family_location.csv'

with open(path_to_folder, 'r') as file:
    lines = file.read().split('\n')

rows_list = []

for line in lines:
    rows_list.append(line.split(','))

key_list = rows_list.pop(0)

contact_list = []

for row in rows_list:
    contact_list.append({key_list[0]:row[0],key_list[2]:row[2],key_list[3]:row[3]})

print(lines)
print('-'*72)
print(rows_list)
print('-'*72)
print(key_list)
print('-'*72)
print(contact_list)