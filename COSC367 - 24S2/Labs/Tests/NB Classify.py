import unittest
import io
from contextlib import redirect_stdout
from learn import *

# Expected Outputs
expected1 = """Prediction: Not Spam, Certainty: 0.99351
Prediction: Spam, Certainty: 0.57441
Prediction: Spam, Certainty: 0.59337
Prediction: Spam, Certainty: 0.83465
Prediction: Not Spam, Certainty: 0.99140"""

expected2 = """Prediction: Not Spam, Certainty: 0.99213
Prediction: Spam, Certainty: 0.57759
Prediction: Spam, Certainty: 0.59073
Prediction: Spam, Certainty: 0.83059
Prediction: Not Spam, Certainty: 0.98989"""


class MyTestCase(unittest.TestCase):
    def test_nb_classify_1(self):
        f = io.StringIO()
        with redirect_stdout(f):

            prior = learn_prior("spam-labelled.csv")
            likelihood = learn_likelihood("spam-labelled.csv")

            input_vectors = [
                (1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0),
                (0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1),
                (1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1),
                (1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1),
                (0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0),
            ]

            predictions = [nb_classify(prior, likelihood, vector)
                           for vector in input_vectors]

            for label, certainty in predictions:
                print("Prediction: {}, Certainty: {:.5f}"
                      .format(label, certainty))

        output = f.getvalue().strip()
        self.assertEqual(expected1, output)

    def test_nb_classify_2(self):
        f = io.StringIO()
        with redirect_stdout(f):
            prior = learn_prior("spam-labelled.csv", pseudo_count=1)
            likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)

            input_vectors = [
                (1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0),
                (0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1),
                (1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1),
                (1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1),
                (0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0),
            ]

            predictions = [nb_classify(prior, likelihood, vector)
                           for vector in input_vectors]

            for label, certainty in predictions:
                print("Prediction: {}, Certainty: {:.5f}"
                      .format(label, certainty))

        output = f.getvalue().strip()
        self.assertEqual(expected2, output)


if __name__ == '__main__':
    unittest.main()
