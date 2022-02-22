from unittest import TestCase
import rubik.check as check 

class CheckTest(TestCase):
        
    def test_check_010_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check', 'cube': 'gwrbbbwwyyybrrygogyowogyygorrogowbggbboyybwobrrrrwgwwo'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
    def _check(parms):
        parm_string = parms.get("cube")  #get the string
        
