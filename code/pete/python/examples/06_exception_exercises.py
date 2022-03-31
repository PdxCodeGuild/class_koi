# Exercise 1

# teachers = [
#     {
#         'name': 'Lisa',
# 		'city': 'Portland',
# 		'job': 'programmer',
# 		'computer': 'windows',
# 		'cat': 'Heather'
#     },
#     {
#         'name': 'Pete',
#         'city': 'Portland',
#         'job': 'programmer',
#         'computer': 'Mac',
#     },
# ]
# keys = ['name', 'city', 'job', 'computer', 'cat']
# for teacher in teachers:
#     for key in keys:
#         try:
#             print(f'Their {key} is {teacher[key]}') # KeyError: 'cat'
#         except KeyError:
#             print(f"{teacher['name']} does not have a {key}.")


# Exercise 2




from typing import Type


def add(x, y):
    return x + y


test_inputs = [
    (2, 2), # 4
    ('2', '2'), # bug: '22'
    (2, '2'), # 4
    ('two', 2),
]

for nums in test_inputs:
    try:
        print(add(nums[0], nums[1]))
    except (ValueError, TypeError) as e: # e is the error, ValueError is the class to which the error belongs
        print('Something went wrong: ', e)
