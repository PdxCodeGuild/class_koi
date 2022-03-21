# # Version 1

nums = [5, 0, 8, 3, 4, 1, 6]
sums = 0

for i in nums:
    sums += i

print(nums)

print(sums / len(nums))


# Version2

nums = []
user_input = ""
sums = 0

while True:
    user_input = input('Add a number to the list. Type done to calculate the average. ')

    if user_input == "done":    
        for i in nums:
            sums += i
            
        print("The average of all numbers is:")
        print(sums / len(nums))
        break

    nums.append(int(user_input))
    print(nums)