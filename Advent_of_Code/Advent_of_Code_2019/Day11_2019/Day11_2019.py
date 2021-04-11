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


class Directions():
    up = 0
    right = 1
    down = 2
    left = 3



def turn(current_direction,should_turn):
    if current_direction == Directions.up:
        if should_turn==0:
            current_direction = Directions.left
        else:
            current_direction = Directions.right
    if current_direction == Directions.right:
        if should_turn==0:
            current_direction = Directions.up
        else:
            current_direction = Directions.down
    if current_direction == Directions.down:
        if should_turn==0:
            current_direction = Directions.right
        else:
            current_direction = Directions.left
    if current_direction == Directions.left:
        if should_turn==0:
            current_direction = Directions.down
        else:
            current_direction = Directions.up
    return current_direction


        
    

path= "AOC\\Advent_of_Code_2019\\Day11_2019\\"


with open(path+"input.txt","r") as input_filed:
    new_input = input_filed.readline()
updated_input = new_input.split(",")
input_filed = []
for i in updated_input:
    input_filed.append(int(i))

print(input_filed)





