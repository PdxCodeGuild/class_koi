# Version 1 Lab 09
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


#empty list to append peaks & valleys
peaks_and_valleys = []

# empty list to append
peaks_list=[]
def find_peaks(data):
    #finds peaks add to list
    for x in range (1,19):
            if data[x] > data[x-1] and data[x] > data[x+1]:
             peaks_list.append(x)
            print (peaks_list)
  
 #empty list to append        
valleys_list = []        
def find_valleys(data):
    #find valleys add to list
    for x in range(1,len(data)):
        if data[x] < data[x-1] and  data[x] < data[x+1]:
            valleys_list.append(x) 
        print (valleys_list)
    
#empty list to append    
peaks_and_valleys = []   
def find_peaks_valleys(data):
    for x in range (1,19):
        if data[x] < data[x-1] and  data[x] < data[x+1]:
            peaks_and_valleys.append(x)
        if data[x] > data[x-1] and data[x] > data[x+1]:
             peaks_and_valleys.append(x)
        print (peaks_and_valleys)
        
        
find_peaks_valleys(data)    
find_peaks(data)
find_valleys(data)   