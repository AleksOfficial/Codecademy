def find_incorrect_val(array,max_numbers):
  values = array[0:max_numbers]
  start = max_numbers
  length = len(array)
  incorrect = False
  while(start != length-1):
    
    if start==332:
      print("hi")

    for j in range(max_numbers):
      incorrect = False
      search_val = abs(array[start]-values[j])
      if(search_val in values):
        break
      else:
        incorrect = True
    if incorrect:
      return start
    else:
      start+=1
      values = sorted(array[(start-max_numbers):start])
      
  print("no numbers found!")
  return 0

def find_list(array,inc_val):
  start = 1
  series = []
  total = 0
  j = 0
  while(42):
    total += array[-(start+j)]
    if(inc_val-total>0):
      series.append(array[-(start+j)])
      j+=1
    elif(total==inc_val):
      series.append(array[-(start+j)])
      return series
    else:
      j=0
      series = []
      total = 0
      start +=1

    



file = open("input.txt","r")
int_input =[]
input = 0
while (42):
  try:
    input = int(file.readline())
    int_input.append(input)
  except:
    break

index_incorrect = find_incorrect_val(int_input,25)
print(int_input[index_incorrect])
continuous_list = find_list(int_input[:index_incorrect],int_input[index_incorrect])
print(continuous_list)
val = min(continuous_list)+max(continuous_list)
print(val)


