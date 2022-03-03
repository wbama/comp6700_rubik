from rubik.solveRotations import createCubeListFromInputParms
from rubik.solveRotations import rotate_cube_to_right
from rubik.solveRotations import flip_cube_top_side
from rubik.solveRotations import createStringFromCube
from rubik.solveRotations import turn_cclock
from rubik.solveRotations import turn_clock


def solveWhiteCross(parms):
    
    #rotate the cube so that the front center is yellow for the daisy   
    
    if createCubeListFromInputParms(parms)[0][4] == 'y':
        # result = {}
        # result['cube'] = createStringFromCube(parms)
        # result['status'] = 'ok' 
        print("yellow front")
    
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
    if lst_cube[0][5] != 'w':
        if lst_cube[4][5] == 'w':
            lst_cube = rotate_cube_to_right(lst_cube)
            cc_rotate_cube = turn_cclock(lst_cube)
            lst_cube = rotate_cube_to_right(cc_rotate_cube)
            lst_cube = rotate_cube_to_right(cc_rotate_cube)
            lst_cube = rotate_cube_to_right(cc_rotate_cube)  
        elif lst_cube[2][1] == 'w': 
            lst_cube = rotate_cube_to_right(lst_cube)
            cc_rotate_cube = turn_cclock(lst_cube)
            cc_rotate_cube = turn_cclock(cc_rotate_cube)
            lst_cube = rotate_cube_to_right(cc_rotate_cube)
            lst_cube = rotate_cube_to_right(cc_rotate_cube)
            lst_cube = rotate_cube_to_right(cc_rotate_cube) 
        elif lst_cube[5][5] == 'w': 
            lst_cube = rotate_cube_to_right(lst_cube)
            cc_rotate_cube = turn_clock(lst_cube)
            lst_cube = rotate_cube_to_right(cc_rotate_cube)
            lst_cube = rotate_cube_to_right(cc_rotate_cube)
            lst_cube = rotate_cube_to_right(cc_rotate_cube) 
        elif lst_cube[1][3] == 'w': 
            lst_cube = rotate_cube_to_right(lst_cube)
            c_rotate_cube = turn_clock(lst_cube)
            lst_cube = rotate_cube_to_right(c_rotate_cube)
            lst_cube = rotate_cube_to_right(lst_cube)
            lst_cube = rotate_cube_to_right(lst_cube) 
            lst_cube = flip_cube_top_side(lst_cube) 
            c_rotate_cube = turn_clock(lst_cube)
            lst_cube = flip_cube_top_side(c_rotate_cube)
            lst_cube = flip_cube_top_side(c_rotate_cube)
            lst_cube = flip_cube_top_side(c_rotate_cube)
        elif lst_cube[2][1] == 'w': 
            lst_cube = rotate_cube_to_right(lst_cube)
            c_rotate_cube = turn_clock(lst_cube)
            lst_cube = rotate_cube_to_right(c_rotate_cube)
            lst_cube = rotate_cube_to_right(lst_cube)
            lst_cube = rotate_cube_to_right(lst_cube) 
            lst_cube = flip_cube_top_side(lst_cube) 
            c_rotate_cube = turn_clock(lst_cube)
            lst_cube = flip_cube_top_side(c_rotate_cube)
            lst_cube = flip_cube_top_side(c_rotate_cube)
            lst_cube = flip_cube_top_side(c_rotate_cube)
   
    print(lst_cube)
    print(lst_cube[0][5])
    result = {}
    result['cube'] = createStringFromCube(lst_cube)
    result['status'] = 'ok'                   

    
    return result 
