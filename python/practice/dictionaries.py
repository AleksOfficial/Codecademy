#import pandas as pd
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks=zip(drinks,caffeine)

drinks_to_caffeine = {key:value for key, value in zip(drinks,caffeine)}
print(drinks_to_caffeine)

def seq_sum(sequence):
  a = zip(sequence, sequence[::-1])
  print(sequence[::-1])
  b = a
 # print(list(b))
  print(sum(next(a)))
  return len(sequence) * sum(next(a)) // 2


    

print(seq_sum(range(10)))
print(0+1+2+3+4+5+6+7+8+9)

#Dictionaries: try Except
population = {"California": {"Los Angeles": 3971883,
                             "San Diego": 1394928,
                             "San Jose": 1026908},
              "Texas": {"Houston": 2296224,
                        "San Antonio": 1469845}
              }

try:
    utah_list = population['Utah']

except KeyError as k:
    print(type(k))
    print("Key " + str(k) + " does not exist")

import random

def drawcard(tarot,spread,key):
  if len(spread)<1:
        x=tarot.pop(key)
        spread["past"] = x

  elif len(spread)<2:
        x = tarot.pop(key)
        spread["present"]= x
    
  elif len(spread)<3:
        x = tarot.pop(key)
        spread["future"] = x

  else:
      x = tarot.pop(key)
      spread["past"] = spread["present"]
      spread["present"] = spread["future"]
      spread["future"] = x


    

tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}
randomnumbers = []

drawcard(tarot,spread,13)
drawcard(tarot,spread,22)
drawcard(tarot,spread,10)

x=len(tarot)
print(x)
randomnumbers=random.sample(list(tarot),x)


    

#FOR CORONAVIRUS PROGRAM:
# import unittest
# from selenium import webdriver

# class GoogleTest(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome("D:\\Google Drive\\Codecademy\\Coronavirus_Email_Project\\chromedriver.exe")
    
#     def test_google_search(self):
#         self.driver.get("https://www.google.com/xhtml")
#         self.assertIn("Google",self.driver.title)
#         search_field=self.driver.find_element_by_name("q")
#         search_field.send_keys("eric donald trump")
#         search_field.submit()
#         assert "Es wurden keine mit deiner Suchanfrage -" not in self.driver.page_source

#     def test_google_search2(self):
#         self.driver.get("https://www.google.com/xhtml")
#         self.assertIn("Google",self.driver.title)
#         search_field=self.driver.find_element_by_name("q")
#         search_field.send_keys("asdfasdfasdfasfaoköpjsdhfoipawshfvpoiashbdfpihapöfnbapisdfhgpoiausdjhfpdfasdfasdf")
#         search_field.submit()
#         assert "Es wurden keine mit deiner Suchanfrage -" not in self.driver.page_source

#     def tearDown(self):
#         self.driver.close()

# if __name__ == "__main__":
#     unittest.main()