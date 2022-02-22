#default
parms = {'op':'check', 'cube': 'wwwbbbyyygggwrwbrbyyyrggwwwbobyoygogrrrgybrrrooobwgooo'}

print(parms)


parms = {'op':'check',
        'cube':'11w11w11wrrrrrrrrryggyggyggaaaaaaaaayy1yy1yy1wwgwwgwwg'}

parms = {'op':'check',
        'cube':'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01'}



parms = {'op':'check',
        'cube':'11w11w11wrrrrrrrrryggyggyggaaaaaaaaayy1yy1yy1wwgwwgwwg'}

#run checks against the first side. blue - front, red - right, green - back, yellow - top
#rotate around once

parms = {'op':'check', 'cube': 'wyrwbbwwwyrgyrwbrwyywggbggygoowoobyyrrrbybbobgrrgwgooo'}




parms = {'op':'check', 'cube': 'wyrwbbowwyrgyrwbrwyywggbggygoowoobyyrrrbybbobgrrgwgooo'}

def verify_adj_col():
    
    #around the edge of side 0
    ctr = 0                
    if ((lst_cube[0][0]) == lst_cube[0][4] and lst_cube[2][4] in [lst_cube[3][2],lst_cube[4][6]]):
        ctr = 1        
    elif ((lst_cube[0][1]) == lst_cube[0][4] and lst_cube[2][4] == lst_cube[4][7]):
        ctr = 1
    elif ((lst_cube[0][2]) == lst_cube[0][4] and lst_cube[2][4] in [lst_cube[4][8],lst_cube[1][0]]):
        ctr = 1
    elif ((lst_cube[0][3]) == lst_cube[0][4] and lst_cube[2][4] == lst_cube[3][5]):
        ctr = 1
    elif ((lst_cube[0][5]) == lst_cube[0][4] and lst_cube[2][4] == lst_cube[1][3]):
        ctr = 1
    elif ((lst_cube[0][6]) == lst_cube[0][4] and lst_cube[2][4] in [lst_cube[3][8],lst_cube[5][0]]):
        ctr = 1   
    elif ((lst_cube[0][7]) == lst_cube[0][4] and lst_cube[2][4] == lst_cube[5][1]):
        ctr = 1
    elif ((lst_cube[0][8]) == lst_cube[0][4] and lst_cube[2][4] in [lst_cube[1][6],lst_cube[5][2]]):
        ctr = 1

    #top right corner
    elif ((lst_cube[4][8]) == lst_cube[0][4] and lst_cube[2][4] == lst_cube[1][0]):
        ctr = 1   
    elif ((lst_cube[4][8]) == lst_cube[2][4] and lst_cube[0][4] == lst_cube[1][0]):
        ctr = 1   
    elif ((lst_cube[4][5]) == lst_cube[0][4] and lst_cube[2][4] == lst_cube[1][1]):
        ctr = 1   
    elif ((lst_cube[4][5]) == lst_cube[2][4] and lst_cube[0][4] == lst_cube[1][1]):
        ctr = 1            
    elif ((lst_cube[4][2]) == lst_cube[0][4] and lst_cube[2][4] == lst_cube[1][2]):
        ctr = 1   
    elif ((lst_cube[4][2]) == lst_cube[2][4] and lst_cube[0][4] == lst_cube[1][2]):
        ctr = 1   
    
    #top left corner    
    elif ((lst_cube[4][6]) == lst_cube[0][4] and lst_cube[2][4] == lst_cube[3][2]):
        ctr = 1   
    elif ((lst_cube[4][6]) == lst_cube[2][4] and lst_cube[0][4] == lst_cube[3][2]):
        ctr = 1   
    elif ((lst_cube[4][3]) == lst_cube[0][4] and lst_cube[2][4] == lst_cube[3][1]):
        ctr = 1    
    elif ((lst_cube[4][3]) == lst_cube[2][4] and lst_cube[0][4] == lst_cube[3][1]):
        ctr = 1    
    elif ((lst_cube[4][0]) == lst_cube[0][4] and lst_cube[2][4] == lst_cube[3][0]):
        ctr = 1   
    elif ((lst_cube[4][0]) == lst_cube[2][4] and lst_cube[0][4] == lst_cube[3][0]):
        ctr = 1   
    
    #bottom right row
    elif ((lst_cube[5][2]) == lst_cube[0][4] and lst_cube[2][4] == lst_cube[1][6]):
        ctr = 1  
    elif ((lst_cube[5][2]) == lst_cube[2][4] and lst_cube[0][4] == lst_cube[1][6]):
        ctr = 1  
    elif ((lst_cube[5][5]) == lst_cube[0][4] and lst_cube[2][4] == lst_cube[1][7]):
        ctr = 1   
    elif ((lst_cube[5][5]) == lst_cube[2][4] and lst_cube[0][4] == lst_cube[1][7]):
        ctr = 1          
    elif ((lst_cube[5][8]) == lst_cube[0][4] and lst_cube[2][4] == lst_cube[1][8]):
        ctr = 1   
    elif ((lst_cube[5][8]) == lst_cube[2][4] and lst_cube[0][4] == lst_cube[1][8]):
        ctr = 1   
    
    #bottom left row

    elif ((lst_cube[5][0]) == lst_cube[0][4] and lst_cube[2][4] == lst_cube[3][8]):
        ctr = 1  
    elif ((lst_cube[5][0]) == lst_cube[2][4] and lst_cube[0][4] == lst_cube[3][8]):
        ctr = 1  
    elif ((lst_cube[5][3]) == lst_cube[0][4] and lst_cube[2][4] == lst_cube[3][7]):
        ctr = 1    
    elif ((lst_cube[5][3]) == lst_cube[2][4] and lst_cube[0][4] == lst_cube[3][7]):
        ctr = 1 
    elif ((lst_cube[5][6]) == lst_cube[0][4] and lst_cube[2][4] == lst_cube[3][6]):
        ctr = 1 
    elif ((lst_cube[5][6]) == lst_cube[2][4] and lst_cube[0][4] == lst_cube[3][6]):
        ctr = 1   

        
    return ctr


