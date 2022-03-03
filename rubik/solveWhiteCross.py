from rubik.solveRotations import createCubeListFromInputParms
from rubik.solveRotations import rotate_cube_to_right
from rubik.solveRotations import flip_cube_top_side


def solveWhiteCross(parms):
    
    #rotate the cube so that the front center is yellow for the daisy
    
    print(createCubeListFromInputParms(parms))
    
    if createCubeListFromInputParms(parms)[0][4] == 'o':
        print(createCubeListFromInputParms(parms))
    
    #check right side if yellow
    elif createCubeListFromInputParms(parms)[1][4] == 'o':
        lst_cube = rotate_cube_to_right(createCubeListFromInputParms(parms))
        print(lst_cube)
        
    #check back side if yellow
    elif createCubeListFromInputParms(parms)[2][4] == 'o':
        lst_cube = rotate_cube_to_right(createCubeListFromInputParms(parms))
        lst_cube = rotate_cube_to_right(lst_cube)
        print(lst_cube)
        
    #check left side if yellow
    elif createCubeListFromInputParms(parms)[3][4] == 'o':
        lst_cube = rotate_cube_to_right(createCubeListFromInputParms(parms))
        lst_cube = rotate_cube_to_right(lst_cube)
        lst_cube = rotate_cube_to_right(lst_cube)
        print(lst_cube)
        
    #check top side if yellow
    elif createCubeListFromInputParms(parms)[4][4] == 'o':
        lst_cube = flip_cube_top_side(createCubeListFromInputParms(parms))
        print(lst_cube)
        
    #check bottom side if yellow
    elif createCubeListFromInputParms(parms)[5][4] == 'o':
        lst_cube = flip_cube_top_side(createCubeListFromInputParms(parms))
        lst_cube = flip_cube_top_side(lst_cube)
        lst_cube = flip_cube_top_side(lst_cube)
        print(lst_cube)
                  
    # result = {}
    # result['cube'] = parm_string
    # result['status'] = 'ok'  
    
    # return result 
