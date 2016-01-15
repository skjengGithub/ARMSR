import unittest
import auditory_robot

class MyTestCase(unittest.TestCase):
    def test_name(self):
        tom = auditory_robot.AuditoryRobot('TOM')
        self.assertEqual(tom.name, 'TOM')

    def runTest(self):
        self.test_name()


MyTestCase().runTest()