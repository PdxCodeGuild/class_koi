'''
Version 1

if result decimel round up 

'''



ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}


with open('food_of_war.txt','r',) as f:
     contents = f.read()
     lines = contents.split('.')
     words = contents.split(' ')
     
     print (contents)
     # number of sentences
     sentence_count = 0
     for line in range (0,len(lines)):
         sentence_count += 1
         print(sentence_count)
       
       # counts number of words
     word_count = 0 
     for word in range (0, len(words)):
         word_count += 1
         print (word_count)
        
     # counts number of charachters 
     chars = 0
     for x in range(0,len(contents)):
         chars += 1
         print (chars)
      
     ari = ((chars / word_count) * 4.71) + ((word_count/sentence_count) * .5) - 21.43   
     print (ari) 
     # round answer logic
     if ari >= 14:
        ari_num = int(ari)
        print(ari_num)
     elif ari % 1 == 0:
        ari_final = int(ari) + 1 
        print(ari_final)


# These are bork, need to fix       
print(f"The ARI score is {ari_num}")
 
print(f"This corresponds with a {ari_scale[ari_num]['grade_level']} reading level")

print(f"This is suitable for someone ages {ari_scale[ari_num]["ages"]}")