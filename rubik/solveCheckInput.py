#    check the input string

def solveCheck(parms):  
    result = {} 
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

        lst_in1, lst_in2, lst_in3, lst_in4, lst_in5, lst_in6 = ([] for i in range(6)) #

        for i in range (1,7):
            for j in range(1,10):
                exec(f"lst_in{i}.append(lst_cube.pop(0))")   

        for i in range(1,7):
            exec(f'lst_cb_out.append(lst_in{i})')
            
 
        #create an instance of the cube by creating nested list        
        # lst_cube = ([x for x in parms.get("cube")])
        #
        # lst_in1, lst_in2, lst_in3, lst_in4, lst_in5, lst_in6 = ([] for i in range(6)) 
        #
        # for i in range (1,7):
        #     for j in range(1,10):
        #         exec(f"lst_in{i}.append(lst_cube.pop(0))")                 


        for i in range(1,7):
            exec(f'lst_cube.append(lst_in{i})')    

          
    except:
        pass #one of the below will catch errors
            
   
    # is present 
    if(parms.get('cube',None) == None):
        result['status'] = ('error: no cube found')
    
    #is a string  
    elif isinstance(parms.get("cube"), str) != True:
        result['status'] = 'error: cube not a string'
        
    #has 54 elements
    elif (len(parms.get("cube")) != 54): 
        result['status'] = ('error: cube string has to have 54 elements')
           
    #has 6 colors
    elif len(set(parms.get("cube"))) != 6:    
        result['status'] = ('error: There should be 6 colors')        
     
    #has 9 occurrences of the 6 colors
    elif (max(lst_cnt_blocks)!= 9):
        result['status'] = ('error: one of the colors is more or less than 9 occurrences')
            
    #each middle face is a different color
    elif len(unique_center) != 6:
        result['status'] = ('error: two middle faces are the same colors')  
        
    elif 'rotate' in parms:
        if (parms.get('rotate', None)) not in ['F','f','R','r','B','b','L','l','U','u','D','d', '', None]:
            result['status'] = ('error: optional rotate should be single letter [FfRrBbLlUuDd], '' or None')   
        else:
            result['status'] = 'ok'   
            
    elif (parms.get('cube',None)).isalnum() == False:
        result['status'] = ('error: only letters and numbers in the cube string')
       
    else:
        result['status'] = 'ok'
    return result

