import unittest
import io
from contextlib import redirect_stdout
from learn import learn_likelihood

# Expected Outputs
expected1 = """12
[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]"""

expected2 = """P(X1=True | Spam=False) = 0.35570
P(X1=False| Spam=False) = 0.64430
P(X1=True | Spam=True ) = 0.66667
P(X1=False| Spam=True ) = 0.33333"""

expected3 = """With Laplacian smoothing:
P(X1=True | Spam=False) = 0.35762
P(X1=False| Spam=False) = 0.64238
P(X1=True | Spam=True ) = 0.66038
P(X1=False| Spam=True ) = 0.33962"""


class MyTestCase(unittest.TestCase):
    def test_learn_likelihood_1(self):
        f = io.StringIO()
        with redirect_stdout(f):
            likelihood = learn_likelihood("spam-labelled.csv")
            print(len(likelihood))
            print([len(item) for item in likelihood])
        output = f.getvalue().strip()
        self.assertEqual(expected1, output)

    def test_learn_likelihood_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            likelihood = learn_likelihood("spam-labelled.csv")

            print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
            print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
            print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
            print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))

        output = f.getvalue().strip()
        self.assertEqual(expected2, output)

    def test_learn_likelihood_3(self):
        f = io.StringIO()
        with redirect_stdout(f):
            likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)

            print("With Laplacian smoothing:")
            print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
            print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
            print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
            print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))

        output = f.getvalue().strip()
        self.assertEqual(expected3, output)


if __name__ == '__main__':
    unittest.main()
