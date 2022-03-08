
from rubik.solve import _solve
from rubik.solveDaisy import solveDaisy
from rubik.solveRotations import rotateIntoWhiteCross_y_0
from rubik.solveWhiteCross import solveWhiteCross


inputDict = {}
inputDict['cube'] = "gboyyobgwbbbgoroggrrywwgwoggrryrboowobyybwyoyrrbwgwwyr"
inputDict['op'] = 'solve' 
#inputDict['rotate'] = 'F'

lst_cube = solveDaisy(inputDict)[0]
rotations = solveDaisy(inputDict)[1]
print(lst_cube)
print(rotations)
print(rotateIntoWhiteCross_y_0(lst_cube, rotations))



