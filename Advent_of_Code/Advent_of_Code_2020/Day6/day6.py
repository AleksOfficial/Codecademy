def set_questions(input_string):
  people = input_string.split("\n")
  questions={}
  for i in people:
     for question in i:
       questions[question]=1
  return len(questions.keys())

def set_questions2(input_string):
  people = input_string.split("\n")
  questions={}
  for i in people:
     for question in i:
       try:
         questions[question]+=1
       except KeyError:
         questions[question]=1
  length = len(people)
  total = 0
  for i in questions.keys():
    if(length == questions[i]):
      total+=1
  return total
  


file = open("input.txt","r")
input=file.read().split("\n\n")
#TESTING
test = '''abc

a
b
c

ab
ac

a
a
a
a

b'''
test_max=0
for i in test.split("\n\n"):
  test_max+=set_questions(i)
print(test_max)

# Aufgabe 1
amount=0
for i in input:
  amount+=set_questions(i)
print(amount)

# Aufgabe 2
amount2=0
for i in input:
  amount2+=set_questions2(i)
print(amount2)