def turn_type1(orig_side):
    turned_side = []
    turned_side.insert(0, orig_side [6])
    turned_side.insert(1, orig_side [3])
    turned_side.insert(2, orig_side [0])
    turned_side.insert(3, orig_side [7])
    turned_side.insert(4, orig_side [4])
    turned_side.insert(5, orig_side [1])
    turned_side.insert(6, orig_side [8])
    turned_side.insert(7, orig_side [5])
    turned_side.insert(8, orig_side [2])
    return turned_side

def turn_type2(orig_side):
    turned_side = []
    turned_side.insert(0, orig_side [2])
    turned_side.insert(1, orig_side [5])
    turned_side.insert(2, orig_side [8])
    turned_side.insert(3, orig_side [1])
    turned_side.insert(4, orig_side [4])
    turned_side.insert(5, orig_side [7])
    turned_side.insert(6, orig_side [0])
    turned_side.insert(7, orig_side [3])
    turned_side.insert(8, orig_side [6])
    return turned_side

def turn_type3(orig_side):
    turned_side = []
    turned_side.insert(0, orig_side [8])
    turned_side.insert(1, orig_side [7])
    turned_side.insert(2, orig_side [6])
    turned_side.insert(3, orig_side [5])
    turned_side.insert(4, orig_side [4])
    turned_side.insert(5, orig_side [3])
    turned_side.insert(6, orig_side [2])
    turned_side.insert(7, orig_side [1])
    turned_side.insert(8, orig_side [0])
    return turned_side

#create an instance of the cube by creating nested list        
lst_cube = ([x for x in parms.get("cube")])

lst_in1, lst_in2, lst_in3, lst_in4, lst_in5, lst_in6 = ([] for i in range(6)) 

for i in range (1,7):
    for j in range(1,10):
        exec(f"lst_in{i}.append(lst_cube.pop(0))")  
        
#create list within a list of the cube.   
lst_opposite_cnt = []
for i in range(1,7):
    exec(f'lst_cube.append(lst_in{i})')
    
print("\n")
print(lst_cube) #blue - front, red - right, green - back, yellow - top

lst_cube_orig = lst_cube[:]

print(lst_cube)


    
########################################

#run checks against the first side. blue - front, red - right, green - back, yellow - top
new_ctr = verify_adj_col()
lst_opposite_cnt.append(new_ctr)
print(f"The counter for blue front and green back is: {new_ctr}")

########################################
#rotate the cube to the right - red - front, green - right, orange - back, yellow - top

first_side = lst_cube.pop(0)
lst_cube.insert(3, first_side)


