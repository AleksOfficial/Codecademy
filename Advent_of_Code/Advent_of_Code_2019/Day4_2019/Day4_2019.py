input_range_lower = 356261
input_range_upper = 846303
total_counter =0
for pwd in range(input_range_lower,input_range_upper+1):
    s = str(pwd)
    digits = [int(x) for x in s]
    pair_exists = False
    paired_numbers = {}
    # pair_two = False
    # pair_three = False
    decreased_digits_exist= False
    #print(s+f" , {digits}")
    for i in range(len(digits)-1):
        if digits[i]>digits[i+1]:
            decreased_digits_exist = True
            break
    for i in range(len(digits)-1):
        if digits[i]==digits[i+1]:
            pair_value = digits[i]
            pair_exists = True
            if i+1 <len(digits)-1:
                if digits[i+2] == pair_value or digits[i-1] == pair_value:
                    paired_numbers[pair_value] = False
                else:
                    paired_numbers[pair_value] = True
            else:
                if digits[i-1]==pair_value:
                    paired_numbers[pair_value] = False
                else:
                    paired_numbers[pair_value] = True
       
    if pair_exists and not decreased_digits_exist:
        for i in paired_numbers.keys():
            if paired_numbers[i]:
                total_counter+=1
                print("total counter increased")
                break
        
        
    
    

print(total_counter)
    



    # It is a six-digit number.
    # The value is within the range given in your puzzle input.
    # Two adjacent digits are the same (like 22 in 122345).
    # Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

    # Additional details:
    # There can be only pairs of numbers, not additional numbers of that pair. except it has another partner to pair up with
    # 112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
    # 123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
    # 111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).



