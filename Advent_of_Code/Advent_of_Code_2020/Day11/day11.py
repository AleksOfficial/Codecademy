import time
import os
clear = lambda: os.system('cls')

def return_closest_element(seats,pos_x,pos_y,increment_x,increment_y,width,length):
  val = "."
  while(42):
    if (pos_x==0 and increment_x<0):
      break
    if (pos_y == 0 and increment_y<0):
      break
    if (pos_x==width-1 and increment_x>0):
      break
    if (pos_y== length-1 and increment_y>0):
      break
    pos_x+=increment_x
    pos_y+=increment_y
    if(seats[pos_y][pos_x] == '#' or seats[pos_y][pos_x] == 'L' ):
      val = seats[pos_y][pos_x]
      break
  return val
  
# if(pos_x)

'''
check if pos_x = 0 or width
if so and increment is equal to the direction it is travelling then return .
Same applies for pos_y
also check the increment
then loop through while the seats at posy posx == # or L and isnt first move;
you could also set the return val as . and change it accordingly. also perhaps a variable that switches to true/false if a
value has been assigned.
'''
  
    
# Perhaps it would help if this function, instead of checking the adj vals,
# it could use the linear travel function above to traverse the list and determine the compare value
# if dict check left is true, then determine the value for left pos; and then for each other checking val in the dict, move accordingly

def check_function_linear(seats, pos_x, pos_y, dict_check_pos, cmp,width, legnth):
      occupations = 0
      if(dict_check_pos["left"]): 
        val = return_closest_element(seats,pos_x,pos_y,-1,0,width,length)
        if(val == cmp):
          occupations += 1
        if(dict_check_pos["top"]):
          val = return_closest_element(seats,pos_x,pos_y,-1,-1,width,length)
          if(val == cmp):
            occupations += 1
        if(dict_check_pos["bottom"]):
          val = return_closest_element(seats,pos_x,pos_y,-1,1,width,length)
          if(val == cmp):
            occupations += 1
      if(dict_check_pos["top"]):
        val = return_closest_element(seats,pos_x,pos_y,0,-1,width,length)
        if(val == cmp):
            occupations += 1
        if(dict_check_pos["right"]):
          val = return_closest_element(seats,pos_x,pos_y,1,-1,width,length)
          if(val == cmp):
            occupations += 1
      if(dict_check_pos["bottom"]):
        val = return_closest_element(seats,pos_x,pos_y,0,1,width,length)
        if(val == cmp):
            occupations += 1
        if(dict_check_pos["right"]):
          val = return_closest_element(seats,pos_x,pos_y,1,1,width,length)
          if(val == cmp):
            occupations += 1
      if(dict_check_pos["right"]):
        val = return_closest_element(seats,pos_x,pos_y,1,0,width,length)
        if(val== cmp):
          occupations += 1
      return occupations
  
def check_function_adj(seats, pos_x, pos_y, dict_check_pos, cmp):
      occupations = 0
      if(dict_check_pos["left"]): 
        if(seats[pos_y][pos_x-1] == cmp):
          occupations += 1
        if(dict_check_pos["top"]):
          if(seats[pos_y-1][pos_x-1] == cmp):
            occupations += 1
        if(dict_check_pos["bottom"]):
          if(seats[pos_y+1][pos_x-1] == cmp):
            occupations += 1
      if(dict_check_pos["top"]):
        if(seats[pos_y-1][pos_x] == cmp):
            occupations += 1
        if(dict_check_pos["right"]):
          if(seats[pos_y-1][pos_x+1] == cmp):
            occupations += 1
      if(dict_check_pos["bottom"]):
        if(seats[pos_y+1][pos_x] == cmp):
            occupations += 1
        if(dict_check_pos["right"]):
          if(seats[pos_y+1][pos_x+1] == cmp):
            occupations += 1
      if(dict_check_pos["right"]):
          if(seats[pos_y][pos_x+1] == cmp):
            occupations += 1
      return occupations

def set_checks(seats, position_x, position_y, width, length):
    positions = {}
    positions['left'] = False
    positions['right'] = False
    positions['top'] = False
    positions['bottom'] = False
    if(position_x > 0):
        positions['left'] = True
    if(position_y > 0):
        positions['top'] = True
    if(position_x < width-1):
        positions['right'] = True
    if(position_y < length-1):
        positions['bottom'] = True
    return positions

def changing_seats(seats, width, length):
    count = 0
    seats_copy = seats[:]

    while(42):
      #clear()
      #for j in seats:
        #print(j)
      #time.sleep(0.2)
      changed = False
      positions = {}
      for i in range(length):
        for j in range(width):
          if(seats[i][j] == '.'):
            continue
          positions = set_checks(seats, j, i, width, length)
          if(seats[i][j] == 'L'):
              num = check_function_linear(seats, j, i, positions, '#',width,length) #changed to linear
              if(num == 0):
                update = list(seats_copy[i])
                update[j]='#'
                seats_copy[i]="".join(update)
                count+=1
                changed = True
          if(seats[i][j] == '#'):
              num = check_function_linear(seats, j, i, positions, '#',width,length) #changed to linear
              if(num >= 5): # 5 instead of 4 as before
                update = list(seats_copy[i])
                update[j]='L'
                seats_copy[i]="".join(update)
                count-=1
                changed = True
      seats = seats_copy[:]
      if(not changed):
        break
    return count


file = open("input.txt", "r")
input = file.read().split("\n")
width = len(input[0])
length = len(input)
print(changing_seats(input,width,length))
