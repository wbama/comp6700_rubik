import unittest
import rubik.cube as cube


class CubeTest(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

#Analysis: Cube class
#        methods: instantiate the cube
#                 instantiate an empty cube
#                 later on load - loads a string
#                then get method
#Analysis: Cube.__init__
#            inputs: no input parameter
#             output: 
#                   side effects: none at the moment
#                   nominal: emptry instance of cube
#                    abnormal: NA for cube
    def test_init_010_ShouldCreateEmptyCube(self):
        myCube = cube.Cube()
        self.assertIsInstance(myCube, cube.Cube)


