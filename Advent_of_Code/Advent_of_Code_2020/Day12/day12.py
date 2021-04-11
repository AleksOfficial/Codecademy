import math
file = open("input.txt","r")
input = file.read().split("\n")
'''

    Action N means to move north by the given value.
    Action S means to move south by the given value.
    Action E means to move east by the given value.
    Action W means to move west by the given value.
    Action L means to turn left the given number of degrees.
    Action R means to turn right the given number of degrees.
    Action F means to move forward by the given value in the direction the ship is currently facing.
    
    // North = 0East = 1; South = 2; West = 3;
'''
position = [0,0,0,0]
facing = 1
for i in input:
  instruction = i[0]
  if(instruction in "LR"):
    degrees = int(int(i[1:])/90)
    if(instruction =="L"):
      degrees*=-1
    facing+=degrees
    facing = facing%4
  elif(instruction in "FR"):
    addition = int(i[1:])
    position[facing]+=addition
  elif(instruction in "NESW"):
    addition = int(i[1:])
    instruction = instruction.replace("N","0")
    instruction = instruction.replace("E","1")
    instruction = instruction.replace("S","2")
    instruction = instruction.replace("W","3")
    index = int(instruction)
    position[index]+=addition

final_coordinates = [position[0]-position[2],position[1]-position[3]]

distance = abs(final_coordinates[0])+abs(final_coordinates[1])
print(distance) 
        
    
  
    
    
    