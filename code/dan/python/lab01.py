distance = input ("What is the distance?")  
from_units = input ("What are the units?")
#to_units = input ("What are the output units?")

def converter (distance, from_units):
  if from_units == "ft": 
    x = (int(distance) * 0.3048)
    print (float(x)) 
  elif from_units == "km":
    x = (int(distance) * 1000)
    print (float(x))
  elif from_units == "mi":
    x = (int(distance) * 1609.34)
    print (float(x))

converter(distance, from_units)