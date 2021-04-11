def is_tree(line,pos_x):
  if(line[pos_x]=='#'):
    return True
  else:
    return False

def count_trees(field,col_up,line_up):
  x=0
  line=line_up
  field_len=len(field[0])
  hitcount=0
  for _ in field:
    x+=col_up
    #print(x)
    if(x>=field_len):
      x-=(field_len)
    if(line>=len(field)):
      break
    if(is_tree(field[line],x)):
      hitcount+=1
    line+=line_up
  return hitcount

#Aufgabe 1
test = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""
test_field = test.split("\n")
file = open("input.txt","r")
field = file.read().split("\n")


test_=0
test = count_trees(test_field,3,1)
hitcount= count_trees(field,3,1)
print(test)
print(hitcount)
print("---------------------")
#Aufgabe 2 
cols=[1,3,5,7,1]
lines=[1,1,1,1,2]
test_hit = 1
trees_hit=1

tmp=0
for i in range(5):
  
  tmp=count_trees(test_field,cols[i],lines[i])
  print(tmp)
  test_hit*=tmp
  tmp=count_trees(field,cols[i],lines[i])
  print(tmp)
  trees_hit*=tmp

print(test_hit)
print(trees_hit)
