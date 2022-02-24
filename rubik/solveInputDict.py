from rubik.solve import _solve

inputDict = {}
inputDict['cube'] = 'bywrbyroroyygwgbwwrbbogrrryybwwygoobowgyroorgwwyboggbg'
inputDict['rotate'] = ' '   
inputDict['op'] = 'solve' 

print(_solve(inputDict))

