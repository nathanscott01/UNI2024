"""
Nathan Scott
COSC262 Lab 10
Computational Geometry Basics
"""


class Vec:
    """A simple vector in 2D. Also used as a position vector for points"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)

    def __mul__(self, scale):
        """Multiplication by a scalar"""
        return Vec(self.x * scale, self.y * scale)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def lensq(self):
        return self.dot(self)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)


def signed_area(a, b, c):
    """Twice the area of the triangle abc.
       Positive if abc are in counter clockwise order.
       Zero if a, b, c are colinear.
       Otherwise negative.
    """
    p = b - a
    q = c - a
    return p.x * q.y - q.x * p.y


def is_on_segment(p, a, b):
    """Return True point p is on segment a to b"""
    if signed_area(p, a, b) == 0:
        if (a - p).lensq() <= (b - a).lensq() and (b - p).lensq() <= (b - a).lensq():
            return True
    return False


def is_ccw(a, b, c):
    """True iff triangle abc is counter-clockwise."""
    p = b - a
    q = c - a
    area = p.x * q.y - q.x * p.y
    # May want to throw an exception if area == 0
    return area >= 0


def classify_points(line_start, line_end, points):
    """Return a tuple (l, r) where l is the number of points to the left
    of the line, and r is the number of points to the right"""
    left = 0
    right = 0
    for point in points:
        if is_ccw(line_start, line_end, point):
            left += 1
        else:
            right += 1
    return tuple((right, left))


def intersecting(a, b, c, d):
    """Return True if line a to b is intersecting line c to d"""
    return is_ccw(a, d, b) != is_ccw(a, c, b) and (is_ccw(c, a, d) != is_ccw(c, b, d))


def is_strictly_convex(vertices):
    """Return True if polygon vertices are convex"""
    for i in range(len(vertices)):
        v1 = vertices[i]
        if i == len(vertices) - 1:
            v2 = vertices[0]
            v3 = vertices[1]
        elif i == len(vertices) - 2:
            v2 = vertices[i + 1]
            v3 = vertices[0]
        else:
            v2 = vertices[i + 1]
            v3 = vertices[i + 2]
        if not is_ccw(v1, v2, v3):
            return False
    return True


def gift_wrap(points):
    """ Returns points on convex hull in CCW using the Gift Wrap algorithm"""
    # Get the bottom-most point (and left-most if necessary).
    assert len(points) >= 3
    bottommost = min(points, key=lambda p: (p.y, p.x))
    hull = [bottommost]
    done = False

    # Loop, adding one vertex at a time, until hull is (about to be) closed.
    while not done:
        candidate = None
        # Loop through all points, looking for the one that is "rightmost"
        # looking from last point on hull
        for p in points:
            if p is hull[-1]:
                continue
            if candidate is None:
                if len(hull) == 1:
                    if hull[0].x < p.x:
                        candidate = p
                elif is_ccw(hull[-2], hull[-1], p):  # ** FIXME **
                    candidate = p
        if candidate is bottommost:
            done = True  # We've closed the hull
        else:
            hull.append(candidate)

    return hull


points = [
    Vec(1, 99),
    Vec(0, 100),
    Vec(50, 0),
    Vec(50, 1),
    Vec(50, 99),
    Vec(50, 50),
    Vec(100, 100),
    Vec(99, 99)]
verts = gift_wrap(points)
for v in verts:
    print(v)
