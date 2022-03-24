"""SyntaxError"""
# print('test') # this doesn't even print because the code was not compiled properly
# x = 5
# if x > 2 # SyntaxError: invalid syntax

# print('a string' # SyntaxError: unexpected EOF while parsing

"""IndentationError"""
# x = 5
# if x > 2:
# print('hey') IndentationError: expected an indented block

# def func():
# print('this is a poorly-formatted function') IndentationError: expected an indented block

"""NameError"""
# sentence1 = 'Python is cool'
# sentence3 = 'JavaScript is cool'

# print(sentence1)
# print(sentence2) # NameError: name 'sentence2' is not defined
# print(sentence3)

"""AttributeError"""
# nums = [1, 2, 3, 4, 5]
# nums.append(6)
# nums2 = '1, 2, 3, 4, 5, capitalize me'
# nums2.append(6) # AttributeError: 'str' object has no attribute 'append'

# # method example
# print(nums2.upper) # <built-in method upper of str object at 0x10fbb1e90>
# print(nums2.upper()) # 1, 2, 3, 4, 5, CAPITALIZE ME

# # attribute example
# print(nums2.__class__) # <class 'str'> 

"""TypeError"""
# var1 = '10'
# var2 = 10
# print(var1 + var2) # TypeError: can only concatenate str (not "int") to str
# print(var2 + var1) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# colors = ['red', 'green', 'blue']
# print(colors[2.3]) # TypeError: list indices must be integers or slices, not float
# print(colors['1']) # TypeError: list indices must be integers or slices, not str

"""IndexError"""
# colors = ['red', 'green', 'blue']
# for i in range(4):
#     print(colors[i]) # IndexError: list index out of range

# message = 'hello world'
# print(message[4])
# print(message[11]) # IndexError: string index out of range

"""KeyError"""
# test = {'a': 1, 'b': 2, 'c': 3}
# print(test['a'])
# print(test['d']) # KeyError: 'd'

# keys = ['a', 'b', 'c', 'd', 'e']
# for key in keys:
#     value = test.get(key)
#     if value is not None:
#         print(key, value)
#     else:
#         print('no value for ' + key)

"""ValueError"""
# print(int('1'))
# print(int('one')) # ValueError: invalid literal for int() with base 10: 'one'

"""raising errors"""
# for i in range(20):
#     if i == 13:
#         raise ValueError('13 is unlucky') # ValueError: 13 is unlucky
#     print(i)

# raise Exception # this will just crash your code