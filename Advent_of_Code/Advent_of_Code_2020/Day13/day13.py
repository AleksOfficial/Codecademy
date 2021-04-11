file = open("input.txt","r")
input = file.read().split("\n")
timestamp = int(input[0])
bus_string = input[1]
busses = bus_string.replace("x,","").split(",")
min_diff = 9999999999999999
min_bus = 0
for bus in busses:
  bus = int(bus)

  multiplier = int(timestamp/bus)+1
  arrival_time = multiplier * bus
  diff = arrival_time-timestamp
  if(min_diff > diff):
    min_diff = diff
    min_bus = bus

print("min_diff: {}".format(min_diff))
print("min_bus: {}".format(min_bus))
print(min_diff*min_bus)