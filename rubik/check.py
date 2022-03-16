"""
    Created on 03/05/2022
    @author: Waldo du Toit
    check string inputs
    
"""

import rubik.cube as rubik
from rubik.solveRotations import verifyAdjacentColors

def _check(parms):

    result={}
   
#put this try except in, if string is a number, or missing cube key, will throw errors here
    
    try:
        parm_string = parms.get("cube")  #get the string
          
        unique_color = [] #create list with all the unique colors in it
        for char in parm_string:
            if char not in unique_color:
                unique_color.append(char) 
            
                
        #create a dictionary of the colors. Use to count colors 
        dict_col = {}       
        keys = ["col1", "col2","col3", "col4", "col5", "col6"]
        for i in range(len(keys)):
            dict_col[keys[i]] = unique_color[i]
        
        #create list to count the blocks 
        lst_cnt_blocks = []
        for vals in dict_col.values():
            lst_cnt_blocks.append(parm_string.count(vals))  
            
        #make a list of the center colors. Should be 6 different ones       
        lst_cube_center = ([x for x in parms.get("cube")])[4::9]
        
        unique_center = []
        for char in lst_cube_center:
            if char not in unique_center:
                unique_center.append(char)               
              
        #create an instance of the cube by creating nested list
        lst_cube = ([x for x in parms.get("cube")])
        
        lst_in1, lst_in2, lst_in3, lst_in4, lst_in5, lst_in6 = ([] for i in range(6))         
        
        for i in range (1,7):
             for j in range(1,10):
                 exec(f"lst_in{i}.append(lst_cube.pop(0))")
        
 
        
        #this function looks at the colors around the edge and compares to the back colors to add to counter
        #create an instance of the cube by creating nested list        
        lst_cube = ([x for x in parms.get("cube")])
      
        lst_in1, lst_in2, lst_in3, lst_in4, lst_in5, lst_in6 = ([] for i in range(6)) 
        
        for i in range (1,7):
            for j in range(1,10):
                exec(f"lst_in{i}.append(lst_cube.pop(0))")  
                
        #create list within a list of the cube.   
        lst_cube = []
        lst_opposite_cnt = []
        for i in range(1,7):
            exec(f'lst_cube.append(lst_in{i})')
            
  
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
            
     
        lst_cube_orig = lst_cube[:]  
                    
        ########################################
        
        #run checks against the first side. blue - front, red - right, green - back, yellow - top
        # new_ctr = verify_adj_col()
        new_ctr = verifyAdjacentColors(parms)
        print(new_ctr)
        lst_opposite_cnt.append(new_ctr)
                
        ########################################
        #rotate the cube to the right - red - front, green - right, orange - back, yellow - top
        
        first_side = lst_cube.pop(0)
        lst_cube.insert(3, first_side)
        
        # rotate the top
        orig_side = lst_cube.pop(4)
        lst_cube.insert(4, turn_type1(orig_side))
        
        #now rotate the bottom
        orig_side = lst_cube.pop(5) 
        lst_cube.insert(5, turn_type2(orig_side))
        
        new_ctr = verifyAdjacentColors(parms)
        lst_opposite_cnt.append(new_ctr)
        
        ########################################
        
        #rotate the cube - green - front, orange - right, blue - back, yellow - top
        first_side = lst_cube.pop(0)
        lst_cube.append(first_side)
        first_side = lst_cube.pop(5)
        lst_cube.insert(3, first_side)

        #now rotate the top
        orig_side = lst_cube.pop(4)
        lst_cube.insert(4, turn_type1(orig_side))
        
        #now rotate the bottom
        orig_side = lst_cube.pop(5)
        lst_cube.insert(5, turn_type2(orig_side))
        
        new_ctr = verifyAdjacentColors(parms)
        lst_opposite_cnt.append(new_ctr)

        ########################################
        
        #rotate the cube - orange - front, blue - right, red - back, yellow - top
        first_side = lst_cube.pop(0)
        lst_cube.append(first_side)
        first_side = lst_cube.pop(5)
        lst_cube.insert(3, first_side)
        
        #now rotate the top
        orig_side = lst_cube.pop(4)
        lst_cube.insert(4, turn_type1(orig_side))
        
        #now rotate the bottom
        orig_side = lst_cube.pop(5)

        lst_cube.insert(5, turn_type2(orig_side))
        
        new_ctr = verifyAdjacentColors(parms)
        lst_opposite_cnt.append(new_ctr)
        
        #Rotate back to the beginning. But dont have to check for it again
        #blue - front, red - right, green - back, yellow - top
        
        
        ########################################
        #flip the cube - yellow - front, red - right, white - back, orange - green
        
        lst_cube = lst_cube_orig[:]
        
        side_0 = lst_cube[4]

        side_1 = lst_cube[1]
        #rotate it correctly
        side_1 = (turn_type2(side_1))

        side_2 = lst_cube[5]
        #rotate side 2
        side_2 = (turn_type3(side_2))

        side_3 = lst_cube[3]
        #rotate side 3
        side_3 = (turn_type1(side_3))

        #rotate side 4
        side_4 = lst_cube[2]
        side_4 = (turn_type3(side_4))

        side_5 = lst_cube[0]

        
        lst_cube = []
        for i in range(6):
            exec(f'lst_cube.append(side_{i})')     
        
     
        new_ctr = verifyAdjacentColors(parms)
        lst_opposite_cnt.append(new_ctr)

        #####################################################
        #last bottom part
        
        lst_cube = lst_cube_orig[:]
        
        #flip the cube - white - front, red - right, yellow - back, blue - top
        side_0 = lst_cube[5]

        side_1 = lst_cube[1]
        #turn side 1
        side_1 = (turn_type1(side_1))

        side_2 = lst_cube[4]
        #rotate side 2
        side_2 = (turn_type3(side_2))
        #rotate side 3
        side_3 = lst_cube[3]
        side_3 = (turn_type2(side_3))

        side_4 = lst_cube[0]

        side_5 = lst_cube[2]
        #rotate side 5
        side_5 = (turn_type3(side_5))
        
        lst_cube = []
        for i in range(6):
            exec(f'lst_cube.append(side_{i})')

        
        new_ctr = verifyAdjacentColors(parms)
        lst_opposite_cnt.append(new_ctr)

        new_ctr = verifyAdjacentColors(parms)
        lst_opposite_cnt.append(new_ctr)   

        max_opposite_ctr = max(lst_opposite_cnt)
             
    except:
        pass #one of the below will catch errors
            
    encodedCube = parms.get('cube',None)  
    
    # is present 
    if(encodedCube == None):
        result['status'] = 'error: no cube found'
    
    #is a string  
    elif isinstance(parms.get("cube"), str) != True:
        result['status'] = 'error: cube not a string'
        
    #valid characters   
    elif ((parms.get('cube')).isalnum())== False:
        result['status'] = ('error: only alphanumeric characters in the cube string')   
        
    #has 54 elements
    elif (len(parms.get("cube")) != 54):
        result['status'] = ('error: cube string has to have 54 elements')
           
    #has 6 colors
    elif len(set(parms.get("cube"))) != 6:    
        result['status'] = ("error: there should be 6 colors")        
     
    #has 9 occurrences of the 6 colors
    elif (max(lst_cnt_blocks)!= 9):
        result['status'] = 'error: one of the colors is more or less than 9 occurrences'
            
    #each middle face is a different color
    elif len(unique_center) != 6:
        result['status'] = 'error: two middle faces are the same colors'   
          
    elif (max_opposite_ctr > 0):
        result['status'] = 'error: adjacent color to color that would appear on opposite side' 
        
    else:
        result['status'] = 'ok'
    return result