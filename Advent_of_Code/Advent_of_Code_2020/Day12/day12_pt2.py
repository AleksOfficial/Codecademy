import math
file = open("input.txt","r")
input = file.read().split("\n")
'''


    Action N means to move the waypoint north by the given value.
    Action S means to move the waypoint south by the given value.
    Action E means to move the waypoint east by the given value.
    Action W means to move the waypoint west by the given value.
    Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
    Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
    Action F means to move forward to the waypoint a number of times equal to the given value.

    
    // North = 0East = 1; South = 2; West = 3;
'''
waypoint = [1,10,0,0]
position = [0,0]
facing = 1
for i in input:
  instruction = i[0]
  if(instruction in "LR"):
    degrees = int(int(i[1:])/90)
    for i in range(degrees):
      if(instruction =="L"):
        new_waypoint =[0,0,0,0]
        new_waypoint[0]=waypoint[1]
        new_waypoint[1]=waypoint[2]
        new_waypoint[2]=waypoint[3]
        new_waypoint[3]=waypoint[0]
        waypoint = new_waypoint
      else:
        new_waypoint = [0,0,0,0]
        new_waypoint[1] = waypoint[0]
        new_waypoint[2] = waypoint[1]
        new_waypoint[3] = waypoint[2]
        new_waypoint[0] = waypoint[3]
        waypoint = new_waypoint
  elif(instruction in "FR"):
    amount = int(i[1:])
    if instruction == "F":
      position[0] += amount* (waypoint[0]-waypoint[2])
      position[1] += amount * (waypoint[1]-waypoint[3])
    else:
      position[0] -= amount * (waypoint[0]-waypoint[2])
      position[1] -= aomunt * (waypoint[1]-waypoint[3])
      
  elif(instruction in "NESW"):
    addition = int(i[1:])
    instruction = instruction.replace("N","0")
    instruction = instruction.replace("E","1")
    instruction = instruction.replace("S","2")
    instruction = instruction.replace("W","3")
    index = int(instruction)
    waypoint[index]+=addition


distance = abs(position[0])+abs(position[1])
print(distance) 
        
    
  
    
    
    