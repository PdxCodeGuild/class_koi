#  *'-.-'*'-.-'*'-.-'*'--'*
#     Project: Python 
#   Lab 12: Contact List
#       Version: 1.0
#   Author: Shaine Warren
#   Email: mwarren86@gmail.com
#       Date: Mar, 2022
# *'-.-'*'-.-'*'-.-'*'--'*

with open('class_koi/code/shaine/python/data/contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    # print(lines)


headers = lines[0].split(', ')
# print(headers)

contacts = []

for i in range (1, len(lines)):
    full_entry  = {}
    for header in headers:
        info = lines[i].split(', ')
        entry = {header:info[headers.index(header)]}
        full_entry.update(entry)
    contacts.append(full_entry)

print(contacts)

# csv = ','.join(contact for contact in contacts)

# print(csv)








        # for info in info:
        #     entry = {header:info}
        #     print(entry)
        




    # # for line in lines[0]:
    #     # dictionary = {str(lines):str(lines)[i]}
    #     print(dictionary)


