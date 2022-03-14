from rubik.solveRotations import createCubeListFromInputParms

inputDict = {}
inputDict['cube'] = "rbgryyygboyobbwrwygyrowobgogwgbggbrbyrwrrowwyrywbogwoo"
inputDict['op'] = 'solve' 
lst_cube = createCubeListFromInputParms(inputDict)  
print(lst_cube)


s = set(lst_cube[0])
print(len(s))


