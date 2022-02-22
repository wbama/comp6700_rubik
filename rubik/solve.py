import rubik.cube as rubik

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

def rotate_cube_to_right(cube):
        #rotate cube to right
        first_side = cube.pop(0)
        cube.insert(3, first_side)        
        # rotate the top
        orig_side = cube.pop(4)
        cube.insert(4, turn_type1(orig_side))        
        #now rotate the bottom
        orig_side = cube.pop(5) 
        cube.insert(5, turn_type2(orig_side))
        return cube
    
def flip_cube_top_side(cube):
        side_0 = cube[4]

        side_1 = cube[1]
        #rotate it correctly
        side_1 = (turn_type2(side_1))
        side_2 = cube[5]
        #rotate side 2
        side_2 = (turn_type3(side_2))
        side_3 = cube[3]
        #rotate side 3
        side_3 = (turn_type1(side_3))
        #rotate side 4
        side_4 = cube[2]
        side_4 = (turn_type3(side_4))
        side_5 = cube[0]        
        cube = []
        for i in range(6):
            exec(f'cube.append(side_{i})') 
               
        return cube

def turn_clock(orig_side):
    new_cube = [[], [], [], [], [], []]
    #front
    new_cube[0].insert(0, orig_side [0][6])
    new_cube[0].insert(1, orig_side [0][3])
    new_cube[0].insert(2, orig_side [0][0])
    new_cube[0].insert(3, orig_side [0][7])
    new_cube[0].insert(4, orig_side [0][4])
    new_cube[0].insert(5, orig_side [0][1])
    new_cube[0].insert(6, orig_side [0][8])
    new_cube[0].insert(7, orig_side [0][5])
    new_cube[0].insert(8, orig_side [0][2])
    
    #right    
    new_cube[1].insert(0, orig_side [4][6])
    new_cube[1].insert(1, orig_side [1][1])
    new_cube[1].insert(2, orig_side [1][2])
    new_cube[1].insert(3, orig_side [4][7])
    new_cube[1].insert(4, orig_side [1][4])
    new_cube[1].insert(5, orig_side [1][5])
    new_cube[1].insert(6, orig_side [4][8])
    new_cube[1].insert(7, orig_side [1][7])
    new_cube[1].insert(8, orig_side [1][8])
    
    #back    
    new_cube[2].insert(0, orig_side [2][0])
    new_cube[2].insert(1, orig_side [2][1])
    new_cube[2].insert(2, orig_side [2][2])
    new_cube[2].insert(3, orig_side [2][3])
    new_cube[2].insert(4, orig_side [2][4])
    new_cube[2].insert(5, orig_side [2][5])
    new_cube[2].insert(6, orig_side [2][6])
    new_cube[2].insert(7, orig_side [2][7])
    new_cube[2].insert(8, orig_side [2][8])
    
    #left    
    new_cube[3].insert(0, orig_side [3][0])
    new_cube[3].insert(1, orig_side [3][1])
    new_cube[3].insert(2, orig_side [5][0])
    new_cube[3].insert(3, orig_side [3][3])
    new_cube[3].insert(4, orig_side [3][4])
    new_cube[3].insert(5, orig_side [5][1])
    new_cube[3].insert(6, orig_side [3][6])
    new_cube[3].insert(7, orig_side [3][7])
    new_cube[3].insert(8, orig_side [5][2])
    
    #top    
    new_cube[4].insert(0, orig_side [4][0])
    new_cube[4].insert(1, orig_side [4][1])
    new_cube[4].insert(2, orig_side [4][2])
    new_cube[4].insert(3, orig_side [4][3])
    new_cube[4].insert(4, orig_side [4][4])
    new_cube[4].insert(5, orig_side [4][5])
    new_cube[4].insert(6, orig_side [3][8])
    new_cube[4].insert(7, orig_side [3][5])
    new_cube[4].insert(8, orig_side [3][2])
    
    #bottom    
    new_cube[5].insert(0, orig_side [1][6])
    new_cube[5].insert(1, orig_side [1][3])
    new_cube[5].insert(2, orig_side [1][0])
    new_cube[5].insert(3, orig_side [5][3])
    new_cube[5].insert(4, orig_side [5][4])
    new_cube[5].insert(5, orig_side [5][5])
    new_cube[5].insert(6, orig_side [5][6])
    new_cube[5].insert(7, orig_side [5][7])
    new_cube[5].insert(8, orig_side [5][8])
    return new_cube

