def rotate_cube_to_left(cube):
        #rotate cube to left
        first_side = cube.pop(0)
        cube.insert(3, first_side)        
        # rotate the top
        orig_side = cube.pop(4)
        cube.insert(4, turn_type1(orig_side))        
        #now rotate the bottom
        orig_side = cube.pop(5) 
        cube.insert(5, turn_type2(orig_side))
        return cube
    
