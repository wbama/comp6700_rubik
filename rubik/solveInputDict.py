from rubik.solve import _solve
from rubik.solveCheckInput import solveCheck


inputDict = {}
inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
inputDict['rotate'] = "fffUUdduu" 
inputDict['op'] = 'solve' 

#print(_solve(inputDict))
print(solveCheck(inputDict))


var1 = 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy'
var2 = 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy'

print(var1 == var2)

