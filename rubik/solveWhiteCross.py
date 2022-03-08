from rubik.solveRotations import rotateCubeToLeft
from rubik.solveRotations import rotateCubeClock
from rubik.solveRotations import rotateIntoWhiteCross_y_0
from rubik.solveDaisy import solveDaisy


def solveWhiteCross(parms):
    
       
    # have the daisy now. match up colors and rotate sides down for white cross
    
    lst_cube = rotateIntoWhiteCross_y_0(solveDaisy(parms))    

    
    return lst_cube 
