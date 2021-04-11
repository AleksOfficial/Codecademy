def read_data(string_data):
    test_list = string_data.split("\n")
    x = 0
    for i in test_list:
        test_list[x]=i.split(")")
        x+=1
    return test_list

def return_dictionary(list_data):
    orbit_points = {}
    x = 0 
    for i in list_data:
        
        try:
            orbit_points[i[1]].append(i[0])
            x+=1
        except:
            orbit_points[i[1]]=[i[0]]
            x+=1
    return orbit_points

def puzzle_part_1(dictionary_data):
    my_list = dictionary_data.keys()
    count = 0
    for i in my_list:
     while 42:
        if i == "COM":
            break
        i = dictionary_data[i][0]
        count +=1
    return count

def puzzle_part_2(dictionary_data):
    intersection = None
    list_total = dictionary_data.keys()
    for i in list_total:
        if i == "YOU":
            list_1 = []
            while True:
                if i == "COM":
                    break
                else:
                    list_1.append(i)
                    i = dictionary_data[i][0]
        if i =="SAN":
            list_2 = []
            while True:
                if i == "COM":
                    break
                else:
                    list_2.append(i)
                    i = dictionary_data[i][0]
    first_section = True
    for y in list_1:
        for j in list_2:
            if y == j and first_section:
                intersection = y
                first_section = False
    
    total_count = 0
    for i in list_1:
        total_count+=1
        if i == intersection:
            break
    for i in list_2:
        total_count+=1
        if i == intersection:
            break
    return total_count-4
    
    
            
path= "AOC\\Advent_of_Code_2019\\Day6_2019\\"

string_example1 = '''COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN'''

input_file = open(path+"input.txt","r")
input__ = input_file.readlines()
input_string =""
for i in input__:
    input_string+=i



test_example1= read_data(string_example1)
test_orbit_points1 = return_dictionary(test_example1)

test_example2 = read_data(input_string)
test_orbit_points2 = return_dictionary(test_example2)
test_count2 = puzzle_part_1(test_orbit_points2)
print(puzzle_part_2(test_orbit_points1))
print(puzzle_part_2(test_orbit_points2))
print(test_count2)


#connections = {}


# for i in test_example1:
#     try:
#         orbit_points[i[1]].append(i[0])
#     except:
#         orbit_points[i[1]]=[i[0]]
#     try:
#         connections[i[0]].append(i[1])
#     except:
#         connections[i[0]]=[i[1]]
#     try:
#         connections[i[1]].append(i[0])
#     except:
#         connections[i[1]]=[i[0]]
    
    # if orbit_points[i[1]].value() is None:
    #     orbit_points[i[1]]=[i[0]]
    # else:
    #     orbit_points[i[1]].append(i[0])

# class vertex_point():
#     def __init__(self):
#print(connections)


test_count_1 = puzzle_part_1(test_orbit_points1)
print(test_count_1)
# print(count)
        