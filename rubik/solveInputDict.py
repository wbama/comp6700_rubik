
from rubik.solve import _solve
from rubik.solveDaisy import solveDaisy
from rubik.solveRotations import rotateIntoWhiteCross_y_0
from rubik.solveWhiteCross import solveWhiteCross


inputDict = {}
inputDict['cube'] = "grygoogyrorgwwwbrbwbrgrbwbrrywwyowroyyoobbrybygyggwboo"
inputDict['op'] = 'solve' 
#inputDict['rotate'] = 'F'


lst_cube = solveDaisy(inputDict)[0]
rotations = solveDaisy(inputDict)[1]
print(f"lst cube {lst_cube}")
print(f"rotations {rotations}")

# print(_solve(inputDict))