def turn_cclock(orig_side):
    new_cube = [[], [], [], [], [], []]
    #front
    new_cube[0].insert(0, orig_side [0][2])
    new_cube[0].insert(1, orig_side [0][5])
    new_cube[0].insert(2, orig_side [0][8])
    new_cube[0].insert(3, orig_side [0][1])
    new_cube[0].insert(4, orig_side [0][4])
    new_cube[0].insert(5, orig_side [0][7])
    new_cube[0].insert(6, orig_side [0][0])
    new_cube[0].insert(7, orig_side [0][3])
    new_cube[0].insert(8, orig_side [0][6])
    
    #right- takes from 5
    new_cube[1].insert(0, orig_side [5][2])
    new_cube[1].insert(1, orig_side [1][1])
    new_cube[1].insert(2, orig_side [1][2])
    new_cube[1].insert(3, orig_side [5][1])
    new_cube[1].insert(4, orig_side [1][4])
    new_cube[1].insert(5, orig_side [1][5])
    new_cube[1].insert(6, orig_side [5][0])
    new_cube[1].insert(7, orig_side [1][7])
    new_cube[1].insert(8, orig_side [1][8])
    
    #back  - stays same  
    new_cube[2].insert(0, orig_side [2][0])
    new_cube[2].insert(1, orig_side [2][1])
    new_cube[2].insert(2, orig_side [2][2])
    new_cube[2].insert(3, orig_side [2][3])
    new_cube[2].insert(4, orig_side [2][4])
    new_cube[2].insert(5, orig_side [2][5])
    new_cube[2].insert(6, orig_side [2][6])
    new_cube[2].insert(7, orig_side [2][7])
    new_cube[2].insert(8, orig_side [2][8])
    
    #left - takes from 4
    new_cube[3].insert(0, orig_side [3][0])
    new_cube[3].insert(1, orig_side [3][1])
    new_cube[3].insert(2, orig_side [4][8])
    new_cube[3].insert(3, orig_side [3][3])
    new_cube[3].insert(4, orig_side [3][4])
    new_cube[3].insert(5, orig_side [4][7])
    new_cube[3].insert(6, orig_side [3][6])
    new_cube[3].insert(7, orig_side [3][7])
    new_cube[3].insert(8, orig_side [4][6])
    
    #top - takes from 1  
    new_cube[4].insert(0, orig_side [4][0])
    new_cube[4].insert(1, orig_side [4][1])
    new_cube[4].insert(2, orig_side [4][2])
    new_cube[4].insert(3, orig_side [4][3])
    new_cube[4].insert(4, orig_side [4][4])
    new_cube[4].insert(5, orig_side [4][5])
    new_cube[4].insert(6, orig_side [1][0])
    new_cube[4].insert(7, orig_side [1][3])
    new_cube[4].insert(8, orig_side [1][6])
    
    #bottom - takes from 3
    new_cube[5].insert(0, orig_side [3][2])
    new_cube[5].insert(1, orig_side [3][5])
    new_cube[5].insert(2, orig_side [3][8])
    new_cube[5].insert(3, orig_side [5][3])
    new_cube[5].insert(4, orig_side [5][4])
    new_cube[5].insert(5, orig_side [5][5])
    new_cube[5].insert(6, orig_side [5][6])
    new_cube[5].insert(7, orig_side [5][7])
    new_cube[5].insert(8, orig_side [5][8])
    return new_cube

def _solve(parms):
    
    inputDict = {}
    ctr = 0
    inputDict['op'] = 'solve'
    inputDict['rotate'] = parms.get("rotate")
    inputDict['cube'] = parms.get("cube")
    
    lst_cube = ([x for x in inputDict.get("cube")])
    lst_in1, lst_in2, lst_in3, lst_in4, lst_in5, lst_in6 = ([] for i in range(6)) 

    for i in range (1,7):
        for j in range(1,10):
            exec(f"lst_in{i}.append(lst_cube.pop(0))")  
        
    #create list within a list of the cube.   
    lst_opposite_cnt = []
    for i in range(1,7):
        exec(f'lst_cube.append(lst_in{i})')
    
