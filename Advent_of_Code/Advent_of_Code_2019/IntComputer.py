def IntCode(Program:List[int],input_list:List[int]=None,):
    index_value = 0
    index = 0
    position1 = 0
    position2 = 0
    result_position = 0

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
            print(input_file[pos1])
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