# rotate the top
orig_side = lst_cube.pop(4)
lst_cube.insert(4, turn_type1(orig_side))
print(lst_cube)

#now rotate the bottom
orig_side = lst_cube.pop(5) 
lst_cube.insert(5, turn_type2(orig_side))
print("\n")
print(lst_cube)

new_ctr = verify_adj_col()
lst_opposite_cnt.append(new_ctr)
print(f"The counter for red front and orange back is: {new_ctr}")

########################################

#rotate the cube - green - front, orange - right, blue - back, yellow - top
first_side = lst_cube.pop(0)
lst_cube.append(first_side)
first_side = lst_cube.pop(5)
lst_cube.insert(3, first_side)
print(lst_cube)

#now rotate the top
orig_side = lst_cube.pop(4)
print(orig_side)
lst_cube.insert(4, turn_type1(orig_side))

#now rotate the bottom
orig_side = lst_cube.pop(5)
print(orig_side)
print(turn_type2(orig_side))
lst_cube.insert(5, turn_type2(orig_side))

print("\n")
print(lst_cube)

new_ctr = verify_adj_col()
lst_opposite_cnt.append(new_ctr)
print(f"The counter for green front and blue back is: {new_ctr}")
########################################

#rotate the cube - orange - front, blue - right, red - back, yellow - top
first_side = lst_cube.pop(0)
lst_cube.append(first_side)
first_side = lst_cube.pop(5)
lst_cube.insert(3, first_side)
print(lst_cube)

#now rotate the top
orig_side = lst_cube.pop(4)
print(orig_side)
print(turn_type1(orig_side))
lst_cube.insert(4, turn_type1(orig_side))

#now rotate the bottom
orig_side = lst_cube.pop(5)
print(orig_side)
print(turn_type2(orig_side))
lst_cube.insert(5, turn_type2(orig_side))

print("\n")
print(lst_cube)

new_ctr = verify_adj_col()
lst_opposite_cnt.append(new_ctr)
print(f"The counter for orange front and red back is: {new_ctr}")

#Rotate back to the beginning. But dont have to check for it again
#blue - front, red - right, green - back, yellow - top


########################################
#flip the cube - yellow - front, red - right, white - back, orange - green

lst_cube = lst_cube_orig[:]
print(lst_cube)

side_0 = lst_cube[4]
print(side_0)
side_1 = lst_cube[1]
#rotate it correctly
side_1 = (turn_type2(side_1))
print(side_1)
side_2 = lst_cube[5]
#rotate side 2
side_2 = (turn_type3(side_2))
print(side_2)
side_3 = lst_cube[3]
#rotate side 3
side_3 = (turn_type1(side_3))
print(side_3)
#rotate side 4
side_4 = lst_cube[2]
side_4 = (turn_type3(side_4))
print(side_4)
side_5 = lst_cube[0]
print(side_5)

lst_cube = []
for i in range(6):
    exec(f'lst_cube.append(side_{i})')


print("\n")
print(lst_cube)

new_ctr = verify_adj_col()
lst_opposite_cnt.append(new_ctr)
print(f"The counter for white front and yellow back is: {new_ctr}")

#####################################################
#last bottom part

lst_cube = lst_cube_orig[:]
print(lst_cube)

#flip the cube - white - front, red - right, yellow - back, blue - top
side_0 = lst_cube[5]
print(side_0)
side_1 = lst_cube[1]
#turn side 1
side_1 = (turn_type1(side_1))
print(side_1)
side_2 = lst_cube[4]
#rotate sdie 2
side_2 = (turn_type3(side_2))
print(side_2)
side_3 = lst_cube[3]
side_3 = (turn_type2(side_3))
print(side_3)
side_4 = lst_cube[0]
print(side_4)
side_5 = lst_cube[2]
#rotate it correctly
side_5 = (turn_type3(side_5))
print(side_5)

lst_cube = []
for i in range(6):
    exec(f'lst_cube.append(side_{i})')


print("\n")
print(lst_cube)

new_ctr = verify_adj_col()
lst_opposite_cnt.append(new_ctr)
print(f"The counter for white front and yellow back is: {new_ctr}")

new_ctr = verify_adj_col()
lst_opposite_cnt.append(new_ctr)
print(f"The counter for yellow front and white back is: {new_ctr}")
    
print(lst_opposite_cnt)
max_opposite_ctr = max(lst_opposite_cnt)
print(max_opposite_ctr)