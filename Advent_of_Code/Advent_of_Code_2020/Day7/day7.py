class Bag:
  def __init__(self,color,contains):
    self.color = color
    self.contains = contains
  def __str__(self):
    return "This is a {} bag, which contains the following other bags: {}".format(self.color,self.contains)
  def color_of_bag(self):
    return "{}".format(self.color)
  def other_bags_colors(self):
    return self.contains.keys()
  def other_bags_array(self):
    other_bags =[]
    for i in self.contains.keys():
      bag = [i,self.contains[i]]
      other_bags.append(bag)
    return other_bags

class has_gold_bags:
  def __init__(self):
    self.bags_colors = {}
    self.bags_colors_amount = {}

  def add_bag(self, bag):
    color = bag.color_of_bag()
    other_bags = bag.other_bags_colors()
    other_bags_array = bag.other_bags_array()
    self.bags_colors[color]=other_bags
    self.bags_colors_amount[color]=other_bags_array
  
  # Aufgabe 1
  def contains_color(self,bag_color,search_val):
    if(search_val in self.bags_colors[bag_color]):
      return True
    else:
      for i in self.bags_colors[bag_color]:
        if(self.contains_color(i,search_val)):
          return True
      return False
  
  # Aufgabe 2
  def amount_bags_color(self,bag_color,amount):
    if(self.bags_colors_amount[bag_color]==[]):
      return amount
    zs = 0
    for i in self.bags_colors_amount[bag_color]:
      if(amount!=0):
        zs+=self.amount_bags_color(i[0],i[1]*amount)
      else:
        zs+=self.amount_bags_color(i[0],i[1])
    amount+=zs
    return amount

  

def create_bag(bag):
  bag_color = bag.split("contain")[0].split("bags")[0].strip()
  other_bags = bag.split("contain")[1]
  as_list_ob = other_bags.split(",")
  other_bags_clean={}
  print(as_list_ob)
  for i in as_list_ob:
    i=i.strip(" ").strip(".")
    if(i !="no other bags"):
      words = i.split(" ")
      other_color=words[1]+" "+words[2]
      amount = int(i[0])
      other_bags_clean[other_color]=amount
  new_bag = Bag(bag_color,other_bags_clean)
  return new_bag

test='''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.'''



test_all_bags = has_gold_bags()
test_input = test.split("\n")
for i in test_input:
  bag = create_bag(i)
  test_all_bags.add_bag(bag)

#the test works :D
test_amount=0
for i in test_all_bags.bags_colors.keys():
  if(test_all_bags.contains_color(i,"shiny gold")):
    test_amount+=1
print(test_amount)  

test_amount_bags = test_all_bags.amount_bags_color("shiny gold",0)
print(test_amount_bags)  


# reading data
all_bags= has_gold_bags()
file = open("input.txt","r")
bags_details = file.read().split("\n")
print(bags_details)
for i in bags_details:
  bag = create_bag(i)
  all_bags.add_bag(bag)

# Aufgabe 1
amount_shiny = 0
amount_bags = 0
for i in all_bags.bags_colors.keys():
  if(all_bags.contains_color(i,"shiny gold")):
    amount_shiny+=1

amount_bags = all_bags.amount_bags_color("shiny gold",0)

print("Amount of Bags that have a shiny gold bag: {}".format(amount_shiny))
print("Amount of Bags that have a shiny gold bag: {}".format(amount_bags))


