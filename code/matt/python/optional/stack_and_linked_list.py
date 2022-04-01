'''
PDX Code Guild - Class Koi
Optional Lab - Stack and Linked List
Matt Walsh
'''

 
# Part 1: Stack

class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

    def __str__(self):
        return f'({self.item}, {self.next})'


class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, element): # insert an element at the start (new head)
        
        self.next = self.head
        self.head = element
    
    def pop(self): # remove an element from the start (the head becomes the next node)
        ...
    
    def peek(self): # returns the element on the head node or None if there is no head
        ...
    
    def __len__(self): # return the number of elements
        ...

    def to_list(self):
        ...
    
    def __str__(self):
        return #f'{self.head}, {self.next}'



s = Stack()
s.push(5)
s.push(6)
# print(s.length()) # 2
# print(s.pop()) # 6
# print(s.pop()) # 5
print(s)