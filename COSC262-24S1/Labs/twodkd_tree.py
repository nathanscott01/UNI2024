"""
Nathan Scott
COSC262 Lab 11
2D KD Tree
"""

import matplotlib.pyplot as plt
import math


class Vec:
    """A simple vector in 2D. Can also be used as a position vector from
       origin to define points.
    """
    point_num = 0
    box_calls = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.label = 'P' + str(Vec.point_num)
        Vec.point_num += 1

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

    def in_box(self, bottom_left, top_right):
        """True iff this point (warning, not a vector!) lies within or on the
           boundary of the given rectangular box area"""
        Vec.box_calls += 1
        return bottom_left.x <= self.x <= top_right.x and bottom_left.y <= self.y <= top_right.y

    def __getitem__(self, axis):
        return self.x if axis == 0 else self.y

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

    def __lt__(self, other):
        """Less than operator, for sorting"""
        return (self.x, self.y) < (other.x, other.y)


class KdTree:
    """A 2D k-d tree"""
    LABEL_POINTS = True
    LABEL_OFFSET_X = 0.25
    LABEL_OFFSET_Y = 0.25

    def __init__(self, points, depth=0, max_depth=10):
        """Initialiser, given a list of points, each of type Vec, the current
           depth within the tree (0 for the root) and the maximum depth
           allowable for a leaf node.
        """
        if len(points) < 2 or depth >= max_depth:  # Ensure at least one point per leaf
            self.is_leaf = True
            self.points = points
        else:
            self.is_leaf = False
            self.axis = depth % 2  # 0 for vertical divider (x-value), 1 for horizontal (y-value)
            points = sorted(points, key=lambda p: p[self.axis])
            halfway = len(points) // 2
            self.coord = points[halfway - 1][self.axis]
            self.leftorbottom = KdTree(points[:halfway], depth + 1, max_depth)
            self.rightortop = KdTree(points[halfway:], depth + 1, max_depth)

    def points_in_range(self, query_rectangle):
        """Return a list of all points in the tree 'self' that lie within or on the
           boundary of the given query rectangle, which is defined by a pair of points
           (bottom_left, top_right).
        """
        if self.is_leaf:
            return [p for p in self.points if p.in_box(query_rectangle[0], query_rectangle[1])]
        else:
            matches = []
            # Check if x-axis
            if self.axis == 0:
                # Check if rectangle in left space
                if query_rectangle[0].x <= self.coord:
                    matches.extend(self.leftorbottom.points_in_range(query_rectangle))
                # Check if in right space
                if query_rectangle[1].x >= self.coord:
                    matches.extend(self.rightortop.points_in_range(query_rectangle))
            # If y-axis,
            else:
                # Check if rectangle in bottom space
                if query_rectangle[0].y <= self.coord:
                    matches.extend(self.leftorbottom.points_in_range(query_rectangle))
                # Check if also in top space
                if query_rectangle[1].y >= self.coord:
                    matches.extend(self.rightortop.points_in_range(query_rectangle))
            # Return the results
            return matches

    def plot(self, axes, top, right, bottom, left, depth=0):
        """Plot the kd tree. axes is the matplotlib axes object on
           which to plot, top, right, bottom, left are the coordinates of
           the bounding box of the plot.
        """

        if self.is_leaf:
            axes.plot([p.x for p in self.points], [p.y for p in self.points], 'bo')
            if self.LABEL_POINTS:
                for p in self.points:
                    axes.annotate(p.label, (p.x, p.y),
                                  xytext=(p.x + self.LABEL_OFFSET_X, p.y + self.LABEL_OFFSET_Y))
        else:
            if self.axis == 0:
                axes.plot([self.coord, self.coord], [bottom, top], '-', color='gray')
                self.leftorbottom.plot(axes, top, self.coord, bottom, left, depth + 1)
                self.rightortop.plot(axes, top, right, bottom, self.coord, depth + 1)
            else:
                axes.plot([left, right], [self.coord, self.coord], '-', color='gray')
                self.leftorbottom.plot(axes, self.coord, right, bottom, left, depth + 1)
                self.rightortop.plot(axes, top, right, self.coord, left, depth + 1)
        if depth == 0:
            axes.set_xlim(left, right)
            axes.set_ylim(bottom, top)

    def __repr__(self, depth=0):
        """String representation of self"""
        if self.is_leaf:
            return depth * 2 * ' ' + "Leaf({})".format(self.points)
        else:
            s = depth * 2 * ' ' + "Node({}, {}, \n".format(self.axis, self.coord)
            s += self.leftorbottom.__repr__(depth + 1) + '\n'
            s += self.rightortop.__repr__(depth + 1) + '\n'
            s += depth * 2 * ' ' + ')'  # Close the node's opening parens
            return s


def build_tree(point_tuples, plot_points=False, print_tree=False, max_depth=10):
    points = [Vec(*tup) for tup in point_tuples]
    tree = KdTree(points, 0, max_depth)
    if print_tree:
        print(tree)
    if plot_points:
        max_x = max(point_tuples, key=lambda point: point[0])[0]  # Get maximum x value
        max_y = max(point_tuples, key=lambda point: point[1])[1]  # Get maximum y value
        max_x_rounded = math.ceil(max_x / 5) * 5  # Find the next multiple of 5 larger than max_x
        max_y_rounded = math.ceil(max_y / 5) * 5  # Find the next multiple of 5 larger than max_y
        axes = plt.axes()
        tree.plot(axes, max_y_rounded, max_x_rounded, 0, 0)
        plt.show()
    return tree


# Call to main provided from lab
# Call is obselete as it is implemented in tests
# main()
