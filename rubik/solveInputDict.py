
from rubik.solve import _solve
from rubik.solveDaisy import solveDaisy
from rubik.solveRotations import createCubeListFromInputParms, rotateCubeToRight, rotateCubeDown, rotateIntoWhiteCross_y_0, rotateIntoWhiteCross_y_1
from rubik.solveWhiteCross import solveWhiteCross


inputDict = {}
inputDict['cube'] = "ybbbbwggboywrrbygwrgoygyroggobrorryowwbwygowwyrrowoybg"
inputDict['op'] = 'solve' 
# inputDict['rotate'] = 'F'
print(createCubeListFromInputParms(inputDict))

lst_rotate = []
lst_cube = solveDaisy(inputDict)[0]
rotations = solveDaisy(inputDict)[1]

# print(f"lst cube {lst_cube}")
# print(f"rotations {rotations}")
#
print(_solve(inputDict))

#print(solveWhiteCross(inputDict))

# print(_solve(inputDict))
