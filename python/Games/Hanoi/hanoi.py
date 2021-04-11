from stack import Stack
solver = False
print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#Set up the Game
num_disks=int(input("\nHow many disks do you want to play with?\n"))
while(num_disks <3):
  num_disks=int(input("Enter a number greater than or equal to 3\n"))

for i in reversed(range(num_disks)):
  left_stack.push(i)
  
num_optimal_moves = 2**num_disks -1
print("\nThe fastest you can solve this game is in {} moves".format(num_optimal_moves))
num_user_moves = 0

def printing():
    print("\n\n\n...Current Stacks...")
    for i in stacks:
      i.print_items()

#Get User Input
def get_input():
  choices = [x.get_name()[0] for x in stacks]
  print(choices)
  while(True):
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {} for {}".format(letter,name))
    user_input = input("").upper()
    if(user_input in choices):
      for i in range(len(stacks)):
        if(user_input == choices[i]):
          return stacks[i]
  
#Play the Game
def playing_the_game():
  num_user_moves =0
  while(right_stack.get_size() != num_disks):
    print("\n\n\n...Current Stacks...")
    for i in stacks:
      i.print_items()
    while(True):
      print("\nWhich stack do you want to move from?\n")
      from_stack = get_input()
      print("\nWhich stack do you want to move to?\n")
      to_stack = get_input()
      if(from_stack.is_empty()):
        print("\n\nInvalid Move. Try again.")
      elif(to_stack.is_empty() or from_stack.peek()<to_stack.peek()):
        disk = from_stack.pop()
        to_stack.push(disk)
        num_user_moves +=1
        break
      else:
        print("\n\nInvalid Move. Try again.")
  print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(num_user_moves,num_optimal_moves))

def move(f,t):
  print("Moving from {} Stack to {} Stack!".format(f.name,t.name))
  disk = f.pop()
  t.push(disk)
  n_solve.append(1)
  
  

def solving(num,f,h,t):
  #print(num)
  if num == 0:
    return 
  solving(num-1,f,t,h)
  printing()
  move(f,t)
  solving(num-1,h,f,t)



n_solve = []
if input("Would you like to get this solved for you?(y/n)") == "y":
  solver = True
if solver:
  solving(num_disks,stacks[0],stacks[1],stacks[2])
  printing()
  print("\n\nThe game was completed in {0} moves, and the optimal number of moves is {1}".format(len(n_solve),num_optimal_moves))
else:
  playing_the_game()
