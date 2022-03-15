
from rubik.solve import _solve
from rubik.solveDaisy import solveDaisy
from rubik.solveRotations import createCubeListFromInputParms, rotateCubeToRight, rotateCubeDown, rotateIntoWhiteCross_y_0, rotateIntoWhiteCross_y_1
from rubik.solveWhiteCross import solveWhiteCross
from rubik.solveRotations import createYellowAndWhiteSides

# inputDict['cube'] = "gwwboboyboygwbyyyrygwrrgwowggyogrowbrwrrygoogyorrwbbbb"

inputDict = {}
inputDict['cube'] = "0O0pOoo00p0PZoOPooZOZPZPPpOpoOZ000ppo0oOpPPpZOZZZPPpoO"
inputDict['op'] = 'solve' 
inputDict['rotate'] = ''
lst_cube = (createCubeListFromInputParms(inputDict))
print(lst_cube)

# var_y = createYellowAndWhiteSides(inputDict)[0]
# var_w = createYellowAndWhiteSides(inputDict)[1]   
#
# print(f"var yellow is: {var_y}")
# print(f"var white is: {var_w}")
# # lst_rotate = []
# lst_cube = solveDaisy(inputDict)[0]
# rotations = solveDaisy(inputDict)[1]
#
# print(f"lst cube {lst_cube}")
# print(f"rotations {rotations}")
#
# print(f"WC {solveWhiteCross(inputDict)}")

print(_solve(inputDict))
#
# lst_cube = createCubeListFromInputParms(parms)

#print(solveWhiteCross(inputDict))

# print(_solve(inputDict))
