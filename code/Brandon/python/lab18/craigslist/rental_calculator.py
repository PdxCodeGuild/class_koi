import csv

print('------------------------------------------------------------------------------')   

x=[]
i=0
price_average = 0

with open('C:\\Users\\Brandon\\Desktop\\PDXCode\\class_koi\\code\\brandon\\python\\lab18\\craigslist\\one_bedroom.csv', 'r') as f:
    rooms = csv.reader(f)
    room_list = list(rooms)

for items in room_list:
    x.append(items)

for i in x:    # Deltes when location not provided
    if 'na' in i:
        del i[:]

for i in x:
    new_rooms = [a for a in x if a]  #taken from stackoverflow: removes empty lists



updated_room_price = []

for i in new_rooms[1:40]:          #removes $ and , to calculate average, removes listings over 2600 and under 500
    a = i[1].lstrip('$')
    if ',' in a:
        a = a.replace(",", "")
    a = int(a)
    if a < 2600 and a > 700:
        updated_room_price.append(a)

updated_room_price[:1].sort()      
rental_average = sum(updated_room_price) / len(updated_room_price)
rental_average = int(rental_average)
print(f'1 BR rental average: ${rental_average}\n1 BR rental units: {len(updated_room_price)}\n1 BR lowest prices: ${updated_room_price[:10]}')

print('------------------------------------------------------------------------------')   

y=[]

with open('C:\\Users\\Brandon\\Desktop\\PDXCode\\class_koi\\code\\brandon\\python\\lab18\\craigslist\\two_bedroom.csv', 'r') as file:
    rooms2 = csv.reader(file)
    room_list2 = list(rooms2)

for items in room_list2: 
    y.append(items)
          
for i in y:    # Deltes when location not provided
    if 'na' in i:
        del i[:]

for i in y:
    new_rooms2 = [a for a in y if a]  #taken from stackoverflow: removes empty lists

updated_room_price2 = []



for i in new_rooms2[1:40]:          #removes $ and , to calculate average, removes listings over 2600 and under 800
    c = i[1].lstrip('$')
    if ',' in c:
        c = c.replace(",", "")
    c = int(c)
    if c < 3000 and c > 800:
        updated_room_price2.append(c)

updated_room_price2.sort()

rental_average2 = sum(updated_room_price2) / len(updated_room_price2)
rental_average2 = int(rental_average2)
print(f'2 BR rental average: ${rental_average2}\n2 BR rental units: {len(updated_room_price2)}\n2 BR lowest prices: ${updated_room_price2[:10]}')

print('------------------------------------------------------------------------------')   

updated_rooms_2 = []
while True:
    user_input = input('Do you want to see all listings for 1BR or 2BR? Type 1BR, 2BR, or exit. ').title()
    
    if user_input == '1Br':
        
            # new_rooms.sort()
        for i in new_rooms:    # Deltes when location not provided
            if 'na' in i:
                del i[:]
            if i in new_rooms:    # Deltes duplicates
                del i
        for i in new_rooms[1:30]:
            print(i)
        print('------------------------------------------------------------------------------')        

    if user_input == '2Br':
        
        for i in new_rooms2:    # Deletes when location not provided
            if 'na' in i:
                del i[:]
            if i in new_rooms2: # Deltes duplicates
                del i
                
        for i in new_rooms2[1:30]:
            print(i)
        
        print('------------------------------------------------------------------------------')      

    if user_input == 'Exit':
        break    