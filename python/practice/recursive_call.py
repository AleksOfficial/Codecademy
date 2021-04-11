def power_set(my_list):
    if len(my_list) == 0:
        return [[]]
    power_set_without_first = power_set(my_list[1:])
    with_first = [ [my_list[0]] + rest for rest in power_set_without_first ]
    return with_first + power_set_without_first
  
power_set(['a', 'b', 'c'])
