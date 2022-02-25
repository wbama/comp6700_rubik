from rubik.solve import _solve
from rubik.solveCheckInput import solveCheck


inputDict = {}
inputDict['cube'] = 'rrbbbbgggryyyyoroyogryggobbwwwwwwwwwgrboorbbyoyyrrgoog'
inputDict['rotate'] = 'F'
inputDict['op'] = 'solve' 

print(_solve(inputDict))
#print(solveCheck(inputDict))


var1 = 'rrbbbbgggryyyyoroyogryggobbwwwwwwwwwgrboorbbyoyyrrgoog'
var2 = 'gbrgbrgbbbyybyoyoyogryggobbwwowwywwygrboorwwwryrrrgoog'

print(var1 == var2)

