from rubik.solveRotations import createCubeListFromInputParms
from rubik.solveRotations import rotate_cube_to_right
from rubik.solveRotations import flip_cube_top_side
from rubik.solveRotations import createStringFromCube


def solveWhiteCross(parms):
    
    #rotate the cube so that the front center is yellow for the daisy   
    
    if createCubeListFromInputParms(parms)[0][4] == 'y':
        result = {}
        result['cube'] = createStringFromCube(parms)
        result['status'] = 'ok' 
    
    #check right side if yellow
    elif createCubeListFromInputParms(parms)[1][4] == 'y':
        lst_cube = rotate_cube_to_right(createCubeListFromInputParms(parms))
        
    #check back side if yellow
    elif createCubeListFromInputParms(parms)[2][4] == 'y':
        lst_cube = rotate_cube_to_right(createCubeListFromInputParms(parms))
        lst_cube = rotate_cube_to_right(lst_cube)
        
    #check left side if yellow
    elif createCubeListFromInputParms(parms)[3][4] == 'y':
        lst_cube = rotate_cube_to_right(createCubeListFromInputParms(parms))
        lst_cube = rotate_cube_to_right(lst_cube)
        lst_cube = rotate_cube_to_right(lst_cube)
        
    #check top side if yellow
    elif createCubeListFromInputParms(parms)[4][4] == 'y':
        lst_cube = flip_cube_top_side(createCubeListFromInputParms(parms))
        
    #check bottom side if yellow
    elif createCubeListFromInputParms(parms)[5][4] == 'y':
        lst_cube = flip_cube_top_side(createCubeListFromInputParms(parms))
        lst_cube = flip_cube_top_side(lst_cube)
        lst_cube = flip_cube_top_side(lst_cube)        

    #now we have the yellow in front.
    #find white leaves   
       
    print(lst_cube)        
    lst_cube[1] = 'y'    
    lst_cube[3] = 'y'  
    lst_cube[5] = 'y'    
    lst_cube[7] = 'y'      
    result = {}
    result['cube'] = createStringFromCube(lst_cube)
    result['status'] = 'ok'                   

    
    return result 
