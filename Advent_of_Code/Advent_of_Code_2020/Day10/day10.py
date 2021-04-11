import math
'''
def possibilities(index, array):
  #return the amount of possibilities to connect
  counter = 1
  val = array[index]
  if(val+1 in array):
    counter +=1
  if(val+2 in array):
    counter +=1
  if(val+3 in array):
    counter +=1
  if counter !=1:
    return counter-1
  else: return 1


def geo_series_possiblities(array):
  total =0
  for i in range(len(array)):
    if total==0:
      total = possibilities(i,array)
    else:
      total += possibilities(i,array)
  print(total)
  n=math.factorial(total)
  print(n)
  divisor=math.factorial((total-len(array))*len(array))
  return n/divisor
'''


def recursive_approach(array,val,target):
  total = 0
  if val == target:
    return 1
  if(val-1 in array):
    total+=recursive_approach(array,val-1,target)
  if(val-2 in array):
    total += recursive_approach(array,val-2,target)
  if(val-3 in array):
    total += recursive_approach(array,val-3,target)
  return total

def list_mulitply(array,crit_vertex):
  for i in range(len(crit_vertex)):
    if(i == 0):
      total = recursive_approach(array[0:crit_vertex[i]],array[crit_vertex[i]],0)
    else:
      total *= recursive_approach(array[crit_vertex[i-1]:crit_vertex[i]],array[crit_vertex[i]],array[crit_vertex[i-1]])
  return total
file = open("input.txt","r")
int_input = []
while(42):
  try:
    x = int(file.readline())
    int_input.append(x)
  except:
    break
int_input.append(0)
int_input.sort()
int_input.append(int_input[-1]+3)
print(int_input)
jolts = [0,0,0]
jolt3=[]
jolt1=[]
for i in range(len(int_input)-1):
  x =int_input[i+1]-int_input[i]   
  if(x==1):
    jolt1.append(i+1)
  elif(x == 3):
    jolt3.append(i+1)
  jolts[x-1]+=1

print(jolts)
print(jolts[0]*jolts[2])
print(jolt1)
print(jolt3)
#print(geo_series_possiblities(int_input))
x = list_mulitply(int_input,jolt3)
print(x)