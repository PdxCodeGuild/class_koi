# Lab 12 - Contact List
# Version 1

import csv

with open('data/contacts.csv','r') as csv_contacts:
    lines = csv_contacts.read().split('\n')
    # print(lines)

headers = lines[0]
headers = headers.split(',')
# print(headers)

contacts_list = []
character_dict = {}
character_list = []
for line in lines[1:]:
    character_dict = {}
    character_list = line.split(',')
    for i, key in enumerate(headers):
        character_dict[key] = character_list[i]
    contacts_list.append(character_dict)
print(contacts_list)

#---------------------------------------------------------------------
# Version 2
while True:
    choice = input('[C]reate, 

