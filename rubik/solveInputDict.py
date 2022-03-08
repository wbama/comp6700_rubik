
from rubik.solve import _solve
from rubik.solveDaisy import solveDaisy
from rubik.solveRotations import rotateIntoWhiteCross_y_0
from rubik.solveWhiteCross import solveWhiteCross


inputDict = {}
inputDict['cube'] = "gboyyobgwbbbgoroggrrywwgwoggrryrboowobyybwyoyrrbwgwwyr"
inputDict['op'] = 'solve' 
#inputDict['rotate'] = 'F'

print(solveDaisy(inputDict))



