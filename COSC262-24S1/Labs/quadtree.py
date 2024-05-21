"""
Nathan Scott
COSC262 Lab 11
Quadtrees
"""


import matplotlib.pyplot as plt


class Vec:
    """A simple vector in 2D. Can also be used as a position vector from
       origin to define points.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Vector addition"""
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Vector subtraction"""
        return Vec(self.x - other.x, self.y - other.y)

    def __mul__(self, scale):
        """Multiplication by a scalar"""
        return Vec(self.x * scale, self.y * scale)

    def dot(self, other):
        """Dot product"""
        return self.x * other.x + self.y * other.y

    def lensq(self):
        """The square of the length"""
        return self.dot(self)

    def __getitem__(self, axis):
        return self.x if axis == 0 else self.y

    def __repr__(self):
        """String representation of self"""
        return "({}, {})".format(self.x, self.y)


class QuadTree:
    """A QuadTree class for COSC262.
       Richard Lobb, May 2019
    """
    MAX_DEPTH = 20

    def __init__(self, points, centre, size, depth=0, max_leaf_points=2):
        self.centre = centre
        self.size = size
        self.depth = depth
        self.max_leaf_points = max_leaf_points
        self.children = []
        # *** COMPLETE ME ***
        self.points = [p for p in points if self.in_square(p)]
        if len(self.points) > self.max_leaf_points and depth < QuadTree.MAX_DEPTH:
            self.is_leaf = False
            for i in range(4):
                child_centre = self.find_center(i)
                child_size = float(self.size) / 2
                child = QuadTree(points, child_centre, child_size, depth + 1, max_leaf_points)
                self.children.append(child)
        else:
            self.is_leaf = True

    def in_square(self, p):
        """Check if point is within the square"""
        d = float(self.size) / 2
        return ((self.centre.x - d < p.x <= self.centre.x + d) and
                (self.centre.y - d < p.y <= self.centre.y + d))

    def find_center(self, i):
        """Find the center of the child quad"""
        if i == 0:
            return Vec(self.centre.x - float(self.size) / 4, self.centre.y - float(self.size) / 4)
        elif i == 1:
            return Vec(self.centre.x - float(self.size) / 4, self.centre.y + float(self.size) / 4)
        elif i == 2:
            return Vec(self.centre.x + float(self.size) / 4, self.centre.y - float(self.size) / 4)
        else:
            return Vec(self.centre.x + float(self.size) / 4, self.centre.y + float(self.size) / 4)

    def plot(self, axes):
        """Plot the dividing axes of this node and
           (recursively) all children"""
        if self.is_leaf:
            axes.plot([p.x for p in self.points], [p.y for p in self.points], 'bo')
        else:
            axes.plot([self.centre.x - self.size / 2, self.centre.x + self.size / 2],
                      [self.centre.y, self.centre.y], '-', color='gray')
            axes.plot([self.centre.x, self.centre.x],
                      [self.centre.y - self.size / 2, self.centre.y + self.size / 2],
                      '-', color='gray')
            for child in self.children:
                child.plot(axes)
        axes.set_aspect(1)

    def __repr__(self, depth=0):
        """String representation with children indented"""
        indent = 2 * self.depth * ' '
        if self.is_leaf:
            return indent + "Leaf({}, {}, {})".format(self.centre, self.size, self.points)
        else:
            s = indent + "Node({}, {}, [\n".format(self.centre, self.size)
            for child in self.children:
                s += child.__repr__(depth + 1) + ',\n'
            s += indent + '])'
            return s


def build_quad(point_list, centre_point, graph_size, plot_tree=False, print_tree=False, max_leaf_points=2):
    """Helper function to build a quadtree from a list of points"""
    vecs = [Vec(*p) for p in point_list]
    tree = QuadTree(vecs, centre_point, graph_size, 0, max_leaf_points)
    if print_tree:
        print(tree)
    if plot_tree:
        axes = plt.axes()
        tree.plot(axes)
        axes.set_xlim(0, graph_size)
        axes.set_ylim(0, graph_size)
        plt.show()
    return tree
