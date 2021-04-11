def valid_pw(input_string):
  splitted = input_string.split(" ")
  constraints=splitted[0].split("-")
  min = int(constraints[0])
  max = int(constraints[1])
  password = splitted[2]
  search_char= splitted[1][0]
  if password.count(search_char)>=min and password.count(search_char) <= max:
    return True
  else:
    return False

def valid_pw2(input_string):
  splitted = input_string.split(" ")
  constraints=splitted[0].split("-")
  index1 = int(constraints[0])-1
  index2 = int(constraints[1])-1
  password = splitted[2]
  search_char= splitted[1][0]
  if(password[index1] == search_char or password[index2] == search_char):
    if(password[index1]==password[index2]):
      return False
    else:
      return True
  else:
    return False


FILE = open("input.txt","r")
input = FILE.read().split("\n")
print(input)
amount_valids=0
new_amount_valids=0
#Aufgabe 1
for i in input:
  if(valid_pw(i)):
    amount_valids+=1

#Aufgabe 2

for i in input:
  if(valid_pw2(i)):
    new_amount_valids+=1

print(new_amount_valids)
