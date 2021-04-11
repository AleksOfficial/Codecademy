#1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,6,23,2,23,13,27,1,27,5,31,2,31,10,35,1,9,35,39,1,39,9,43,2,9,43,47,1,5,47,51,2,13,51,55,1,55,9,59,2,6,59,63,1,63,5,67,1,10,67,71,1,71,10,75,2,75,13,79,2,79,13,83,1,5,83,87,1,87,6,91,2,91,13,95,1,5,95,99,1,99,2,103,1,103,6,0,99,2,14,0,0

path= "AOC\\Advent_of_Code_2019\\Day2_2019\\"
with open(path+"input.txt","r") as input_file:
    new_input = input_file.readline()
updated_input = new_input.split(",")
input_file = []
for i in updated_input:
    input_file.append(int(i))
input_file[2] = 2
input_file[1] = 12
before_input_file = input_file[:]
# print("before:\n")
# print(before_input_file)

# index_value = 0
# index = 0
# position1 = 0
# position2 = 0
# result_position = 0
target_result = 19690720

for pos1 in range(100):
    for pos2 in range(100):
        input_file =before_input_file[:]
        input_file[1] = pos1
        input_file[2] = pos2
        index_value = 0
        index = 0
        position1 = 0
        position2 = 0
        result_position = 0
        
        while index_value != 99:
            index_value = input_file[index]
            position1 = input_file[index+1]
            position2 = input_file[index+2]
            result_position = input_file[index+3]
            if index_value == 1:
                input_file[result_position] = input_file[position1]+input_file[position2]
            elif index_value == 2:
                input_file[result_position] = input_file[position1]*input_file[position2]
            else:
                break
            index+=4
        if input_file[0] == target_result:
            print(f"pos1 = {pos1}, pos2 = {pos2} ")
            break
            

        
#print(f"pos1 = {pos1}, pos2 = {pos2} ")


# print("After:\n")
# print(input_file)

# print(test)
# while index_value != 99:
#     index_value = test[index]
#     position1 = test[index+1]
#     position2 = test[index+2]
#     result_position = test[index+3]
#     if index_value == 1:
#         test[result_position] = test[position1]+test[position2]
#     elif index_value == 2:
#         test[result_position] = test[position1]*test[position2]
#     index+=4
#     index_value = test[index]
# print(test)

#OpCode: Operation - Position1 - Position2 - Resultposition
# Operations: 1 = Addition; 2 = Multiplication; 99 = Halt; Positions: Like in an Array
# 1,9,10,3, -> Add position 9 (30) and position 10 (40) together and save at position 3 (3)
# 2,3,11,0, -> Multiply position 3 (30+40) with position 11 (50) and save at position 0 (1) 
# 99, -> Halt
# 30,40,50

#70*50,9,10,30+40,2,3,11,0,!99!,30,40,50 = 

#70*50,9,10,30+40, = 3500,9,10,70
#2,3,11,0,
# !99!,
# 30,40,50



