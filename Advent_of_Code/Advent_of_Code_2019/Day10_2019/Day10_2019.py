#testing inputs & Final States return
#region
test_input_1 = """.#..#
.....
#####
....#
...##
"""
test_result1 = ((3,4),8)
test_input_2 = """......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####
"""
test_result2=((5,8),33)
test_input_3 = """#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.
"""
test_result3=((1,2),35)
test_input_4=""".#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..
"""
test_result4=((6,3),41)
test_input_5 = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
"""
test_result5=((11,13),210)
#endregion
import math
path= "AOC\\Advent_of_Code_2019\\Day10_2019\\"
input_data =""
with open(path+"input.txt","r") as i_f:
    for line in i_f:
        input_data +=line

def evaluate_asteroids(asteroidlist):
    max = 0
    for asteroid in asteroidlist:
        current_asteroid = eval_line_of_sight(asteroidlist,asteroid)
        #print(current_asteroid)
        if not max:
            max = len(current_asteroid)
            coordinates = asteroid
            #print("Initial: {}, {}".format(max,coordinates))
        else:
            if max<len(current_asteroid):
                max = len(current_asteroid)
                coordinates = asteroid
                #print("New High: {}, {}".format(max,coordinates))
    return (coordinates,max)

def evaluate_asteroids_pt2(asteroidlist):
    max = 0
    for asteroid in asteroidlist:
        asteroidmap = eval_line_of_sight(asteroidlist,asteroid)
        #print(current_asteroid)
        if not max:
            max = len(asteroidmap)
            max_map = asteroidmap
            coordinates = asteroid
            #print("Initial: {}, {}".format(max,coordinates))
        else:
            if max<len(asteroidmap):
                max = len(asteroidmap)
                max_map = asteroidmap
                coordinates = asteroid
                #print("New High: {}, {}".format(max,coordinates))
    return (max_map, max,coordinates)

def laserdrill(asteroidlist):
    asteroidmap,total,coordinates = evaluate_asteroids_pt2(asteroidlist)
    update = sorted(asteroidmap.keys())
    rotationlist = []
    for i in update:
        if i >= 270:
            rotationlist.append(i)
    for i in update:
        if i <270:
            rotationlist.append(i) 
          
    #print(updated_list)
        
    i = 0
    while i <total:
        for j in rotationlist:
            try:
                drilled=asteroidmap[j].pop(-1)
                i+=1
                if i ==200:
                    print(drilled)
                    
            except:
                pass

def eval_line_of_sight(list,asteroid):
    line_of_sight = {}
    # line_of_sight2 = {}
    # line_of_sight3 = {}
    # line_of_sight4 = {}

    #line_of_sight["origin"] = asteroid 
    for object in list:
        if object != asteroid:
            new_object = (object[0] - asteroid[0],object[1]-asteroid[1])
            if new_object[1]==0:
                if new_object[0]>0:
                    angle = 0
                else:
                    angle = 180
            elif new_object[0] ==0:
                if new_object[1]>0:
                    angle = 90
                else:
                    angle = 270
                
            else:
                angle = math.degrees(math.atan(new_object[1]/new_object[0]))
                
                if new_object[0]<0 and new_object[1]<0:
                    angle+=180
                elif new_object[0]>0 and new_object[1]<0:
                    angle+=360
                elif new_object[0]<0 and new_object[1]>0:
                    angle+=180
         
            try:
                line_of_sight[angle].append(object)
            except:
                line_of_sight[angle] = []
                line_of_sight[angle].append(object)
                
    return line_of_sight

    
def positions_asteroids(mapfile):
    asteroids = []
    maplist = mapfile.split("\n")
    for line in range(len(maplist)):
        for column in range(len(maplist[line])):
            if maplist[line][column]=="#":
              asteroids.append((column,line))
    return asteroids

#region
# total_asteroids = positions_asteroids(test_input_1)
# result1 = evaluate_asteroids(total_asteroids)
# if result1 == test_result1:
#     print("Correct answer!")
# else:
#     print("Wrong!")
#     print(test_result1)
#     print(result1)
    
# total_asteroids = positions_asteroids(test_input_2)
# result1 = evaluate_asteroids(total_asteroids)
# if result1 == test_result2:
#     print("Correct answer!")
# else:
#     print("Wrong!")
#     print(test_result2)
#     print(result1)
    
# total_asteroids = positions_asteroids(test_input_3)
# result1 = evaluate_asteroids(total_asteroids)
# if result1 == test_result3:
#     print("Correct answer!")
# else:
#     print("Wrong!")
#     print(test_result3)
#     print(result1)
    
# total_asteroids = positions_asteroids(test_input_4)
# result1 = evaluate_asteroids(total_asteroids)
# if result1 == test_result4:
#     print("Correct answer!")
# else:
#     print("Wrong!")
#     print(test_result4)
#     print(result1)

total_asteroids = positions_asteroids(test_input_5)
result1 = evaluate_asteroids(total_asteroids)
if result1 == test_result5:
    print("Correct answer!")
else:
    print("Wrong!")
    print(test_result5)
    print(result1)
#endregion
total_asteroids = positions_asteroids(input_data)
result1 = evaluate_asteroids(total_asteroids)
result2 = laserdrill(total_asteroids)
print(result1)
#yay. was harder than it should have been. 
#mainly cuz the coordinate system was rotated and that caused confusion :) 







  
                
                
                

    

 
