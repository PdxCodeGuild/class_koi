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
        new_node = Node(element)
        if(not(self.head)):
            self.head = new_node
            return self.head
        new_node.next = self.head
        self.head = new_node
        return self.head
    
    def pop(self): # remove an element from the start (the head becomes the next node)
        if(not(self.head)):
            return None
        
        temp_value = self.head
        self.head = self.head.next

        return temp_value.item
    
    def peek(self): # returns the element on the head node or None if there is no head
        if(not(self.head)):
            return None
        
        return self.head
    
    def length(self): # return the number of elements
        if(not(self.head)):
            return None
        
        count = 0
        current = self.head
        while(current):
            current = current.next
            count += 1
        return count

    def to_list(self):
        if(not(self.head)):
            return None
        
        temp_list = []
        current = self.head
        while(current):
            temp_list.append(current.item)
            current = current.next
        return temp_list
    
    
    def __str__(self):
        if(not(self.head)):
            return None
        
        s = ''
        current = self.head
        while(current):
            s += f"{current.item}\n"
            current = current.next
        return s
    
class LinkedList:
    def __init__(self):
        self.head = None

    def append(element): # add the element to the end
        ...
            

    def insert(element, index): # insert the element at the given index
        ...

    def remove(element): # remove the first occurrence of the element
        ...

    def get(index): # get the element at the given index (starting with 0)
        ...

    def find(element): # find the first occurrence of the element and return it
        ...

    def length(self): # return the length of the list
        ...