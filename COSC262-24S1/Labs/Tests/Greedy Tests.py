import unittest
from greedy import *


buskers_example1 = [
    ('a', 0, 6),
    ('b', 1, 3),
    ('c', 3, 2),
    ('d', 3, 5),
    ('e', 4, 3),
    ('f', 5, 4),
    ('g', 6, 4),
    ('h', 8, 3)]

buskers_example2 = [
    ('Lazaro Lindo', 948, 48),
    ('Otelia Olivar', 415, 37),
    ('Lean Lyall', 111, 45),
    ('Sherlene Schneck', 841, 34),
    ('Jacinta Jara', 53, 36),
    ('Jamaal Jonson', 267, 11),
    ('Ehtel Engram', 24, 2),
    ('Catrina Coletta', 167, 50),
    ('Diann Dimeo', 698, 2),
    ('Glenn Garst', 583, 5),
    ('Ciera Canela', 198, 22),
    ('Youlanda Yepez', 695, 31),
    ('Kandra Keasler', 641, 23),
    ('Hettie Housand', 205, 6),
    ('Brenna Blanca', 324, 22),
    ('Virgil Vides', 770, 34),
    ('Krystina Karcher', 47, 47),
    ('Sindy Simek', 179, 14),
    ('Leanne Lindauer', 132, 49),
    ('Cristie Chesnutt', 12, 30),
    ('Migdalia Manske', 484, 8),
    ('Abram Aquilino', 143, 45),
    ('Minnie Mcclinton', 678, 24),
    ('Hilma Hodgin', 760, 5),
    ('Edythe Estepp', 436, 7),
    ('Zonia Zacharias', 263, 33),
    ('Marylin Mai', 550, 4),
    ('Tana Tonn', 170, 2),
    ('Lawrence Longacre', 554, 11),
    ('Delbert Degarmo', 234, 16),
    ('Margit Mendenhall', 767, 11),
    ('Liz Low', 640, 40),
    ('Nakisha Ned', 525, 26),
    ('Octavia Ojeda', 554, 21),
    ('Gertha Greening', 1, 37),
    ('Jolanda Jakubowski', 532, 26),
    ('Codi Covert', 344, 45),
    ('Cammie Cassidy', 109, 44),
    ('Tilda Tippie', 995, 15),
    ('Sherril Strebel', 986, 42),
    ('Lizzette Lawless', 771, 18),
    ('Leia Lieu', 355, 12),
    ('Julian Joe', 161, 30),
    ('Carolynn Canez', 974, 27),
    ('Magda Mcdowell', 904, 40),
    ('Izola Igoe', 375, 21),
    ('Shakira Sonnenberg', 9, 4),
    ('Ardith Artiaga', 858, 20),
    ('Marry Montag', 708, 6),
    ('Rod Ruggiero', 973, 16)]

items = [
    ("Chocolate cookies", 20, 5),
    ("Potato chips", 15, 3),
    ("Pizza", 14, 2),
    ("Popcorn", 12, 4)]

buskers_expected1 = [('Shakira Sonnenberg', 9, 13),
     ('Ehtel Engram', 24, 26),
     ('Jacinta Jara', 53, 89),
     ('Cammie Cassidy', 109, 153),
     ('Tana Tonn', 170, 172),
     ('Sindy Simek', 179, 193),
     ('Hettie Housand', 205, 211),
     ('Delbert Degarmo', 234, 250),
     ('Jamaal Jonson', 267, 278),
     ('Brenna Blanca', 324, 346),
     ('Leia Lieu', 355, 367),
     ('Izola Igoe', 375, 396),
     ('Edythe Estepp', 436, 443),
     ('Migdalia Manske', 484, 492),
     ('Nakisha Ned', 525, 551),
     ('Lawrence Longacre', 554, 565),
     ('Glenn Garst', 583, 588),
     ('Kandra Keasler', 641, 664),
     ('Diann Dimeo', 698, 700),
     ('Marry Montag', 708, 714),
     ('Hilma Hodgin', 760, 765),
     ('Margit Mendenhall', 767, 778),
     ('Sherlene Schneck', 841, 875),
     ('Magda Mcdowell', 904, 944),
     ('Rod Ruggiero', 973, 989),
     ('Tilda Tippie', 995, 1010)]





class TestGreedy(unittest.TestCase):

    def test_change_greedy_example1(self):
        result = change_greedy(82, [1, 10, 25, 5])
        self.assertEqual([(3, 25), (1, 5), (2, 1)], result)

    def test_change_greedy_example2(self):
        result = change_greedy(80, [1, 10, 25])
        self.assertEqual([(3, 25), (5, 1)], result)

    def test_change_greedy_example3(self):
        result = change_greedy(82, [10, 25, 5])
        self.assertEqual(None, result)

    def test_buskers_example(self):
        result = buskers_schedule(buskers_example1)
        expected_result = [('b', 1, 4), ('e', 4, 7), ('h', 8, 11)]
        self.assertEqual(expected_result, result)

    def test_buskers_example2(self):
        result = buskers_schedule(buskers_example2)
        self.assertEqual(buskers_expected1, result)

    def test_knapsack_example(self):
        result = fractional_knapsack(9, items)
        self.assertEqual(45.0, result)

    def test_knapsack_example2(self):
        result = fractional_knapsack(11, [])
        self.assertEqual(0.0, result)

    def test_knapsack_example3(self):
        result = fractional_knapsack(100, items)
        self.assertEqual(61.0, result)


if __name__ == '__main__':
    unittest.main()
