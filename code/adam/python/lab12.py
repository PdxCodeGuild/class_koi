# Lab 12 - Contact List

import csv

with open('data/contacts.csv','r') as csv_contacts:
    lines = csv_contacts.read().split('\n')
    # print(lines)

headers = lines[0]
headers = headers.split(',')
print(headers)
contact1 = lines[1]
contact1 = contact1.split(',')
contact2 = lines[2]
contact2 = contact2.split(',')
contact3 = lines[3]
contact3 = contact3.split(',')
contact4 = lines[4]
contact4 = contact4.split(',')
contact5 = lines[5]
contact5 = contact5.split(',')
contact6 = lines[6]
contact6 = contact6.split(',')
print(contact1)
print(contact2)
print(contact3)
print(contact4)
print(contact5)
print(contact6)
    
# headers
# contact1
contacts_dict = {}
# keys = headers
# values = []
# for i in keys:
#     for x in values:
contacts_dict['name'] = 'jery'

print(contacts_dict)


