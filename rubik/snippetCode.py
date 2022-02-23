
from rubik.solve import turn_clock
from rubik.solve import turn_cclock
from rubik.solve import turn_type1
from rubik.solve import turn_type2
from rubik.solve import turn_type3
import rubik.cube as rubik
from rubik.solve import _solve


inputDict = {}
inputDict['cube'] = 'rrbbbbgggryyyyoroyogryggobbwwwwwwwwwgrboorbbyoyyrrgoog'
inputDict['rotate'] = 'F'
inputDict['op'] = 'solve' 

print(inputDict)

print(_solve(inputDict))

