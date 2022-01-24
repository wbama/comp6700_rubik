import rubik.cube as rubik

def _check(parms):
    result={}

    cub_len = len(set(parms.get("cube")))
        
    parm_string = parms.get("cube")
    unique = []
    for char in parm_string:
        if char not in unique:
            unique.append(char) 
    
    #create a dictionary of the colors. Use later
    dict_col = {}
    keys = ["col1", "col2","col3", "col4", "col5", "col6"]
    for i in range(len(keys)):
        dict_col[keys[i]] = unique[i]
        
    #create a flag. Should be 9 blocks of each color. 
    col_flag = 0   
    for vals in dict_col.values():
        if parm_string.count(vals) != 9:
            col_flag = 1
    
    encodedCube = parms.get('cube',None)  
    
    # first check if there is a cube key     
    if(encodedCube == None):
        result['status'] = 'error: no cube found'
    
    #does cube have number instead of characters    
    elif isinstance(parms.get("cube"), str) != True:
        result['status'] = 'error: cube string not characters'
        
    #there has to be exactly 54 blocks
    elif (len(parms.get("cube")) < 54):
        result['status'] = 'error: cube string is too small'
        
    elif (len(parms.get("cube")) > 54):
        result['status'] = 'error: cube string is too large'
        
    #has to be six colors
    elif len(set(parms.get("cube"))) < 6:

        result['status'] = (f"error: There are only {cub_len} colors. There should be 6.\n The colors are {unique}")
        
    elif len(set(parms.get("cube"))) > 6:
        result['status'] = (f"error: There are {cub_len} colors. There should be 6.\n The colors are {unique}")
        
    elif col_flag == 1:
            result['status'] = 'error: one of the colors is more or less than 9 units'
        
    else:
        result['status'] = 'ok'
    return result