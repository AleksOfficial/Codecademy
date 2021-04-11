import datetime
def welcome_message():
    print('''Welcome to the Fibonacci numbers generator!
Choose your action:
1 -> define upper limit and see all Fibonacci numbers up to specified value.
2 -> define lower and upper limit and see all Fibonacci numbers in between.
3 -> Enter a number and see if the number is a Fibonacci number or not. 
0 -> Exit
''')
    return

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-2)+fibonacci(n-1)
    
def sequence(upper_limit,lower_limit=0):
    mem_sequence = []
    iteration =0
    fibonacci_number = fibonacci(iteration)
    while lower_limit>fibonacci_number:
        iteration+=1
        fibonacci_number = fibonacci(iteration)
    while upper_limit>=fibonacci_number:
        mem_sequence.append(fibonacci_number)
        iteration+=1
        fibonacci_number = fibonacci(iteration)
    return mem_sequence

#Needs to be done.
def output(user_sequence=[],User_Choice=0,upper_limit=0,lower_limit=0):
    total_string =""
    if User_Choice == "1":
        total_string +="User Choice: 1 -> define upper limit and see all Fibonacci numbers up to specified value. "
        total_string +=f"Upper Limit: {upper_limit}. "
        total_string +=f"Fibonacci Sequence: {user_sequence}\n"
        print(f"Your upper limit: {upper_limit}")
        if user_sequence !=[]:
            print("Here is your Fibonacci Sequence!")
            sequence_string=""
            for i in range(len(user_sequence)):
                if i !=len(user_sequence)-1:
                    sequence_string+=str(user_sequence[i])
                    sequence_string +=", "
                else:
                    sequence_string+=str(user_sequence[i])
            print(sequence_string)
            return total_string
        else:
            print("Your input resulted into an empty Fibonacci Sequence!")
            return total_string

    elif User_Choice == "2":
        total_string +="User Choice: 2 -> define lower and upper limit and see all Fibonacci numbers in between."
        total_string +=f"Upper Limit: {upper_limit}. "
        total_string +=f"Lower Limit: {lower_limit}. "
        total_string +=f"Fibonacci Sequence: {user_sequence}\n"
        print(f"Your upper limit: {upper_limit}")
        print(f"Your lower limit: {lower_limit}")
        if user_sequence !=[]:
            print("Here is your Fibonacci Sequence in the requested area!")
            sequence_string=""
            for i in range(len(user_sequence)):
                if i !=len(user_sequence)-1:
                    sequence_string+=str(user_sequence[i])
                    sequence_string +=", "
                else:
                    sequence_string+=str(user_sequence[i])
            print(sequence_string)
            return total_string
        else:
            print("Your input resulted into an empty Fibonacci Sequence!")
            return total_string
            
    elif User_Choice == "3":
        check_sequence = sequence(upper_limit)
        if upper_limit in check_sequence:
            in_sequence = True
        else:
            in_sequence = None
        if in_sequence:
            for i in range(len(check_sequence)):
                if check_sequence[i] == upper_limit:
                    index = i+1
            total_string +="User Choice: 3 -> Enter a number and see if the number is a Fibonacci number or not. "
            total_string +=f" Number entered: {upper_limit}. "
            total_string +=f"Element within Fibonacci-Sequence: True; Position {index}\n"
            print(f"Your number {upper_limit} is at position {index} in the Fibonacci Sequence!")
            return total_string
        else:
            total_string +="User Choice: 3 -> Enter a number and see if the number is a Fibonacci number or not. "
            total_string +=f"Number entered: {upper_limit}. "
            total_string +=f"Element within Fibonacci-Sequence: False\n"
            print(f"Your number {upper_limit} is not in the Fibonacci Sequence!")
            return total_string
    elif User_Choice == "0":
        total_string +="User Choice: 0 -> Exit\n"
    return total_string

directory_addition = "fibonacci\\"

inputs_outputs = open(directory_addition+"Inputs_Outputs.txt","a")
time_= datetime.datetime.now()
time = datetime.datetime(time_.year,time_.month,time_.day,time_.hour,time_.minute,time_.second)

total_output_string = str(time) +"\n"
user_sequence = []

while 24:
    welcome_message()
    user_choice=input(": ")
    if user_choice =="1":
        while 24:
            try:
                upper_limit = int(input("Define your upper limit: "))
                user_sequence = sequence(upper_limit)
                total_output_string += output(user_sequence,user_choice,upper_limit)
                break
            except:
                print("Invalid input. Try again.")
            
    if user_choice =="2":
        while 24:
            try:
                lower_limit = int(input("define your lower limit: "))
                upper_limit = int(input("define your upper limit: "))
                user_sequence = sequence(upper_limit,lower_limit)
                total_output_string += output(user_sequence,user_choice,upper_limit,lower_limit)
                break
            except:
                print("Invalid input. Try again.")
    if user_choice =="3":
        while 24:
            try: 
                number_entered=int(input("Enter your possible Fibonacci number: "))
                total_output_string += output([],user_choice,number_entered,number_entered)
                break
            except:
                print("Invalid Input. Try again.")
    if user_choice =="0":
            total_output_string += output(User_Choice=user_choice)
            break
    input("Press the Enter key to continue...")
inputs_outputs.writelines(total_output_string)
inputs_outputs.close()




# Basic Requirements

# User Story: As a user I want to be able to input an upper limit and see all Fibonacci numbers up to the specified value.

# User Story: As a user I want to be able to quit the program or go again after each cycle.
# Additional Challenges

# Intermediate Challenge

# User Story: As a user I want to be able to input an upper AND a lower limit, and see all Fibonacci numbers in that range.

# User Story: As a user I want to be able to input an integer and see whether or not it’s one of the Fibonacci numbers. If it is, I want to see its index in the sequence.

# Advanced Challenge

# User Story: As a user I want the program to save the output, in addition to printing to console, so that it can be preserved and accessed separately.