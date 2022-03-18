# ver 1 ---- #

nums = [5, 0, 8, 3, 4, 1, 6]

for x in range(len(nums)):
    print(sum(nums) / len(nums))
    break

# ver 2 ---- #

nums = []

while True:
    num = input('Enter a number, or "done": ')
    if num == 'done':
        print(f'The average is {sum(nums) / len(nums)}') # average
        break

    nums.append(int(num)) # adding user input to list


