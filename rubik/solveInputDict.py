
from rubik.solve import _solve
from rubik.solveDaisy import solveDaisy
from rubik.solveRotations import createCubeListFromInputParms
from rubik.solveWhiteCross import solveWhiteCross


inputDict = {}
inputDict['cube'] = "boygygrrbrwywbyyowgoorwobrogywwgyyrwwbobrboygggrwogbbr"
inputDict['op'] = 'solve' 
#inputDict['rotate'] = 'F'

lst_cube = createCubeListFromInputParms(inputDict)
print(lst_cube)

# lst_cube = solveDaisy(inputDict)[0]
# rotations = solveDaisy(inputDict)[1]
# print(f"lst cube {lst_cube}")
# print(f"rotations {rotations}")

# print(_solve(inputDict))