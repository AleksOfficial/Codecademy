# Aufgabe 1
def execute_cmd(cmd):
  global instructor
  global acc
  operator = cmd[0]
  val = int(cmd[1])
  if(operator == 'nop'):
    instructor+=1
  if(operator == 'acc'):
    acc +=val
    instructor +=1
  if(operator == 'jmp'):
    instructor +=val
  return  



file = open("input.txt","r")
acc = 0
instructor = 0

# Aufgabe 1
'''
input = file.read().split("\n")
lib = [0 for x in range(len(input))]
while(42):
  cmd = input[instructor].split(" ")
  if(lib[instructor]):
    print("ACCUMULATOR VALUE: ")
    print(acc)
    exit(0)
  else: 
    lib[instructor]=1
    execute_cmd(cmd)
'''
# Aufgabe 2
input = file.read().split("\n")
length = len(input)
updated_input = [x.split(" ") for x in input]


for i in range(length):
  lib = {} #With the dictionary it's possibly faster
  acc = 0
  instructor = 0
  if(updated_input[i][0]== "jmp"):
    updated_input[i][0]="nop"
  elif(updated_input[i][0]=="nop"):
    updated_input[i][0] = "jmp"
  else:
      continue
  while(42):
    if(length-1 == instructor):
      print("ACCUMULATOR VALUE: ")
      print(acc)
      exit(0)
    try:
      if lib[instructor]:
        break
    except:
      cmd = updated_input[instructor]
      lib[instructor]=1
      execute_cmd(cmd)    
  if(updated_input[i][0]== "jmp"):
    updated_input[i][0]="nop"
  elif(updated_input[i][0]=="nop"):
    updated_input[i][0] = "jmp"