###############################################################################
    global warnstring

    if inputDict['rotate'] == 'F':
         c_rotate_cube = (turn_clock(lst_cube))  
      
        
    elif inputDict['rotate'] == 'f':
        c_rotate_cube = (turn_cclock(lst_cube))          
             
    elif inputDict['rotate'] == 'R':
       
        rotate_cube_to_right(lst_cube)
        
        #rotate Right side clockwise
        c_rotate_cube = (turn_clock(lst_cube)) 
        
        rotate_cube_to_right(c_rotate_cube)
        rotate_cube_to_right(c_rotate_cube)
        rotate_cube_to_right(c_rotate_cube)  
        
              
    elif inputDict['rotate'] == 'r':
        c_rotate_cube = (turn_cclock(lst_cube))
        
      
        rotate_cube_to_right(lst_cube)
        
        #rotate Right side clockwise
        c_rotate_cube = (turn_cclock(lst_cube)) 
        
        rotate_cube_to_right(c_rotate_cube)
        rotate_cube_to_right(c_rotate_cube)
        rotate_cube_to_right(c_rotate_cube)  
              
        
    elif inputDict['rotate'] == 'B':
        
        rotate_cube_to_right(lst_cube)
        rotate_cube_to_right(lst_cube)
        
        #rotate Right side clockwise
        c_rotate_cube = (turn_clock(lst_cube))         
        
        rotate_cube_to_right(c_rotate_cube)
        rotate_cube_to_right(c_rotate_cube)  
        
     
    elif inputDict['rotate'] == 'b':
        rotate_cube_to_right(lst_cube)
        rotate_cube_to_right(lst_cube)
        
        #rotate Right side clockwise
        c_rotate_cube = (turn_cclock(lst_cube))         
        
        rotate_cube_to_right(c_rotate_cube)
        rotate_cube_to_right(c_rotate_cube) 
       
         
    elif inputDict['rotate'] == 'L':
      
        rotate_cube_to_right(lst_cube)
        rotate_cube_to_right(lst_cube)
        rotate_cube_to_right(lst_cube)
        
        #rotate Right side clockwise
        c_rotate_cube = (turn_clock(lst_cube))       
        
        rotate_cube_to_right(c_rotate_cube)  
             
        
        
    elif inputDict['rotate'] == 'l':        
        
        rotate_cube_to_right(lst_cube)
        rotate_cube_to_right(lst_cube)
        rotate_cube_to_right(lst_cube)
        
        #rotate Right side clockwise
        c_rotate_cube = (turn_cclock(lst_cube))       
        
        rotate_cube_to_right(c_rotate_cube)  
           
        
    elif inputDict['rotate'] == 'U':
        
        flip_cube_one = flip_cube_top_side(lst_cube)
        c_rotate_cube = (turn_clock(flip_cube_one)) 
        flip_cube_two = flip_cube_top_side(c_rotate_cube)
        flip_cube_three= flip_cube_top_side(flip_cube_two)
        c_rotate_cube= flip_cube_top_side(flip_cube_three)   
          
              
    elif inputDict['rotate'] == 'u':
        
        flip_cube_one = flip_cube_top_side(lst_cube)
        c_rotate_cube = (turn_cclock(flip_cube_one)) 
        flip_cube_two = flip_cube_top_side(c_rotate_cube)
        flip_cube_three= flip_cube_top_side(flip_cube_two)
        c_rotate_cube= flip_cube_top_side(flip_cube_three)
        

    elif inputDict['rotate'] == 'D':
         
        flip_cube_one = flip_cube_top_side(lst_cube)
        
        flip_cube_two = flip_cube_top_side(flip_cube_one)

        flip_cube_three = flip_cube_top_side(flip_cube_two)

        c_rotate_cube = (turn_clock(flip_cube_three)) 

        flip_cube_four = flip_cube_top_side(c_rotate_cube)
        c_rotate_cube= flip_cube_four
       

        
    elif inputDict['rotate'] == 'd':
        flip_cube_one = flip_cube_top_side(lst_cube)        
        flip_cube_two = flip_cube_top_side(flip_cube_one)
        flip_cube_three = flip_cube_top_side(flip_cube_two)
        c_rotate_cube = (turn_cclock(flip_cube_three)) 
        flip_cube_four = flip_cube_top_side(c_rotate_cube)
        c_rotate_cube= flip_cube_four

        
    else:
        c_rotate_cube = (turn_clock(lst_cube))     

   
    str1 = "".join(c_rotate_cube[0])
    str2 = "".join(c_rotate_cube[1])
    str3 = "".join(c_rotate_cube[2])
    str4 = "".join(c_rotate_cube[3])
    str5 = "".join(c_rotate_cube[4])
    str6 = "".join(c_rotate_cube[5])                       
 
    str_cube = str1+str2+str3+str4+str5+str6
    
    result = {}
    result['cube'] = str_cube
    result['status'] = warnstring
    return result    


# validate my parms, if invalid, need to return status with error
# if everything is valid, load parms into cube modell
# then rotate the cube model in the desired direction
# serialize the cube model in encoded cube into a string
# return the string result + status of "ok"


# but have to write the test code first


