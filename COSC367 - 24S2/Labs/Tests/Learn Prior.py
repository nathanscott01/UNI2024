import unittest
import io
from contextlib import redirect_stdout
from learn import learn_prior

# Expected Outputs
expected1 = """Prior probability of spam is 0.25500."""

expected2 = """Prior probability of not spam is 0.74500."""

expected3 = """0.25743"""

expected4 = """0.25980"""

expected5 = """0.27727"""

expected6 = """0.37750"""

expected7 = """0.47773"""


class MyTestCase(unittest.TestCase):
    def test_learn_prior_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            prior = learn_prior("spam-labelled.csv")
            print("Prior probability of spam is {:.5f}.".format(prior))
        output = f.getvalue().strip()
        self.assertEqual(expected1, output)

    def test_learn_prior_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            prior = learn_prior("spam-labelled.csv")
            print("Prior probability of not spam is {:.5f}.".format(1 - prior))
        output = f.getvalue().strip()
        self.assertEqual(expected2, output)

    def test_learn_prior_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            prior = learn_prior("spam-labelled.csv", pseudo_count=1)
            print(format(prior, ".5f"))
        output = f.getvalue().strip()
        self.assertEqual(expected3, output)

    def test_learn_prior_4(self):
        f = io.StringIO()
        with redirect_stdout(f):
            prior = learn_prior("spam-labelled.csv", pseudo_count=2)
            print(format(prior, ".5f"))
        output = f.getvalue().strip()
        self.assertEqual(expected4, output)

    def test_learn_prior_5(self):
        f = io.StringIO()
        with redirect_stdout(f):
            prior = learn_prior("spam-labelled.csv", pseudo_count=10)
            print(format(prior, ".5f"))
        output = f.getvalue().strip()
        self.assertEqual(expected5, output)

    def test_learn_prior_6(self):
        f = io.StringIO()
        with redirect_stdout(f):
            prior = learn_prior("spam-labelled.csv", pseudo_count=100)
            print(format(prior, ".5f"))
        output = f.getvalue().strip()
        self.assertEqual(expected6, output)

    def test_learn_prior_7(self):
        f = io.StringIO()
        with redirect_stdout(f):
            prior = learn_prior("spam-labelled.csv", pseudo_count=1000)
            print(format(prior, ".5f"))
        output = f.getvalue().strip()
        self.assertEqual(expected7, output)


if __name__ == '__main__':
    unittest.main()
