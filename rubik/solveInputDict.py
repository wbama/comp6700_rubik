import rubik.cube as rubik
from rubik.solve import _solve
import rubik.solveCheckInput
from rubik.solveCheckInput import solveCheck



inputDict = {}
inputDict['cube'] = 'oybrbrogryrybyoyyybgbygoobgwwwwwwwwwrrrboyggoboggrbrog'
inputDict['rotate'] = 'p'   
inputDict['op'] = 'solve' 

print(_solve(inputDict))

