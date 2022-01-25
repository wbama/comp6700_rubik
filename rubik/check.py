import rubik.cube as rubik

def _check(parms):
    
#put this try except in, if string is a number, or missing cube key, will throw errors here
    
    try:
        parm_string = parms.get("cube")    
        unique_color = []
        dict_col = {}
        result={}
        
        for char in parm_string:
            if char not in unique_color:
                unique_color.append(char) 
        lst_cube_center = ([x for x in parms.get("cube")])[4::9]
        unique_center = []
        for char in lst_cube_center:
            if char not in unique_center:
                unique_center.append(char)             
                
        #create a dictionary of the colors. Use to count colors
        
        keys = ["col1", "col2","col3", "col4", "col5", "col6"]
        for i in range(len(keys)):
            dict_col[keys[i]] = unique_color[i]
        
        #create a flag. Should be 9 blocks of each color. 
        col_flag = 0   
        for vals in dict_col.values():
            if parm_string.count(vals) != 9:
                col_flag = 1              
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
    elif (len(parms.get("cube")) < 54):
        result['status'] = 'error: cube string is too small'
        
    elif (len(parms.get("cube")) > 54):
        result['status'] = 'error: cube string is too large'    
       
    #has 6 colors
    elif len(set(parms.get("cube"))) < 6:    
        cub_len = len(set(parms.get("cube")))  #get the length of the cube          
        result['status'] = (f"error: There are {cub_len} colors. There should be 6.\n The colors in this cube are {unique_color}")        
     
    #has 9 occurrences of the 6 colors
    elif (col_flag == 1):
        result['status'] = 'error: one of the colors is more or less than 9 occurrences'
            
    #each middle face is a different color
    elif len(unique_center) != 6:
        result['status'] = 'error: two middle faces are the same colors'   
          
    #no color can be adjacent to a color that would appear on the opposite side of the cube when solved
    #what is opposite side of the cube?
    #how identify one side solved?
        
    else:
        result['status'] = 'ok'
    return result