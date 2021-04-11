class IntCode():
    def __init__(self,input_file_,input_list = None):
        self.zero_bank = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.input_file = input_file_[:] 
        self.input_list = input_list[:]
        #print(self.input_file)
        self.index = 0
        self.opcode = 0
        self.instruction = 0
        self.possible_outcomes = []
        self.rel_base = 0
    
    def reset(self):
        self.immediate_mode1 = False
        self.immediate_mode2 = False
        self.immediate_mode3 = False
        self.relative_mode1 = False
        self.relative_mode2 = False
        self.relative_mode3 = False
        self.val1 = None
        self.val2 = None
        self.val3 = None
        self.pos1 = None
        self.pos2 = None
        self.pos3 = None

    def set_modes_and_opcode(self):
        self.instruction = str(self.input_file[self.index])
        if len(self.instruction) > 2:
            self.opcode = int(self.instruction[-2:])
            if len(self.instruction) == 3:
                if self.instruction[0] == "1":
                    self.immediate_mode1 = True
                if self.instruction[0] == "2":
                    self.relative_mode1 = True
            elif len(self.instruction) == 4:
                if self.instruction[0] == "1":
                    self.immediate_mode2 = True
                if self.instruction[0] == "2":
                    self.relative_mode2 = True
                if self.instruction[1] == "1":
                    self.immediate_mode1 = True
                if self.instruction[1] == "2":
                    self.relative_mode1 = True
            elif len(self.instruction) == 5:
                if self.instruction[0] == "1":
                    self.immediate_mode3 = True
                if self.instruction[0] == "2":
                    self.relative_mode3 = True
                if self.instruction[1] == "1":
                    self.immediate_mode2 = True
                if self.instruction[1] == "2":
                    self.relative_mode2 = True
                if self.instruction[2] == "1":
                    self.immediate_mode1 = True
                if self.instruction[2] == "2":
                    self.relative_mode1 = True
            else:
                print(f"Error - Instruction cannot be computed! Instructioncode: {self.instruction}")
                raise ValueError()
            return
        else:
            self.opcode = int(self.instruction)
            return
    def evaluate_positions(self,amount):
        if amount ==1:
            self.pos1 = self.input_file[self.index+1]
        if amount ==2:
            self.pos1 = self.input_file[self.index+1]
            self.pos2 = self.input_file[self.index+2]
        if amount ==3:
            self.pos1 = self.input_file[self.index+1]
            self.pos2 = self.input_file[self.index+2]
            self.pos3 = self.input_file[self.index+3]
        
        if self.relative_mode1 and self.pos1 is not None:
            self.pos1 +=self.rel_base
        if self.relative_mode2 and self.pos2 is not None:
            self.pos2 +=self.rel_base
        if self.relative_mode3 and self.pos3 is not None:
            self.pos3 +=self.rel_base

        
        if self.immediate_mode1 and self.pos1 is not None:
            self.val1 = self.pos1
        elif self.pos1 is not None:
            while self.pos1 >len(self.input_file)-1:
                self.input_file+=self.zero_bank
            self.val1 = self.input_file[self.pos1]
        if self.immediate_mode2 and self.pos2 is not None:
            self.val2 = self.pos2
        elif self.pos2 is not None:
            while self.pos2 >len(self.input_file)-1:
                self.input_file+=self.zero_bank
            self.val2 = self.input_file[self.pos2]
        if self.immediate_mode3 and self.pos3 is not None:
            self.val3 = self.pos3
        elif self.pos3 is not None:
            while self.pos3 >len(self.input_file)-1:
                self.input_file+=self.zero_bank
            self.val3 = self.input_file[self.pos3]

        return 0
        
    def run(self):
        running = True
        while running:
            self.reset()
            self.set_modes_and_opcode()
            if self.opcode == 1:
                self.evaluate_positions(3)
                self.input_file[self.pos3] = self.val1+self.val2
                self.index+=4
                        
            elif self.opcode == 2:
                self.evaluate_positions(3)
                self.input_file[self.pos3] = self.val1*self.val2
                self.index+=4

            elif self.opcode ==3:
                self.evaluate_positions(1)
                self.input_file[self.pos1]=self.input_list[0]
                self.input_list = self.input_list[1:]
                self.index +=2

            elif self.opcode ==4:
                self.evaluate_positions(1)
                print(self.val1)
                self.possible_outcomes.append(self.val1)
                #input_file.append(input_file[pos1])
                self.index +=2

            elif self.opcode == 5:
                self.evaluate_positions(2)
                if self.val1 !=0:
                    self.index = self.val2
                else:
                    self.index +=3

            elif self.opcode == 6:
                self.evaluate_positions(2)
                if self.val1 ==0:
                    self.index = self.val2
                else:
                    self.index +=3
                    
            elif self.opcode == 7:
                self.evaluate_positions(3)
                if self.val1<self.val2:
                    self.input_file[self.pos3] = 1
                else:
                    self.input_file[self.pos3] =0
                self.index +=4

            elif self.opcode == 8:
                self.evaluate_positions(3)
                if self.val1==self.val2:
                    self.input_file[self.pos3] = 1
                else:
                    self.input_file[self.pos3] =0
                self.index +=4

            elif self.opcode == 9:
                self.evaluate_positions(1)
                self.rel_base += self.val1
                self.index+=2
            elif self.opcode == 99:
                running = False
        return self.possible_outcomes



path= "AOC\\Advent_of_Code_2019\\Day9_2019\\"

test_data1=[109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99] # should return copy of itself
test_data2=[1102,34915192,34915192,7,4,7,99,0] # should output a 16 digit number
test_data3=[104,1125899906842624,99] #should output middle number

with open(path+"input.txt","r") as input_filed:
    new_input = input_filed.readline()
updated_input = new_input.split(",")
input_filed = []
for i in updated_input:
    input_filed.append(int(i))


first_try = IntCode(test_data1,[1])
second_try = IntCode(test_data2,[1])
third_try = IntCode(test_data3,[1])
final_try = IntCode(input_filed,[2])

#print(first_try.run())
#print(second_try.run())
#print(third_try.run())
print(final_try.run())



