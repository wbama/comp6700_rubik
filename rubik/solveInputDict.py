from rubik.solve import _solve

inputDict = {}
inputDict['cube'] = 'oybrbrogryrybyoyyybgbygoobgwwwwwwwwwrrrboyggoboggrbrog'
inputDict['rotate'] = 'f'   
inputDict['op'] = 'solve' 

print(_solve(inputDict))

