from rubik.solve import _solve

inputDict = {}
inputDict['cube'] = 'oyoobyryyyggryobbgygwygworrrwbowbgwyborgorwbgbgobrrwww'
inputDict['rotate'] = 'f'   
inputDict['op'] = 'solve' 

print(_solve(inputDict))

