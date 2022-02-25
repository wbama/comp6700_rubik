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
        for rotation in (parms.get('rotate')):
            print(rotation)
            if rotation in ['F','f','R','r','B','b','L','l','U','u','D','d'] or rotation == '':                
                result['status'] = 'ok'                
            else:
                result['status'] = ('error: optional rotate should be in [FfRrBbLlUuDd], "" or None')
                  
            
    elif (parms.get('cube',None)).isalnum() == False:
        result['status'] = ('error: only letters and numbers in the cube string')
       
    else:
        result['status'] = 'ok'
    return result

