path= "AOC\\Advent_of_Code_2019\\Day1_2019\\"
with open(path+"input.txt","r") as input_file:
    input = input_file.readlines()
for i in range(len(input)):
    input[i].strip("\n")
    input[i]=int(input[i])

def fuelcount(fuel):
    fuel = fuel//3-2
    if fuel <5 and fuel >0:
        return fuel
    elif fuel <= 0:
        return 0
    else:
        return fuel + fuelcount(fuel)

first_total_fuel = 0

for i in input:
    first_total_fuel+= i//3-2        

#print(input)
total_fuel = 0
fuel = 0
example = 68936
my_fuel= fuelcount(example)
print(my_fuel)


for i in input:
    fuel = fuelcount(i)
    total_fuel+=fuel

print(total_fuel)






# Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

# For example:

#     For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.