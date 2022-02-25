from rubik.solve import _solve

inputDict = {}
inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
inputDict['rotate'] = 'Ff' 
inputDict['op'] = 'solve' 

print(_solve(inputDict))

var1 = 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy'
var2 = 'gggggggggwrrwrrwrrbbbbbbbbbooyooyooywwwwwwooorrryyyyyy'

print(var1 == var2)

