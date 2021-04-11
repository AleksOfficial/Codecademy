file = open("input.txt","r")
input = file.read().split("\n")
bus_string = input[1]
_busses = bus_string.split(",")
busses =[]
distances = []
distance = 0
for bus in _busses:
  if(bus!="x"):
    busses.append(int(bus))
    distances.append(distance)
    distance += 1
  else:
    distance +=1
  
print(busses)
print(distances)
length = len(busses)
max_id = 0
index = 0
for i in range(length):
  if(max_id<busses[i]):
    max_id = busses[i]
    index = i
j = max_id * 215982721382
print("max_id: {}".format(max_id))
print("at index: {}".format(index))
found = False
while(not found):
  #print(j)
  first_half = False
  for i in range(length+1):
    if(first_half):
      break
    if(i == length):
      found = True
      print(j-distances[index])
      #print(j)
      break
    
    if(i <index):
      for x in range(index):
        #print(str(j-distances[(index-x)])+" divided by "+str(busses[x]))
        
        if((j-distances[index]+distances[x])%busses[x]  ==0):
          print(str(j-distances[index]+distances[x])+" divided by "+str( busses[x]) + " equals "+str((j-distances[index]+distances[x])/busses[x]) )
          continue
        else:
          first_half = True
          break
    elif(i == index):
      continue
    else:      
      if((j+distances[i]-distances[index])%busses[i] ==0):
        print(str(j+distances[i]-distances[index])+" divided by "+str( busses[i]) + " equals "+str((j+distances[i]-distances[index])/busses[i]) )
        continue

      else:
        break
  j += max_id

'''
t + d1 = a1 * id1
t + d2 = a2 * id2
t + d3 = a3 * id3

    Bus ID 7 departs at timestamp t.
    Bus ID 13 departs one minute after timestamp t.
    There are no requirements or restrictions on departures at two or three minutes after timestamp t.
    Bus ID 59 departs four minutes after timestamp t.
    There are no requirements or restrictions on departures at five minutes after timestamp t.
    Bus ID 31 departs six minutes after timestamp t.
    Bus ID 19 departs seven minutes after timestamp t.
'''
