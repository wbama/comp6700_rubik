from rubik.solveRotations import rotateCubeToLeft
from rubik.solveRotations import rotateCubeClock
from rubik.solveRotations import rotateIntoWhiteCross_y_0, createCubeListFromInputParms
from rubik.solveDaisy import solveDaisy


def solveWhiteCross(parms):
    
       
    # have the daisy now. match up colors and rotate sides down for white cross
    if createCubeListFromInputParms(parms)[0][4] == 'y': 
        lst_cube_rotations = (rotateIntoWhiteCross_y_0(solveDaisy(parms)[0], solveDaisy(parms)[1]))   

    
    return lst_cube_rotations 
