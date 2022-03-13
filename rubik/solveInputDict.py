
from rubik.solve import _solve
from rubik.solveDaisy import solveDaisy
from rubik.solveRotations import createCubeListFromInputParms, rotateCubeToRight, rotateCubeDown, rotateIntoWhiteCross_y_0
from rubik.solveWhiteCross import solveWhiteCross


inputDict = {}
inputDict['cube'] = "byybyoyrwryywgggwrgrrrwbgrwywryboogobwogogwogbboorbbyw"
inputDict['op'] = 'solve' 
#inputDict['rotate'] = 'F'

lst_rotate = []
lst_cube = solveDaisy(inputDict)[0]
rotations = solveDaisy(inputDict)[1]
lst_cube = rotateIntoWhiteCross_y_0(lst_cube, rotations)

print(f"lst cube {lst_cube}")
# print(f"rotations {rotations}")

# print(_solve(inputDict)

print(solveWhiteCross(inputDict))
