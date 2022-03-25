import re

# it didn't work 😢
# email_regex = re.compile(r'/^([A-Z]|[a-z])\w+@([A-Z]|[a-z])\w+\.([A-Z]|[a-z])\w+$/')

# print(email_regex, type(email_regex))

# print(email_regex.findall('pete@pdxcodeguild.com'))


phone_number_regex = re.compile(r'\d{3}-\d{3}-\d{4}')

# print(phone_number_regex.findall('123-456-7890'))

with open('code/pete/python/examples/data/phone-numbers.txt', 'r') as f:
    contents = f.read()

matches = phone_number_regex.findall(contents)
print(matches) # ['123-456-7890', '555-123-0987']
search = phone_number_regex.search(contents)
print(search) # <re.Match object; span=(0, 12), match='123-456-7890'>
print(search.start()) # 0
print(search.end()) # 12
print(search.group()) # 123-456-7890
