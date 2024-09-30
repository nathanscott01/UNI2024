import unittest
import io
from contextlib import redirect_stdout
from prosterior import *

# Expected Outputs
expected1 = """P(C=False|observation) is approximately 0.00248
P(C=True |observation) is approximately 0.99752"""

expected2 = """P(C=False|observation) is approximately 0.29845
P(C=True |observation) is approximately 0.70155"""

expected3 = """P(C=False|observation) is approximately 0.99454
P(C=True |observation) is approximately 0.00546"""

expected4 = """P(C=False|observation) is approximately 0.99987
P(C=True |observation) is approximately 0.00013"""


class MyTestCase(unittest.TestCase):
    def test_prosterior_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            prior = 0.05
            likelihood = ((0.001, 0.3), (0.05, 0.9), (0.7, 0.99))

            observation = (True, True, True)

            class_posterior_true = posterior(prior, likelihood, observation)
            print("P(C=False|observation) is approximately {:.5f}"
                  .format(1 - class_posterior_true))
            print("P(C=True |observation) is approximately {:.5f}"
                  .format(class_posterior_true))

        output = f.getvalue().strip()
        self.assertEqual(expected1, output)

    def test_prosterior_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            prior = 0.05
            likelihood = ((0.001, 0.3), (0.05, 0.9), (0.7, 0.99))

            observation = (True, False, True)

            class_posterior_true = posterior(prior, likelihood, observation)
            print("P(C=False|observation) is approximately {:.5f}"
                  .format(1 - class_posterior_true))
            print("P(C=True |observation) is approximately {:.5f}"
                  .format(class_posterior_true))

        output = f.getvalue().strip()
        self.assertEqual(expected2, output)

    def test_prosterior_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            prior = 0.05
            likelihood = ((0.001, 0.3), (0.05, 0.9), (0.7, 0.99))

            observation = (False, False, True)

            class_posterior_true = posterior(prior, likelihood, observation)
            print("P(C=False|observation) is approximately {:.5f}"
                  .format(1 - class_posterior_true))
            print("P(C=True |observation) is approximately {:.5f}"
                  .format(class_posterior_true))

        output = f.getvalue().strip()
        self.assertEqual(expected3, output)

    def test_prosterior_4(self):
        f = io.StringIO()
        with redirect_stdout(f):
            prior = 0.05
            likelihood = ((0.001, 0.3), (0.05, 0.9), (0.7, 0.99))

            observation = (False, False, False)

            class_posterior_true = posterior(prior, likelihood, observation)
            print("P(C=False|observation) is approximately {:.5f}"
                  .format(1 - class_posterior_true))
            print("P(C=True |observation) is approximately {:.5f}"
                  .format(class_posterior_true))

        output = f.getvalue().strip()
        self.assertEqual(expected4, output)


if __name__ == '__main__':
    unittest.main()
