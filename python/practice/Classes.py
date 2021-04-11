how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]
count_s = 0
for i in how_many_s:
    print(dir(i))
'''  if(hasattr(i,"count")):
      for x in i:
          if(x == "s"):
              count_s+=1
'''

    

'''class TestClass:
    def __init__(self, id):
        self.id = id
        print("Creating object id = " + str(self.id))

    def __del__(self):
        print("Deleting object id = " + str(self.id))

print("Instantiating object 1")
my_obj = TestClass(1)

print("Instantiating object 2")
my_obj2 = TestClass(2)

print("Instantiating object 3")
my_obj = TestClass(3)

# Wait for 10 seconds to show that object 1 is destroyed before the program ends
from time import sleep
sleep(10)'''