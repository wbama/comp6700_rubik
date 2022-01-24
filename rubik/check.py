import rubik.cube as rubik

def _check(parms):
    result={}
    encodedCube = parms.get('cube',None)       
    if(encodedCube == None):
        result['status'] = 'error: no cube found'
    else:
        result['status'] = 'a-ok'
    return result