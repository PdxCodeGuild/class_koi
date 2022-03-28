'''
We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum', then divide that sum by the number of elements in that list. 
'''

def versionOne():
    nums = [5, 0, 8, 3, 4, 1, 6]
    sum = 0
    for num in nums:
        sum += num
    print(sum / len(nums))
    return


# Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', then calculate and display the average.
def versionTwo():
    nums = []
    userInput = ''
    sum = 0
    while(userInput != 'done'):
        userInput = input("Enter a number or 'done' to quit: ")
        if(userInput != 'done'):
            nums.append(int(userInput))
    for num in nums:
        sum += num
    print(sum / len(nums))
    return

print("\n***\nLab02 Version 1:\n***\n")
versionOne()

print("\n***\nLab02 Version 2:\n***\n")
versionTwo()