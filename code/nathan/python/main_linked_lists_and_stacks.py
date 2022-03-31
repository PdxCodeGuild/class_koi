from linked_lists_and_stacks import Stack, LinkedList

s = Stack()
s.push(5)
s.push(6)
print(s)
print(s.length()) # 2
print(s.pop()) # 6
print(s.pop()) # 5

# nums = LinkedList()
# nums.append(5)
# nums.append(6)
# nums.insert(7, 0)
# print(nums) # [7, 5, 6]
# print(nums.find(5)) # 1
# nums.remove(5)
# print(nums) # [7, 6]
# print(nums.length()) # 2