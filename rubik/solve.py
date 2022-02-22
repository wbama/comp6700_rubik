import rubik.cube as rubik

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
    
    print("\nThe list cube")
    print(lst_cube) #blue - front, yellow - right, green - back, yellow - top


###############################################################################
    if inputDict['rotate'] == 'F':
        c_rotate_cube = (turn_clock(lst_cube))
    elif inputDict['rotate'] == 'f':
        c_rotate_cube = (turn_cclock(lst_cube))        
    elif inputDict['rotate'] == 'R':
        c_rotate_cube = (turn_clock(lst_cube))
    elif inputDict['rotate'] == 'r':
        c_rotate_cube = (turn_cclock(lst_cube))
    elif inputDict['rotate'] == 'B':
        c_rotate_cube = (turn_clock(lst_cube))        
    elif inputDict['rotate'] == 'b':
        c_rotate_cube = (turn_cclock(lst_cube))
    elif inputDict['rotate'] == 'L':
        c_rotate_cube = (turn_clock(lst_cube))
    elif inputDict['rotate'] == 'l':
        c_rotate_cube = (turn_cclock(lst_cube))
    elif inputDict['rotate'] == 'U':
        c_rotate_cube = (turn_clock(lst_cube))        
    elif inputDict['rotate'] == 'u':
        c_rotate_cube = (turn_cclock(lst_cube))
    elif inputDict['rotate'] == 'D':
        c_rotate_cube = (turn_clock(lst_cube))        
    elif inputDict['rotate'] == 'd':
        c_rotate_cube = (turn_cclock(lst_cube))
    else:
        print("missing rotate")
        c_rotate_cube = (turn_clock(lst_cube))
        

    print("\nRotated cube")
    print(c_rotate_cube)
    
    str1 = "".join(c_rotate_cube[0])
    str2 = "".join(c_rotate_cube[1])
    str3 = "".join(c_rotate_cube[2])
    str4 = "".join(c_rotate_cube[3])
    str5 = "".join(c_rotate_cube[4])
    str6 = "".join(c_rotate_cube[5])                       
 
    str_cube = str1+str2+str3+str4+str5+str6
    print("\nString Cube")
    print(str_cube)
    
    result = {}
    result['cube'] = str_cube
    result['rotate'] = 'F'
    result['status'] = 'ok'
    return result    
    






# validate my parms, if invalid, need to return status with error
# if everything is valid, load parms into cube modell
# then rotate the cube model in the desired direction
# serialize the cube model in encoded cube into a string
# return the string result + status of "ok"


# but have to write the test code first


