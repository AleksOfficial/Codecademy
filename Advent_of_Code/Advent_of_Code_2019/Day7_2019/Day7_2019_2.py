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
test_input2= [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
amplifier_setting2=[9,7,8,5,6]

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

class Amplifier:
    def __init__(self,input_file,phase: int) -> None:
        self.input_file = input_file[:]
        self.inputs = [phase]
        #self.step(phase)
        self.index = 0
       
    def step(self,input_value):
        self.inputs.append(input_value)
        while True:
            immediate_mode1 = False
            immediate_mode2 = False
            immediate_mode3 = False
            
            index_value = self.input_file[self.index]
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
            if index_value == 99:
                return None
            
            elif index_value == 1:
                pos1,pos2,pos3 = self.input_file[self.index+1],self.input_file[self.index+2],self.input_file[self.index+3]
                if immediate_mode1:
                    val1 = pos1
                else:
                    val1 = self.input_file[pos1]
                if immediate_mode2:
                    val2 = pos2
                else:
                    val2 = self.input_file[pos2]
                if immediate_mode3:
                    val3 = pos3
                else:
                    val3 = self.input_file[pos3]
                self.input_file[pos3] = val1+val2
                self.index+=4
                
            elif index_value == 2:
                pos1,pos2,pos3 = self.input_file[self.index+1],self.input_file[self.index+2],self.input_file[self.index+3]
                if immediate_mode1:
                    val1 = pos1
                else:
                    val1 = self.input_file[pos1]
                if immediate_mode2:
                    val2 = pos2
                else:
                    val2 = self.input_file[pos2]
                if immediate_mode3:
                    val3 = pos3
                else:
                    val3 = self.input_file[pos3]
                self.input_file[pos3] = val1*val2
                self.index+=4
                
            elif index_value ==3:
                pos1 = self.input_file[self.index+1]
                self.input_file[pos1]=self.inputs[0]
                self.inputs = self.inputs[1:]
                self.index +=2
            elif index_value ==4:
                pos1 = self.input_file[self.index+1]
                self.index +=2
                if immediate_mode1:
                    val1 = pos1
                else:
                    val1 = self.input_file[pos1]
                return val1 

            elif index_value == 5:
                pos1,pos2 = self.input_file[self.index+1],self.input_file[self.index+2]
                if immediate_mode1:
                    val1 = pos1
                else:
                    val1 = self.input_file[pos1]
                if immediate_mode2:
                    val2 = pos2
                else:
                    val2 = self.input_file[pos2]
                if val1 !=0:
                    self.index = val2
                else:
                    self.index +=3

            elif index_value == 6:
                pos1,pos2 = self.input_file[self.index+1],self.input_file[self.index+2]
                if immediate_mode1:
                    val1 = pos1
                else:
                    val1 = self.input_file[pos1]
                if immediate_mode2:
                    val2 = pos2
                else:
                    val2 = self.input_file[pos2]
                if val1 ==0:
                    self.index = val2
                else:
                    self.index +=3
                    
            elif index_value == 7:
                pos1,pos2,pos3 = self.input_file[self.index+1],self.input_file[self.index+2],self.input_file[self.index+3]
                if immediate_mode1:
                    val1 = pos1
                else:
                    val1 = self.input_file[pos1]
                if immediate_mode2:
                    val2 = pos2
                else:
                    val2 = self.input_file[pos2]
                if immediate_mode3:
                    val3 = pos3
                else:
                    val3 = self.input_file[pos3]
                if val1<val2:
                    self.input_file[pos3] = 1
                else:
                    self.input_file[pos3] =0
                self.index +=4

            elif index_value == 8:
                pos1,pos2,pos3 = self.input_file[self.index+1],self.input_file[self.index+2],self.input_file[self.index+3]
                if immediate_mode1:
                    val1 = pos1
                else:
                    val1 = self.input_file[pos1]
                if immediate_mode2:
                    val2 = pos2
                else:
                    val2 = self.input_file[pos2]
                if immediate_mode3:
                    val3 = pos3
                else:
                    val3 = self.input_file[pos3]
                if val1==val2:
                    self.input_file[pos3] = 1
                else:
                    self.input_file[pos3] =0
                self.index +=4

def run_amplifiers(program,phases):
    amplifiers = [Amplifier(program,phase) for phase in phases]
    n = len(amplifiers)
    num_finished = 0

    last_output = 0
    last_non_none_output = None
    aid = 0

    while num_finished <n:
        last_output = amplifiers[aid].step(last_output)
        if last_output is None:
            return last_non_none_output
        else:
            last_non_none_output = last_output
        aid = (aid+1)%n
    

def find_best_config(program):
    total_max = 0
    for i in itertools.permutations(range(5,10)):
        amp_max = run_amplifiers(program,i)
        if amp_max >total_max:
            total_max = amp_max
    return total_max
    

print(run_amplifiers(test_input2,amplifier_setting2))
print(find_best_config(input_filed))


