# Imports
from datetime import time
# Classes


class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return "{} menu available from {:%I}am to {:%I}pm".format(self.name, self.start_time, self.end_time)

    def calculate_bill(self, purchased_items):
        total = 0
        for i in purchased_items:
            total += self.items[i]
        return total


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def available_order(self,time):
        available_menu = []
        for i in self.menus:
            if i.start_time<= time and i.end_time >= time:
                available_menu.append(i)
        return available_menu
  
    def __repr__(self):
        return self.address

class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

# Menus
brunch = Menu("Brunch",
              {
                  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
              }, time(11, 0, 0), time(16, 0, 0))

early_bird = Menu("Early_bird",
                  {
                      'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
                  }, time(15, 0, 0), time(18, 0, 0))

dinner = Menu("Dinner",
              {
                  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
              }, time(17, 0, 0), time(23, 0, 0))

kids = Menu("Kids",
            {
                'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
            }, time(11, 0, 0), time(21, 0, 0))

# Test Menus
print(brunch)
brunchies = brunch.calculate_bill(["pancakes", "home fries", "coffee"])
early_birdz = early_bird.calculate_bill(
    ["salumeria plate", "mushroom ravioli (vegan)"])
print(early_birdz)
print(brunchies)

all_menus = [brunch, early_bird, dinner, kids]

# Test Franchises
flagship_store = Franchise("1232 West End Road", all_menus)
new_installment = Franchise("12 East Mulberry Street", all_menus)
print(flagship_store)
print(new_installment)

print("Here are your available menus (FLAGSHIP): ")
menus = flagship_store.available_order(time(12))
for i in menus:
    print("- "+ str(i))
    #print("- {}, available from {:%H}:00 to {:%H}:00".format(i.name,i.start_time,i.end_time))
print("Here are your available menus (NEW INSTALLMENT): ")
menus = new_installment.available_order(time(17))
for i in menus:
    print("- "+ str(i))

#Test Businesses
business_basta = Business("Basta Fazoolin' with my Heart",[flagship_store,new_installment])
arepas_menu = Menu("Take a' Arepa",{
  'arepa pabellon': 7.00, 'pernil arepa': 8.50,
  'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, time(10), time(20))

arepas_place = Franchise("189 Firtzgerald Avernue",arepas_menu)

Business_arepa = Business("Take a' Arepa",arepas_place)
