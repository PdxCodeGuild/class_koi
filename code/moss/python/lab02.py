#-----Version 1-----#

print('\nVersion 1: Average of provided list of numbers.\n')

nums = [5, 0, 8, 3, 4, 1, 6]

total = 0

# looping over elements
# for num in nums:
#     total+= num
#     print (num)

# looping over indices
for i in range(len(nums)):
    total +=nums[i]
    print(nums[i])

avrg = round(total/len(nums),2)

print (f'\nThe average of the listed numbers is : {avrg}\n')

#-----Version 2-----#
print('__________________________________________________________')
print('\nVersion 2 : Average of numbers provided by the user.\n')
print('\nWelcome to the averaging tool.\n')
user_num_list = []

while True:
    user_num = input("\nEnter your number or 'done' to quit:\n")

    if user_num =='done':
        answer = round(sum(user_num_list)/len(user_num_list),2)
        print(f'\nNumbers provided : {user_num_list}\n')
        print(f'\nThe average of the numbers is : {answer}\n')
        break

    else :
        user_num = int(user_num)
        user_num_list.append(user_num)
