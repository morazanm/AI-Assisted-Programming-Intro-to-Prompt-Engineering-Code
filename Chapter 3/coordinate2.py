"""
A Coordinate is either
 - A Coordinate2D object
 - A Coordinate3D object

A Coordinate2D has two numbers and its interface offers these services:
 - get the x coordinate
 - get the y coordinate

A Coordinate3D has three numbers and its interface offers these services:
 - get the x coordinate
 - get the y coordinate
 - get the z coordinate
"""

class Coordinate2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

class Coordinate3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z


def test_coordinates():
    """
    Test 2D and 3D coordinates
    Test coordinates with negative, positive and zero values
    Test coordinates with both negative and positive values
    """
    # Test 2D coordinates
    coord_2d = Coordinate2D(1, 2)
    assert coord_2d.get_x() == 1
    assert coord_2d.get_y() == 2

    coord_2d = Coordinate2D(-1, -2)
    assert coord_2d.get_x() == -1
    assert coord_2d.get_y() == -2

    coord_2d = Coordinate2D(0, 0)
    assert coord_2d.get_x() == 0
    assert coord_2d.get_y() == 0

    # Test 3D coordinates
    coord_3d = Coordinate3D(1, 2, 3)
    assert coord_3d.get_x() == 1
    assert coord_3d.get_y() == 2
    assert coord_3d.get_z() == 3

    coord_3d = Coordinate3D(-1, -2, -3)
    assert coord_3d.get_x() == -1
    assert coord_3d.get_y() == -2
    assert coord_3d.get_z() == -3

    coord_3d = Coordinate3D(0, 0, 0)
    assert coord_3d.get_x() == 0    
    assert coord_3d.get_y() == 0
    assert coord_3d.get_z() == 0

    # Test mixed coordinates
    coord_2d = Coordinate2D(1, -2)
    assert coord_2d.get_x() == 1
    assert coord_2d.get_y() == -2

    coord_3d = Coordinate3D(-1, 2, 3)
    assert coord_3d.get_x() == -1
    assert coord_3d.get_y() == 2
    assert coord_3d.get_z() == 3

    coord_3d = Coordinate3D(1, -2, 3)
    assert coord_3d.get_x() == 1
    assert coord_3d.get_y() == -2
    assert coord_3d.get_z() == 3
    
test_coordinates()

def dist_origin(coord):
    """
    Signature: Coordinate -> number
    Purpose: Returns the distance of the coordinate from the origin
    Design Idea: Use the distance formulas for 2D and 3D coordinates
    """
    if isinstance(coord, Coordinate2D):
        return (coord.get_x()**2 + coord.get_y()**2)**0.5
    else:
        return (coord.get_x()**2 + coord.get_y()**2 + coord.get_z()**2)**0.5

def test_dist_origin():
    """
    Signature: () -> None
    Purpose: Tests the dist_origin function
    Test coordinates with negative, positive and zero values
    Test coordinates with both negative and positive values
    """
    # Test 2D coordinates
    coord_2d = Coordinate2D(3,4)
    assert dist_origin(coord_2d)==5.0
    coord_2d_neg = Coordinate2D(-3,-4)
    assert dist_origin(coord_2d_neg)==5.0
    coord_2d_zero=Coordinate2D(0,0)
    assert dist_origin(coord_2d_zero)==0.0
    # Test 3 D coordinates
    coord_3d = Coordinate3D(1,2,2)
    assert dist_origin(coord_3d)==3.0
    coord_3d_neg = Coordinate3D(-1 ,-2 ,-2)
    assert dist_origin(coord_3d_neg )==3.0
    # Extra Tests
    coord_2d = Coordinate2D(3, 4)
    assert dist_origin(coord_2d) == 5, "Test Case 0 Failed"

    coord_3d = Coordinate3D(1, 2, 2)
    assert dist_origin(coord_3d) == 3, "Test Case 1 Failed"

    coord_2d_neg = Coordinate2D(-3, -4)
    assert dist_origin(coord_2d_neg) == 5, "Test Case 2 Failed"

    coord_3d_neg = Coordinate3D(-1, -2, -2)
    assert dist_origin(coord_3d_neg) == 3, "Test Case 3 Failed"

    coord_3d = Coordinate3D(10, 0, -4)
    assert abs(dist_origin(coord_3d)-10.770)<=0.001, "Test Case 4 Failed"

test_dist_origin()

