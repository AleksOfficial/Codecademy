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

#FOR CORONAVIRUS PROGRAM:
import unittest
from selenium import webdriver

class GoogleTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("D:\\Google Drive\\Codecademy\\Coronavirus_Email_Project\\chromedriver.exe")
    
    def test_google_search(self):
        self.driver.get("https://www.google.com/xhtml")
        self.assertIn("Google",self.driver.title)
        search_field=self.driver.find_element_by_name("q")
        search_field.send_keys("eric donald trump")
        search_field.submit()
        assert "Es wurden keine mit deiner Suchanfrage -" not in self.driver.page_source

    def test_google_search2(self):
        self.driver.get("https://www.google.com/xhtml")
        self.assertIn("Google",self.driver.title)
        search_field=self.driver.find_element_by_name("q")
        search_field.send_keys("asdfasdfasdfasfaoköpjsdhfoipawshfvpoiashbdfpihapöfnbapisdfhgpoiausdjhfpdfasdfasdf")
        search_field.submit()
        assert "Es wurden keine mit deiner Suchanfrage -" not in self.driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
