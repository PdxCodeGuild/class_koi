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
        
        # s = ''
        # current = self.head
        # while(current):
        #     s += f"{current.item}\n"
        #     current = current.next
        s = '['
        current = self.head
        while(current):
            s += f"{current.item}"
            current = current.next
        s += ']'
        return s
    
class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if(not(self.head)):
            return None
        
        s = '['
        current = self.head
        while(current):
            s += f"{current.item}"
            current = current.next
        s += ']'
        return s

    def append(self, element): # add the element to the end
        new_node = Node(element)

        if(not(self.head)):
            self.head = new_node
            return self.head
        
        current = self.head
        while(current.next):
            current = current.next
        
        current.next = new_node

        return new_node.item

    def insert(self, element, index): # insert the element at the given index
        # return codes: 1 = successful, None = unsuccessful
        if(not(self.head)):
            return None
        
        if(index > self.length()):
            return None

        if(index == 0):
            new_node = Node(element)
            # new_node.next = self.head
            # new_node = self.head
            new_node.next = self.head
            self.head = new_node
            return 1

        count = 0
        current = self.head
        while(current):
            current = current.next
            count += 1

        new_node = Node(element)
        current = new_node.next
        return 1

    def remove(self, element): # remove the first occurrence of the element
        # return codes: 1 = successful, None = unsuccessful/element doesn't exist
        if(not(self.head)):
            return None
        
        if(self.head == element):
            self.head = None
            self.head.next = self.head
            return 1
        
        current = self.head.next
        temp_node = self.head
        while(current and current.item != element):
            temp_node = current
            current = current.next
        if(current == None):
            return None
        temp_node.next = current.next
        current = None
        return 1

    def get(self, index): # get the element at the given index (starting with 0)
        if(not(self.head)):
            return None
        
        if(index > self.length()):
            return None

        count = 0
        current = self.head
        while(current and count <= index):
            current = current.next
            count += 1
        return current.item

    def find(self, element): # find the first occurrence of the element and return it
        # return index of element***
        if(not(self.head)):
            return None
        
        count = 0
        current = self.head
        while(current and current.item != element):
            current = current.next
            count += 1
        if(current == None):
            return None

        return count

    def length(self): # return the length of the list
        if(not(self.head)):
            return None

        count = 0
        current = self.head
        while(current):
            current = current.next
            count += 1
        return count