from rubik.solveRotations import createCubeStringFromInputParms


def solveWhiteCross(parms):
    
    #rotate the cube so that the front center is yellow for the daisy
    
    parm_string = parms.get("cube")  #get the string
    
    lst_cube = ([x for x in parms.get("cube")])
    lst_in1, lst_in2, lst_in3, lst_in4, lst_in5, lst_in6 = ([] for i in range(6)) 
    
    for i in range (1,7):
        for j in range(1,10):
            exec(f"lst_in{i}.append(lst_cube.pop(0))")  
            
    for i in range(1,7):
        exec(f'lst_cube.append(lst_in{i})')  
                  
    result = {}
    result['cube'] = parm_string
    result['status'] = 'ok'  
    
    return result 
