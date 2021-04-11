''' byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)
'''
#I guess you could seperate this function further down into creating an passport first and then check if the fields are present
#Meh. it's so short it doesn't bother me rn
#Actually it doesn now. Gotta split that up now

def create_passport(passport_details):
  details_split = passport_details.split("\n")
  details_not_seperated=[]
  detail_list=[]
  passport={}
  for i in details_split:
    detail_list.append(i.split(" "))
  #print(detail_list)
  for i in detail_list:
    for j in i:
      key_val=j.split(":")
      passport[key_val[0]]=key_val[1]
  return passport

def valid_passport_fields(passport_details):
  passport_creds=set(["byr","iyr","eyr","hgt","hcl","ecl","pid"]) # is not necessary:"cid"
  passport=create_passport(passport_details)
  keys=set(passport.keys())
  if(passport_creds.issubset(keys)):
    return True
  else:
    return False
#Aufgabe 1 (original)
'''
def valid_passport_fields(passport_details):
  passport_creds=set(["byr","iyr","eyr","hgt","hcl","ecl","pid"]) # is not necessary:"cid"
  details_split = passport_details.split("\n")
  details_not_seperated=[]
  detail_list=[]
  passport={}
  for i in details_split:
    detail_list.append(i.split(" "))
  print(detail_list)
  for i in detail_list:
    for j in i:
      key_val=j.split(":")
      passport[key_val[0]]=key_val[1]
  keys=set(passport.keys())
  if(passport_creds.issubset(keys)):
    return True
  else:
    return False
'''
#Aufgabe 2
def number_checks(value,subarray):
  if(int(value)>=subarray[0] and int(value)<=subarray[1]):
    return True
  else:
    return False

def valid_passport_data(passport_details):
  passport_creds=["byr","iyr","eyr","hgt","hcl","ecl","pid"] # is not necessary:"cid"
  byr_iyr_eyr = [[1920,2002],[2010,2020],[2020,2030]]
  _cm = [150,193]
  _in = [59,76]
  ecl = ["amb","blu","brn","gry","grn","hzl","oth"]
  hcl = hcl = [chr(i) for i in range(ord('a'),ord('f')+1)]+["{}".format(i) for i in range(10)]
  pid = 9
  passport=create_passport(passport_details)
  for i in range(3):
    if(not number_checks(passport[passport_creds[i]],byr_iyr_eyr[i])):
      return False
  if(passport["hgt"][-2:]=="cm"):
    if(not number_checks(int(passport["hgt"][:-2]),_cm)):
      return False
  elif(passport["hgt"][-2:]=="in"):
    if(not number_checks(int(passport["hgt"][:-2]),_in)):#ha. had wrong array right there: instead of _in I had _cm
      return False
  else:
    return False
  if(len(passport["hcl"])==7 and passport["hcl"][0]=='#'):
    for char in passport["hcl"][1:]:
      if(not(char in hcl)):
        return False
  else:
    return False
  if(not (passport["ecl"] in ecl)):
    return False
  if(len(passport["pid"])!=pid):
    return False
  print(passport)
  print("valid")
  return True


#Somewhere in Task 2 was a mistake
test_string='''pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'''  
test_split=test_string.split("\n\n")
test_count = 0
for i in test_split:
  if(valid_passport_fields(i)):
    if(valid_passport_data(i)):
      test_count+=1
print(test_count)
'''

file = open("input.txt","r")
input=file.read().split("\n\n")
count_pws=0
for i in input:
  if(valid_passport_fields(i)):
    if(valid_passport_data(i)):
      count_pws+=1

print(count_pws)
'''