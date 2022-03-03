from rubik.solveRotations import createCubeListFromInputParms
from rubik.solveRotations import rotate_cube_to_right
from rubik.solveRotations import flip_cube_top_side


def solveWhiteCross(parms):
    
    #rotate the cube so that the front center is yellow for the daisy   
    
    if createCubeListFromInputParms(parms)[0][4] == 'y':
        print(createCubeListFromInputParms(parms))
    
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
        
    str1 = "".join(lst_cube[0])
    str2 = "".join(lst_cube[1])
    str3 = "".join(lst_cube[2])
    str4 = "".join(lst_cube[3])
    str5 = "".join(lst_cube[4])
    str6 = "".join(lst_cube[5])                       
         
    str_cube = str1+str2+str3+str4+str5+str6
                    
    result = {}
    result['cube'] = str_cube
    result['status'] = 'ok'                   

    
    return result 
