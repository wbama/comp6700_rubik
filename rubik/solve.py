import rubik.cube as rubik

def _solve(parms):
    result = {}
    encodedCube = parms.get('cube',None)       #get "cube" parameter if present
    result['solution'] = 'FfRrBbLlUuDd'        #example rotations
    result['status'] = 'ok'                     
    return result

# validate my parms, if invalid, need to return status with error
# if everything is valid, load parms into cube modell
# then rotate the cube model in the desired direction
# serialize the cube model in encoded cube into a string
# return the string result + status of "ok"


# but have to write the test code first


