def find_searchval(input_string,row_selection,lower_selector):
  #print(input_string)
  if(len(input_string)==1):
    if(input_string==lower_selector):
      return row_selection[0]
    else:
      return row_selection[1]
  selector = input_string[0]
  adder = (row_selection[1]-row_selection[0])/2
  if(adder%2>0):
    adder = int(adder+1)
  else:
    adder = int(adder)
  if(selector == lower_selector):
    return(find_searchval(input_string[1:],[row_selection[0],row_selection[1]-adder],lower_selector))
  else:
    return(find_searchval(input_string[1:],[row_selection[0]+adder,row_selection[1]],lower_selector))
#########################
test ="FBFBBFFRLR"
test1="BFFFBBFRRR"
test2="FFFBBBFRRR"
test3="BBFFBBFRLL"


file = open("input.txt","r")
input = file.read().split("\n")
#Tests
print(find_searchval(test[:7],[0,127],"F"))
print(find_searchval(test[7:],[0,7],"L"))
# Aufgabe 1
max = 0
for i in input:
  row = find_searchval(i[:7],[0,127],'F')
  col = find_searchval(i[7:],[0,7],'L')
  id=col+row*8
  print(id)
  if(max<id):
    max = id
print(max)

# Aufgabe 2
all_seats=[]
for i in input:
  row = find_searchval(i[:7],[0,127],'F')
  col = find_searchval(i[7:],[0,7],'L')
  id=col+row*8
  all_seats.append(id)

all_seats.sort()
for i in range(len(all_seats)-1):
  if(all_seats[i]+1 == all_seats[i+1]-1):
    print(all_seats[i]+1)
    break




