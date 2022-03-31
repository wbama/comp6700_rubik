"""
    Created on 03/05/2022
    @author: Waldo du Toit
    code to feed in cube strings
    
"""
from rubik.solve import _solve

from rubik.solveRotations import createCubeListFromInputParms, rotateCubeToRight, rotateCubeDown, rotateIntoWhiteCross_y_0, rotateIntoWhiteCross_y_1
from rubik.solveWhiteCross import solveWhiteCross
from rubik.solveRotations import createYellowAndWhiteVariables, createStringFromCube
from rubik.solveLowerLayer import solveLowerLayer

# inputDict['cube'] = "ooogboyyrgrbbrgwwroyrygbgbgygywowyrrbowoygbwwgbbywrorw"
#inputDict['cube'] = 'xy54Ra5ax4RxRxxa545445yxayy54RR4RaxxRayya5aayRxyy5445R'

inputDict = {}
inputDict['cube'] = 'gggggggggyowyowyowbbbbbbbbbyrwyrwyrwoooyyyrrrooowwwrrr'
#inputDict['cube'] = 'rybbbrggryrybyoyyybgryggobbwwwwwwwwwgrrooybgooogrrboog'
inputDict['op'] = 'solve' 
inputDict['rotate'] = ''



# lst_cube = (createCubeListFromInputParms(inputDict))
# print(lst_cube)
#
# lst_cube = rotateCubeDown(lst_cube)
# print(lst_cube)
# print(createStringFromCube(lst_cube))
#
# var_y = createYellowAndWhiteSides(inputDict)[0]
# var_w = createYellowAndWhiteSides(inputDict)[1]   
#
#  print(f"var yellow is: {var_y}")
#  print(f"var white is: {var_w}")
#  lst_rotate = []
# lst_cube = solveDaisy(inputDict)[0]
# rotations = solveDaisy(inputDict)[1]

# print(f"lst cube {lst_cube}")
# print(f"rotations {rotations}")
# #
#print(f"WC {solveWhiteCross(inputDict)}")
#
print(_solve(inputDict))
#
# lst_cube = createCubeListFromInputParms(parms)

#solveLowerLayer(inputDict)


#print(_solve(inputDict))
