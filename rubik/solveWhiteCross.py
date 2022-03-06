from rubik.solveRotations import createCubeListFromInputParms
from rubik.solveRotations import rotateCubeToLeft
from rubik.solveRotations import rotateCubeToRight
from rubik.solveRotations import rotateCubeToTop
from rubik.solveRotations import rotateCubeToBottom
from rubik.solveRotations import createStringFromCube
from rubik.solveRotations import rotateSideCounterClock
from rubik.solveRotations import rotateSideClock
from rubik.solveRotations import putWhiteLeafPosition0_5
from rubik.solveInputDict import lst_cube




def solveWhiteCross(parms):
    
    #rotate the cube so that the front center is yellow for the daisy   
    
    if createCubeListFromInputParms(parms)[0][4] == 'y':
        # result = {}
        # result['cube'] = createStringFromCube(parms)
        # result['status'] = 'ok' 
        lst_cube = (createCubeListFromInputParms(parms))
    
    #check right side if yellow
    elif createCubeListFromInputParms(parms)[1][4] == 'y':
        lst_cube = rotateCubeToLeft(createCubeListFromInputParms(parms))
        
    #check back side if yellow
    elif createCubeListFromInputParms(parms)[2][4] == 'y':
        lst_cube = rotateCubeToLeft(createCubeListFromInputParms(parms))
        lst_cube = rotateCubeToLeft(lst_cube)
        
    #check left side if yellow
    elif createCubeListFromInputParms(parms)[3][4] == 'y':
        lst_cube = rotateCubeToLeft(createCubeListFromInputParms(parms))
        lst_cube = rotateCubeToLeft(lst_cube)
        lst_cube = rotateCubeToLeft(lst_cube)
        
    #check top side if yellow
    elif createCubeListFromInputParms(parms)[4][4] == 'y':
        lst_cube = rotateCubeToTop(createCubeListFromInputParms(parms))
        
    #check bottom side if yellow
    elif createCubeListFromInputParms(parms)[5][4] == 'y':
        lst_cube = rotateCubeToTop(createCubeListFromInputParms(parms))
        lst_cube = rotateCubeToTop(lst_cube)
        lst_cube = rotateCubeToTop(lst_cube)    
        
    #now we have the yellow in front.
    #find white leaves   
    if lst_cube[0][5] == 'w':
        lst_cube = lst_cube
    else:
        #inside cells
        lst_cube = putWhiteLeafPosition0_5(lst_cube)

            
    #now rotate the whole cube, and do the yellow[0][5] again
   
    print(lst_cube)
    print(lst_cube[0][5])
    result = {}
    result['cube'] = createStringFromCube(lst_cube)
    result['status'] = 'ok'                   

    
    return result 
