from rubik.solve import _solve
from rubik import solveCheckInput
from rubik.solveCheckInput import solveCheck


inputDict = {}
inputDict['cube'] = 'rrbbbbgggr????oro?ogr?ggobbwwwwwwwwwgrboorbb?o??rrgoog'
inputDict['rotate'] = 'FLFFBUUdLfDrFLdRRdLLdRRu'
inputDict['op'] = 'solve' 

#print(_solve(inputDict))

print(solveCheck(inputDict))

