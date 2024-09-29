import unittest
import io
from contextlib import redirect_stdout
from query import *

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
expected1_1 = """P(A=true) = 0.20000
P(A=false) = 0.80000"""

expected2_1 = """P(B=true|A=false) = 0.70000
P(B=false|A=false) = 0.30000"""

expected2_2 = """P(B=true) = 0.71000
P(B=false) = 0.29000"""

expected3_1 = """Probability of a burglary when both
John and Mary have called: 0.284"""

expected3_2 = """Probability of John calling if
Mary has called: 0.17758"""


class MyTestCase(unittest.TestCase):
    def test_joint1_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            answer = query(network_1, 'A', {})
            print("P(A=true) = {:.5f}".format(answer[True]))
            print("P(A=false) = {:.5f}".format(answer[False]))
        output = f.getvalue().strip()
        self.assertEqual(expected1_1, output)

    def test_joint2_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            answer = query(network_2, 'B', {'A': False})
            print("P(B=true|A=false) = {:.5f}".format(answer[True]))
            print("P(B=false|A=false) = {:.5f}".format(answer[False]))
        output = f.getvalue().strip()
        self.assertEqual(expected2_1, output)

    def test_joint2_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            answer = query(network_2, 'B', {})
            print("P(B=true) = {:.5f}".format(answer[True]))
            print("P(B=false) = {:.5f}".format(answer[False]))
        output = f.getvalue().strip()
        self.assertEqual(expected2_2, output)

    def test_joint3_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            answer = query(network_3, 'Burglary', {'John': True, 'Mary': True})
            print("Probability of a burglary when both\n"
                  "John and Mary have called: {:.3f}".format(answer[True]))
        output = f.getvalue().strip()
        self.assertEqual(expected3_1, output)

    def test_joint3_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            answer = query(network_3, 'John', {'Mary': True})
            print("Probability of John calling if\n"
                  "Mary has called: {:.5f}".format(answer[True]))
        output = f.getvalue().strip()
        self.assertEqual(expected3_2, output)


if __name__ == '__main__':
    unittest.main()
