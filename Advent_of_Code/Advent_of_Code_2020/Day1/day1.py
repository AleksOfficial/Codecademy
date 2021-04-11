file = open("input.txt","r")
array = file.read().split("\n")
new_array=[] #this will be the same array saved as an integer array. In order to be more efficient, I save the values while iterating through
test_array = {1721,979,366,299,675,1456}
z2=0
z1=z2

#Exercise 1 done
"""
for i in array:
  for j in array:
    if(int(i)+int(j)==2020):
      z1 = int(i)
      z2 = int(j)
      

print("z1 = {}, z2 = {}".format(z1,z2))
"""

#Exercise 2
array_2=[]
for i in array:
  new_array.append(int(i))
  for j in array:
      z1 = int(i)
      z2 = int(j)
      if(z1+z2>2020):
        continue
      else:
        z3=2020-z1-z2
        array_2.append(z3)

      
#print(array_2)
intersection=set(array_2) & set(new_array)
print(intersection)
numbers=list(intersection)
total = numbers[0]*numbers[1]*numbers[2]
print(total)

