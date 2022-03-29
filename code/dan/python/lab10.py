# Version 1 

# Prompt user for random string
user_prompt = input ('What is the weather like today?: ')
print(user_prompt)


#Function takes in a string and encrypts it with ROT13 
def rot_13(user_prompt):
        letters = "abcdefghjklimnopqrstuvwxyz"
        encrypted_string = ""         # Empty string to add 

        for char in user_prompt:
            encrypted_string += letters[(letters.find(char)+13)%26]
    
        return encrypted_string 



print(rot_13(user_prompt))
