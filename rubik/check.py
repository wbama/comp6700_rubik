import rubik.cube as rubik

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
        print(lst_cube)

        lst_in1, lst_in2, lst_in3, lst_in4, lst_in5, lst_in6 = ([] for i in range(6)) #

        for i in range (1,7):
            for j in range(1,10):
                exec(f"lst_in{i}.append(lst_cube.pop(0))")   
        
        #if front cube is solved, back cube should also be solved
        lst_cb_out = []
        for i in range(1,7):
            exec(f'lst_cb_out.append(lst_in{i})')
            
        def verify_adj_col():
            
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
        
            return ctr

        #create an instance of the cube by creating nested list        
        lst_cube = ([x for x in parms.get("cube")])
#        print(lst_cube)
        
        lst_in1, lst_in2, lst_in3, lst_in4, lst_in5, lst_in6 = ([] for i in range(6)) 
        
        for i in range (1,7):
            for j in range(1,10):
                exec(f"lst_in{i}.append(lst_cube.pop(0))")  
                
        #create list within a list of the cube.   
        lst_cube = []
        lst_opposite_cnt = []
        for i in range(1,7):
            exec(f'lst_cube.append(lst_in{i})')
            
  
        #run checks against the first side. blue - front, red - right, green - back, yellow - top
        new_ctr = verify_adj_col()
        lst_opposite_cnt.append(new_ctr)
#        print("\n")
#        print(lst_cube)

        
        #rotate the cube - red - front, green - right, orange - back, yellow - top
        first_side = lst_cube.pop(0)
        lst_cube.append(first_side)
        first_side = lst_cube.pop(5)
        lst_cube.insert(3, first_side)
#        print("\n")
#        print(lst_cube)

        
        new_ctr = verify_adj_col()
        lst_opposite_cnt.append(new_ctr)

        
        #rotate the cube - green - front, orange - right, blue - back, yellow - top
        first_side = lst_cube.pop(0)
        lst_cube.append(first_side)
        first_side = lst_cube.pop(5)
        lst_cube.insert(3, first_side)
#        print("\n")
#        print(lst_cube)
        
        new_ctr = verify_adj_col()
        lst_opposite_cnt.append(new_ctr)
        
        #rotate the cube - orange - front, blue - right, red - back, yellow - top
        first_side = lst_cube.pop(0)
        lst_cube.append(first_side)
        first_side = lst_cube.pop(5)
        lst_cube.insert(3, first_side)
#        print("\n")
#        print(lst_cube)
    
        new_ctr = verify_adj_col()
        lst_opposite_cnt.append(new_ctr)

        
        #flip the cube - white - front, orange - right, yellow - back, green - top
        first_side = lst_cube.pop(5)
        lst_cube.insert(0, first_side)
        first_side = lst_cube.pop(5)
        lst_cube.insert(2, first_side)
        first_side = lst_cube.pop(4)
        lst_cube.insert(3, first_side)
        first_side = lst_cube.pop(4)
        lst_cube.append(first_side)
#        print("\n")
#        print(lst_cube)
        
        new_ctr = verify_adj_col()
        lst_opposite_cnt.append(new_ctr)
        
        #flip the cube - yellow - front, orange - right, white - back, blue - top
        first_side = lst_cube.pop(2)
        lst_cube.insert(0, first_side)
        first_side = lst_cube.pop(2)
        lst_cube.insert(1, first_side)
        first_side = lst_cube.pop(4)
        lst_cube.append(first_side)
#        print("\n")
#        print(lst_cube)
        
        new_ctr = verify_adj_col()
        lst_opposite_cnt.append(new_ctr)
#        print(f"The counter for yellow front and white back is: {new_ctr}")
            
#        print(lst_opposite_cnt)
        max_opposite_ctr = max(lst_opposite_cnt)
#        print(max_opposite_ctr)
              
    except:
        pass #one of the below will catch errors
            
    encodedCube = parms.get('cube',None)  
    
    # is present 
    if(encodedCube == None):
        result['status'] = 'error: no cube found'
    
    #is a string  
    elif isinstance(parms.get("cube"), str) != True:
        result['status'] = 'error: cube not a string'
        
    #has 54 elements
    elif (len(parms.get("cube")) != 54):
        cub_len = len((parms.get("cube")))  #get the length of the cube   
        result['status'] = (f'error: cube string has to have 54 elements. It has {cub_len} elements.')
           
    #has 6 colors
    elif len(set(parms.get("cube"))) != 6:    
        cub_col = len(set(parms.get("cube")))  #get the colors of the cube         
        result['status'] = (f"error: there are {cub_col} colors. There should be 6.\n The colors in this cube are {unique_color}")        
     
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