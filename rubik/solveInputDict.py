from rubik.solve import _solve
from rubik.solveCheckInput import solveCheck


inputDict = {}
inputDict['cube'] = 'rbbgbobbgrgwyrywyobggrggywgoryyowowwyoobyrgwyrorrwbwob'
inputDict['rotate'] = 'f'
inputDict['op'] = 'solve' 

print(_solve(inputDict))

