"""
    Created on 03/05/2022
    @author: Waldo du Toit
    check string inputs
    
"""

import rubik.cube as rubik
from rubik.solveRotations import *

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
        lst_cube = createCubeListFromInputParms(parms)            
  
        # def turn_type1(orig_side):
        #     turned_side = []
        #     turned_side.insert(0, orig_side [6])
        #     turned_side.insert(1, orig_side [3])
        #     turned_side.insert(2, orig_side [0])
        #     turned_side.insert(3, orig_side [7])
        #     turned_side.insert(4, orig_side [4])
        #     turned_side.insert(5, orig_side [1])
        #     turned_side.insert(6, orig_side [8])
        #     turned_side.insert(7, orig_side [5])
        #     turned_side.insert(8, orig_side [2])
        #     return turned_side
        #
        # def turn_type2(orig_side):
        #     turned_side = []
        #     turned_side.insert(0, orig_side [2])
        #     turned_side.insert(1, orig_side [5])
        #     turned_side.insert(2, orig_side [8])
        #     turned_side.insert(3, orig_side [1])
        #     turned_side.insert(4, orig_side [4])
        #     turned_side.insert(5, orig_side [7])
        #     turned_side.insert(6, orig_side [0])
        #     turned_side.insert(7, orig_side [3])
        #     turned_side.insert(8, orig_side [6])
        #     return turned_side
        #
        # def turn_type3(orig_side):
        #     turned_side = []
        #     turned_side.insert(0, orig_side [8])
        #     turned_side.insert(1, orig_side [7])
        #     turned_side.insert(2, orig_side [6])
        #     turned_side.insert(3, orig_side [5])
        #     turned_side.insert(4, orig_side [4])
        #     turned_side.insert(5, orig_side [3])
        #     turned_side.insert(6, orig_side [2])
        #     turned_side.insert(7, orig_side [1])
        #     turned_side.insert(8, orig_side [0])
        #     return turned_side     

                    
        ########################################
        lst_opposite_cnt = []
        #run checks against the first side. blue - front, red - right, green - back, yellow - top
        # new_ctr = verify_adj_col()
        new_ctr = verifyAdjacentColors(lst_cube)
        lst_opposite_cnt.append(new_ctr)
                
        ########################################
        #rotate the cube to the right - red - front, green - right, orange - back, yellow - top
        lst_cube = rotateCubeToRight(lst_cube)        
        
        new_ctr = verifyAdjacentColors(lst_cube)
        lst_opposite_cnt.append(new_ctr)
        
        ########################################
        
        #rotate the cube to right again - green - front, orange - right, blue - back, yellow - top
        lst_cube = rotateCubeToRight(lst_cube)
        
        new_ctr = verifyAdjacentColors(lst_cube)
        lst_opposite_cnt.append(new_ctr)

        ########################################
        lst_cube = rotateCubeToRight(lst_cube)
        
        new_ctr = verifyAdjacentColors(lst_cube)
        lst_opposite_cnt.append(new_ctr)
        
        #Rotate back to the beginning. But dont have to check for it again
        #blue - front, red - right, green - back, yellow - top
        
        
        ########################################
        #flip the cube - yellow - front, red - right, white - back, orange - green
        lst_cube = rotateCubeToRight(lst_cube)
        lst_cube = rotateCubeUp(lst_cube)       

     
        new_ctr = verifyAdjacentColors(lst_cube)
        lst_opposite_cnt.append(new_ctr)

        #####################################################
        #last bottom part
        lst_cube = rotateCubeDown(lst_cube)
        lst_cube = rotateCubeDown(lst_cube)
        
        new_ctr = verifyAdjacentColors(lst_cube)
        lst_opposite_cnt.append(new_ctr)

        new_ctr = verifyAdjacentColors(parms)
        lst_opposite_cnt.append(new_ctr)   
        print(lst_opposite_cnt)

             
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
          
    elif (max(lst_opposite_cnt) > 0):
        result['status'] = 'error: adjacent color to color that would appear on opposite side' 
        
    else:
        result['status'] = 'ok'
    return result