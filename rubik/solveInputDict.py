from rubik.solve import _solve
from rubik.solveCheckInput import solveCheck


inputDict = {}
inputDict['cube'] = 'rrbbbbgggryyyyoroyogryggobbwwwwwwwwwgrboorbbyoyyrrgoog'
inputDict['rotate'] = " "
inputDict['op'] = 'solve' 

print(_solve(inputDict))

