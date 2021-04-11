import itertools

def IntCode(input_file_,input_list=None):
    input_file = input_file_[:]
    index_value = 0
    index = 0
    position1 = 0
    position2 = 0
    result_position = 0
    possible_outcomes = []

    while index_value != 99:
        immediate_mode1 = False
        immediate_mode2 = False
        immediate_mode3 = False
        
        index_value = input_file[index]
        string_value = str(index_value)
        if len(string_value)>2:
            index_value = int(string_value[-2:])
            assert index_value !=99,"Program Terminated with OpCode 99"
            
            if len(string_value) ==3:
                if int(string_value[0]):
                    immediate_mode1 = True
            elif len(string_value) ==4:
                if int(string_value[0]):
                    immediate_mode2 = True
                if int(string_value[1]):
                    immediate_mode1 = True
            elif len(string_value) ==5:
                if int(string_value[0]):
                    immediate_mode3 = True
                if int(string_value[1]):
                    immediate_mode2 = True
                if int(string_value[2]):
                    immediate_mode1 = True

        if index_value == 1:
            pos1,pos2,pos3 = input_file[index+1],input_file[index+2],input_file[index+3]
            if immediate_mode1:
                val1 = pos1
            else:
                val1 = input_file[pos1]
            if immediate_mode2:
                val2 = pos2
            else:
                val2 = input_file[pos2]
            if immediate_mode3:
                val3 = pos3
            else:
                val3 = input_file[pos3]
            input_file[pos3] = val1+val2
            index+=4
            
        elif index_value == 2:
            pos1,pos2,pos3 = input_file[index+1],input_file[index+2],input_file[index+3]
            if immediate_mode1:
                val1 = pos1
            else:
                val1 = input_file[pos1]
            if immediate_mode2:
                val2 = pos2
            else:
                val2 = input_file[pos2]
            if immediate_mode3:
                val3 = pos3
            else:
                val3 = input_file[pos3]
            input_file[pos3] = val1*val2
            index+=4
        elif index_value ==3:
            pos1 = input_file[index+1]
            input_file[pos1]=input_list[0]
            input_list = input_list[1:]
            index +=2
        elif index_value ==4:
            pos1 = input_file[index+1]
            possible_outcomes.append(input_file[pos1])
            input_file.append(input_file[pos1])
            index +=2

        elif index_value == 5:
            pos1,pos2 = input_file[index+1],input_file[index+2]
            if immediate_mode1:
                val1 = pos1
            else:
                val1 = input_file[pos1]
            if immediate_mode2:
                val2 = pos2
            else:
                val2 = input_file[pos2]
            if val1 !=0:
                index = val2
            else:
                index +=3

        elif index_value == 6:
            pos1,pos2 = input_file[index+1],input_file[index+2]
            if immediate_mode1:
                val1 = pos1
            else:
                val1 = input_file[pos1]
            if immediate_mode2:
                val2 = pos2
            else:
                val2 = input_file[pos2]
            if val1 ==0:
                index = val2
            else:
                index +=3
                
        elif index_value == 7:
            pos1,pos2,pos3 = input_file[index+1],input_file[index+2],input_file[index+3]
            if immediate_mode1:
                val1 = pos1
            else:
                val1 = input_file[pos1]
            if immediate_mode2:
                val2 = pos2
            else:
                val2 = input_file[pos2]
            if immediate_mode3:
                val3 = pos3
            else:
                val3 = input_file[pos3]
            if val1<val2:
                input_file[pos3] = 1
            else:
                input_file[pos3] =0
            index +=4

        elif index_value == 8:
            pos1,pos2,pos3 = input_file[index+1],input_file[index+2],input_file[index+3]
            if immediate_mode1:
                val1 = pos1
            else:
                val1 = input_file[pos1]
            if immediate_mode2:
                val2 = pos2
            else:
                val2 = input_file[pos2]
            if immediate_mode3:
                val3 = pos3
            else:
                val3 = input_file[pos3]
            if val1==val2:
                input_file[pos3] = 1
            else:
                input_file[pos3] =0
            index +=4

    return max(possible_outcomes)

test_input = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"
test_input2= "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"

path= "AOC\\Advent_of_Code_2019\\Day7_2019\\"
with open(path+"input.txt","r") as input_filed:
    new_input = input_filed.readline()
updated_input = new_input.split(",")
input_filed = []
for i in updated_input:
    input_filed.append(int(i))

def find_max_amp_config(program,amplifier_amount):
    total_max = 0
    config = None
    
    for i in itertools.permutations(range(amplifier_amount)):
        amp_max = 0
        for j in i:
            amp_max =IntCode(program,[j,amp_max])
            #print(amp_max)
        if amp_max>total_max:
            total_max = amp_max
            config = i
    return total_max,config



test_input = [int(x) for x in test_input.split(",")]
#before_input_file = input_file[:]

# first value = 55

#IntCode(input_file,[4,0])
print(find_max_amp_config(test_input,5))
print(find_max_amp_config2(input_filed,(5,10)))



