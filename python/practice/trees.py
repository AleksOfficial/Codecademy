'''
class TreeNode:
  def __init__(self, value):
    self.value = value
    self.children = []

  def add_child(self, child_node):
    #print("adding " + child_node.value +" to children")
    self.children.append(child_node) 
  
  def traverse(self):
    nodes_to_visit = [self]
    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop(0)
      nodes_to_visit += current_node.children

      #print(current_node.children)
      print(current_node.value)

root = TreeNode("A")
first_child = TreeNode("B")
second_child = TreeNode("C")

root.add_child(first_child)
root.add_child(second_child)


root.traverse()'''
######
# TREENODE CLASS
######
class TreeNode:
  def __init__(self,story_piece):
    self.story_piece = story_piece
    self.choices = []

  def add_child(self,node):
    self.choices.append(node)
  
  def traverse(self):
    story_node = self
    
    while(len(story_node.choices)!=0):
      print(story_node.story_piece)
      user_choice = int(input("What will you do? (Press 1 or 2 and Enter)\n"))
      if(user_choice == 1):
        story_node = self.choices[0]
      elif(user_choice == 2):
        story_node = self.choices[1]
      else: print("invalid input")
    print(story_node.story_piece)
    return



######
# VARIABLES FOR TREE
######
user_choice = input("What is your name? ")
story_root = TreeNode("""
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
""")

choice_a =TreeNode("""
The bear is startled and runs away.
Do you:
1 ) Shout 'Sorry bear!'
2 ) Yell 'Hooray!'
""")

choice_b= TreeNode("""
You come across a clearing full of flowers. 
The bear follows you and asks 'what gives?'
Do you:
1 ) Gasp 'A talking bear!'
2 ) Explain that the bear scared you.
""")

story_root.add_child(choice_a)
story_root.add_child(choice_b)



######
# TESTING AREA
######
print(user_choice)
print("Once upon a time...")
story_root.traverse()
