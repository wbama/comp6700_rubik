from rubik.solveRotations import createCubeListFromInputParms
from rubik.solveRotations import rotateCubeToLeft
from rubik.solveRotations import rotateCubeToRight
from rubik.solveRotations import rotateCubeDown
from rubik.solveRotations import rotateCubeUp
from rubik.solveRotations import createStringFromCube
from rubik.solveRotations import rotateSideCounterClock
from rubik.solveRotations import rotateSideClock
from rubik.solveRotations import putWhiteLeafPosition0_5
from rubik.solveWhiteCross import solveWhiteCross
from rubik.solve import _solve


inputDict = {}
inputDict['cube'] = "ygrgybbbbwroogowyygyrwwwbgybygbbooyrwbwrowrrgyroorggwo"
inputDict['op'] = 'solve' 
#inputDict['rotate'] = 'F' 


print(_solve(inputDict))
#print(solveWhiteCross(inputDict))



