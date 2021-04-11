path= "AOC\\Advent_of_Code_2019\\Day3_2019\\"
input_file = open(path+"Input.txt","r")
wires = input_file.readlines()

wire1 = wires[0].strip("\n").split(",")
wire2 = wires[1].strip("\n").split(",")

#takes way too long because of the 4 for-loops -> 
def get_crosssections(function_wire1,function_wire2):
    Crossings = []
    coordinates_wire1 = [0,0]
    for i in function_wire1:
        direction1 = i[0]
        amount1 = int(i[1:])
        for traveled1 in range(amount1):
            if direction1 =="R":
                coordinates_wire1[0]+=1
            elif direction1 =="L":
                coordinates_wire1[0]-=1
            elif direction1 =="U":
                coordinates_wire1[1]+=1
            elif direction1 =="D":
                coordinates_wire1[1]-=1
            coordinates_wire2 =[0,0]
            for y in function_wire2:
                direction2 = y[0]
                amount2 = int(y[1:])
                for traveled2 in range(amount2):
                    if direction2 =="R":
                        coordinates_wire2[0]+=1
                    elif direction2 =="L":
                        coordinates_wire2[0]-=1
                    elif direction2 =="U":
                        coordinates_wire2[1]+=1
                    elif direction2 =="D":
                        coordinates_wire2[1]-=1
                    if coordinates_wire1 == coordinates_wire2:
                        Crossings.append(tuple(coordinates_wire1[:]))
    return Crossings
#more efficient approach WAY MORE EFFICIENT HOLY MOLY COW
def new_list_of_points(function_wire):
    coordinate_list = []
    coordinates_wire1 = [0,0]
    for i in function_wire:
        direction1 = i[0]
        amount1 = int(i[1:])
        for traveled1 in range(amount1):
            if direction1 =="R":
                coordinates_wire1[0]+=1
            elif direction1 =="L":
                coordinates_wire1[0]-=1
            elif direction1 =="U":
                coordinates_wire1[1]+=1
            elif direction1 =="D":
                coordinates_wire1[1]-=1
            coordinate_list.append(tuple(coordinates_wire1[:]))

    return coordinate_list

def step_function(crossing_list,Wire1,Wire2):
    list_with_steps = [[] for x in range(len(crossing_list))]
    for i in range(len(crossing_list)):
        for j in Wire1:
            if j == crossing_list[i]:
                list_with_steps[i].append(Wire1.index(j)+1)
                break
        for j in Wire2:
            if j == crossing_list[i]:
                list_with_steps[i].append(Wire2.index(j)+1)
    return list_with_steps
            

def get_shortest_distance(Crosssections):
    minimum = None
    for x in Crosssections:
        if minimum is None:
            minimum = abs(x[0])+abs(x[1])
        elif minimum> abs(x[0])+abs(x[1]):
            minimum = abs(x[0])+abs(x[1])
    return minimum





test_wire_1 = ["R8","U5","L5","D3"]
test_wire_2 = ["U7","R6","D4","L4"]

Crosssections1 = get_crosssections(test_wire_1,test_wire_2)
shortest_distance1 = get_shortest_distance(Crosssections1)
print(Crosssections1)
print(step_function(Crosssections1,new_list_of_points(test_wire_1),new_list_of_points(test_wire_2)))
print(shortest_distance1)
shortest_amount_steps1=get_shortest_distance(step_function(Crosssections1,new_list_of_points(test_wire_1),new_list_of_points(test_wire_2)))
print(shortest_amount_steps1)



test_wire_3 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
test_wire_4 = "U62,R66,U55,R34,D71,R55,D58,R83"
#distance = 159
#steps = 610
test_wire_3 = test_wire_3.split(",")
test_wire_4 = test_wire_4.split(",")

Crosssections2 = get_crosssections(test_wire_3,test_wire_4)
shortest_distance2 = get_shortest_distance(Crosssections2)
print(shortest_distance2)
shortest_amount_steps2=get_shortest_distance(step_function(Crosssections2,new_list_of_points(test_wire_3),new_list_of_points(test_wire_4)))
print(shortest_amount_steps2)


test_wire_5 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
test_wire_6 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
test_wire_5 = test_wire_5.split(",")
test_wire_6 = test_wire_6.split(",")

Crosssections3 = get_crosssections(test_wire_5,test_wire_6)
shortest_distance3 = get_shortest_distance(Crosssections3)
print(shortest_distance3)
shortest_amount_steps3=get_shortest_distance(step_function(Crosssections3,new_list_of_points(test_wire_5),new_list_of_points(test_wire_6)))
print(shortest_amount_steps3)
#distance = 135
#steps = 410

# Crosssections4 = get_crosssections(test_wire_5,test_wire_6)
# shortest_distance4 = get_shortest_distance(Crosssections4)
# print(shortest_distance4)
# DIDNT WORK: TOO MUCH DATA AND THEREFORE TAKES TOO LONG
wire1_coordinates = tuple(new_list_of_points(wire1))
wire2_coordinates = tuple(new_list_of_points(wire2))
#get_crossings(wire1_coordinates,wire2_coordinates)
Crosssections4 = set(wire1_coordinates)&set(wire2_coordinates)
print(wire1_coordinates[3])
shortest_distance4 = get_shortest_distance(Crosssections4)
print(shortest_distance4)

Crosssection_steps = step_function(list(Crosssections4),wire1_coordinates,wire2_coordinates)
print(get_shortest_distance(Crosssection_steps))


#yay :) not the most efficient way. maybe you can make this more clever
