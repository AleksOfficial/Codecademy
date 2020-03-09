#Data
destinations =["Paris, France","Shanghai, China","Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes',"Shanghai, China", ["historical site","art"]]

attractions = [[] for i in destinations]
#functions
"""
#My Method
def get_destination_index(destination):
  index =0
  for i in destinations:
    if(i == destination):
      return index
    index +=1
  print("Your Destination is not in our list!")
  return -1
"""
#Recommended Method with Python
def get_destination_index(destination):
  dest_index =destinations.index(destination)
  return dest_index

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_dest_index = get_destination_index(traveler_destination)
  return traveler_dest_index

def add_attraction(destination,attraction):
  try:
    dest_index =  get_destination_index(destination)
  except ValueError:
      return
  attractions_for_destination = attractions[dest_index]
  attractions_for_destination.append(attraction)
  return 

def find_attractions(destination,interests):
  try:
    dest_index = get_destination_index(destination)
  except ValueError: 
    return
  attractions_in_city = attractions[dest_index]
  attractions_with_interest = []
  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]
    for interest in interests:
      for attract in attraction_tags:
        if(interest == attract):
          attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

def get_attractions_for_traveler(traveler):
  trav_dest = traveler[1]
  trav_interest = traveler[2]
  traveler_attractions = find_attractions(trav_dest, trav_interest)
  interests_string = "Hi "+ traveler[0]
  interests_string += ", we think you'll like these places around " +trav_dest +": "
  for interest in traveler_attractions:
    interests_string += interest
  return interests_string          
    
    
      
    

    
#Programcode

#print(get_destination_index("Los Angeles, USA"))
#print(get_destination_index("Paris, France"))
#print(get_destination_index("Los Angelds, USD"))
#print(get_traveler_location(test_traveler))
#print(attractions)
add_attraction("Los Angeles, USA",['Venice Beach', ['beach']])
#print(attractions)
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
#print(attractions)
la_arts=find_attractions("Los Angeles, USA", ['art'])
#print("\n"+str(la_arts))

smills_france=get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)