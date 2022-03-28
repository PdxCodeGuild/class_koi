#version
list = []

while True: 
  x = input(
          "What number would you like to add to the list? If you are finished please type done "
    )
  counter = 0
  total = 0
  if x == "done":
    break
  else:
    list.append(int(x))
  for x in list:
    counter += 1
    total += x 
  print (list)
  print(total/counter)