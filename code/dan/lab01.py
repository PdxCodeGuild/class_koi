# Below is Version 1 & 2

#distance = input ("What is the distance?")  
#from_units = input ("What are the units?")
#to_units = input ("What are the output units?")

#def converter (distance, from_units):
 # if from_units == "ft": 
  #  x = (int(distance) * 0.3048)
   # print (float(x)) 
  #elif from_units == "km":
   # x = (int(distance) * 1000)
    #print (float(x))
  #elif from_units == "mi":
   # x = (int(distance) * 1609.34)
    #print (float(x))

# converter(distance, from_units)



# Version 3 & 4 

dict = {
    'in':.0254,
    'ft':.3048,
    'yd':.9144,
    'mi':1609.34,
    'm':1,
    'km':1000
}

distance = input('Please enter a value ')
start = input("Please enter a unit of measurement")
end = input("Please enter the unit of measurement you'd like to convet to")

if start in dict.keys():
  print ("That is a correct unit of measurement")

if distance in dict.values():
  print ("Please choose a different value")

print (float(distance) * dict[start] / dict[end])