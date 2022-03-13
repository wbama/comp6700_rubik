from rubik.solveRotations import rotateCubeToLeft
from rubik.solveRotations import rotateCubeClock
from rubik.solveRotations import rotateIntoWhiteCross_y_0, createCubeListFromInputParms
from rubik.solveDaisy import solveDaisy


def solveWhiteCross(parms):
    
       
    # have the daisy now. match up colors and rotate sides down for white cross
    if createCubeListFromInputParms(parms)[0][4] == 'y': 
        lst_cube_from_daisy = ((rotateIntoWhiteCross_y_0(solveDaisy(parms)[0], solveDaisy(parms)[1])))[0]
        rotation_from_daisy = ((rotateIntoWhiteCross_y_0(solveDaisy(parms)[0], solveDaisy(parms)[1])))[1]
        
        whiteCrossCube = (rotateIntoWhiteCross_y_0(lst_cube_from_daisy, rotation_from_daisy ))             
        while not ("LL" in whiteCrossCube[1] and "RR" in whiteCrossCube[1] and "DD" in whiteCrossCube[1] and "UU" in whiteCrossCube[1]):
            whiteCrossCube = (rotateIntoWhiteCross_y_0(whiteCrossCube[0], whiteCrossCube[1])) 
               
    
    return whiteCrossCube 
