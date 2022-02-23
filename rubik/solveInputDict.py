import rubik.cube as rubik
from rubik.solve import _solve


inputDict = {}
inputDict['cube'] = 'rrbbbbgggryyyyoroyogryggobbwwwwwwwwwgrboorbbyoyyrrgoog'
inputDict['rotate'] = 'F'
inputDict['op'] = 'solve' 

print(inputDict)

print(_solve(inputDict))