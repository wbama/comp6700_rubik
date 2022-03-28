"""
    Created on 03/05/2022
    @author: Waldo du Toit
    program for solving the white cross
    03/17 - Refactoring. Replace i in range with _
    
"""


from rubik.solveRotations import rotateIntoWhiteCross_y_4
from rubik.solveDaisy import solveDaisy

def solveWhiteCross(parms):    

    lst_cube_from_daisy = ((rotateIntoWhiteCross_y_4(solveDaisy(parms)[0], solveDaisy(parms)[1])))[0]
    rotation_from_daisy = ((rotateIntoWhiteCross_y_4(solveDaisy(parms)[0], solveDaisy(parms)[1])))[1]        
    whiteCrossCube = (rotateIntoWhiteCross_y_4(lst_cube_from_daisy, rotation_from_daisy ))             
    for _ in range(20):
        whiteCrossCube = (rotateIntoWhiteCross_y_4(whiteCrossCube[0], whiteCrossCube[1])) 
            
    return whiteCrossCube 
