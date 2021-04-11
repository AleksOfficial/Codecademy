path = "AOC\\Advent_of_Code_2019\\Day8_2019\\"
input_file = open(path+"input.txt").readline()
print(len(input_file))
test_file = "123456789012"

def image_creater(code,length,height):
    image = [[]]
    i = 0
    while code !="":
        for j in range(height):
            for x in range(length):
                image[i].append(int(code[0]))
                code = code[1:]
        image.append([])
        i+=1
    image.pop(-1)
    return image

    #DES MUAS I FERTIG MOCHN HEAST

def least_zeros(image):
    minimum_zeros_layer = None
    amount_zeros = None
    
    for layer in image:
        layer_amount_zeros =0            
        for pixel in layer:
            if pixel ==0:
                layer_amount_zeros+=1
        if amount_zeros is None:
            amount_zeros = layer_amount_zeros
            minimum_zeros_layer = layer[:]
        elif amount_zeros>layer_amount_zeros:
            amount_zeros=layer_amount_zeros
            minimum_zeros_layer = layer[:]
    return minimum_zeros_layer

def calculate_1_2(layer):
    amount_1 = 0
    amount_2 = 0
    for pixel in layer:
        if pixel == 1:
            amount_1+=1
        if pixel ==2:
            amount_2 +=1
    return amount_1*amount_2

def decode_image(image):
    midlayer = []
    for layer in image:
        if midlayer == []:
            midlayer = layer[:]
        else:
            for index_pixel in range(len(midlayer)):
                if midlayer[index_pixel] == 2:
                    midlayer[index_pixel] = layer[index_pixel]
    return midlayer
def draw_image(layer,height,length):
    i = 0
    for line in range(height):
        line_string = ""
        for pixel in range(length):
            if layer[i] == 0:
                line_string+="_"
            if layer[i] == 1:
                line_string+="#"
            i+=1
        print(line_string)


print(calculate_1_2(least_zeros(image_creater(test_file,3,2))))
print(calculate_1_2(least_zeros(image_creater(input_file,25,6))))
sol =  decode_image(image_creater(input_file,25,6))

print(draw_image(sol,6,25))        




