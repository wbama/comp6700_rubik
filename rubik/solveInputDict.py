from rubik.solve import _solve
from rubik.solveCheckInput import solveCheck


inputDict = {}
inputDict['cube'] = 'yyobbbbbbyrrrrrrrrggrggggggyyboooooobyybyyoogwwwwwwwww'
inputDict['rotate'] = 'Ff'
inputDict['op'] = 'solve' 

print(_solve(inputDict))
#print(solveCheck(inputDict))


var1 = 'gbrgbrgbbbyybyoyoyogryggobbwwowwywwygrboorwwwryrrrgoog'
var2 = 'gbrgbrgbbbyybyoyoyogryggobbwwowwywwygrboorwwwryrrrgoog'

print(var1 == var2)

