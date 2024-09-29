import unittest
import io
from contextlib import redirect_stdout
from joint_probability import *

# Inputs
network_1 = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2
            }},
}

network_2 = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
        }},

    'B': {
        'Parents': ['A'],
        'CPT': {
            (True,): 0.8,
            (False,): 0.7,
        }},
}

network_3 = {
    'Burglary': {
        'Parents': [],
        'CPT': {
            (): 0.001
        }},

    'Earthquake': {
        'Parents': [],
        'CPT': {
            (): 0.002,
        }},
    'Alarm': {
        'Parents': ['Burglary', 'Earthquake'],
        'CPT': {
            (True, True): 0.95,
            (True, False): 0.94,
            (False, True): 0.29,
            (False, False): 0.001,
        }},

    'John': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.9,
            (False,): 0.05,
        }},

    'Mary': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.7,
            (False,): 0.01,
        }},
}

# Expected Outputs
expected1_1 = """0.20000"""

expected1_2 = """0.80000"""

expected2_1 = """0.63000"""

expected2_2 = """0.27000
0.63000
0.02000
0.08000"""

expected3 = """0.00062811"""


class MyTestCase(unittest.TestCase):
    def test_joint1_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            p = joint_prob(network_1, {'A': True})
            print("{:.5f}".format(p))
        output = f.getvalue().strip()
        self.assertEqual(expected1_1, output)

    def test_joint1_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            p = joint_prob(network_1, {'A': False})
            print("{:.5f}".format(p))
        output = f.getvalue().strip()
        self.assertEqual(expected1_2, output)

    def test_joint2_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            p = joint_prob(network_2, {'A': False, 'B': True})
            print("{:.5f}".format(p))
        output = f.getvalue().strip()
        self.assertEqual(expected2_1, output)

    def test_joint2_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            p = joint_prob(network_2, {'A': False, 'B': False})
            print("{:.5f}".format(p))
            p = joint_prob(network_2, {'A': False, 'B': True})
            print("{:.5f}".format(p))
            p = joint_prob(network_2, {'A': True, 'B': False})
            print("{:.5f}".format(p))
            p = joint_prob(network_2, {'A': True, 'B': True})
            print("{:.5f}".format(p))
        output = f.getvalue().strip()
        self.assertEqual(expected2_2, output)

    def test_joint3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            p = joint_prob(network_3, {'John': True, 'Mary': True,
                                     'Alarm': True, 'Burglary': False,
                                     'Earthquake': False})
            print("{:.8f}".format(p))
        output = f.getvalue().strip()
        self.assertEqual(expected3, output)


if __name__ == '__main__':
    unittest.main()
