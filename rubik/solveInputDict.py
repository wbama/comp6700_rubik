from rubik.solve import _solve
from rubik import solveCheckInput
from rubik.solveCheckInput import solveCheck


inputDict = {}
inputDict['cube'] = "rbbgbobbgrgw$r$w$obggrgg$wgor$$owoww$oob$rgw$rorrwbwob"
inputDict['rotate'] = 'FLFFBUUdLfDrFLdRRdLLdRRu'
inputDict['op'] = 'solve' 

print(_solve(inputDict))



