"""
Data definition
A coordinate is either:
  1. A 2D cartesian coordinate (number, number, None)
  2. A 3D cartesian coordinate (number, number, number)
"""

"""
Define a class for coordinate.

The services provided by the class are:
    - creation of a coordinate from either 2 or 3 arguments
    - access to the x, y, and z coordinates
    - mutation of the x, y, and z coordinates
    - a predicate that checks if the coordinate is 2D
    - a predicate that checks if the coordinate is 3D
"""
class Coordinate:
    def __init__(self, *coords):
        if len(coords) == 2:
            self.x = coords[0]
            self.y = coords[1]
            self.z = None
            
        elif len(coords) == 3:
            self.x = coords[0]
            self.y = coords[1]
            self.z = coords[2]
        else:
            raise ValueError("Invalid number of arguments")
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_z(self):
        return self.z
    
    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_z(self, z):
        self.z = z
    
    def is_2d(self):
        return self.z == None

    def is_3d(self):
        return self.z != None

def test_Coordinate():
    """
    Define a function to test the Coordinate class.
    Test several coordinates, both 2D and 3D.
    Test coordinates with negative, positive values, and both positive and negative values.
    Test coordinates with zero values.
    """

    # Test 2D coordinates
    coord_2d = Coordinate(1, 2)
    assert coord_2d.get_x() == 1
    assert coord_2d.get_y() == 2
    assert coord_2d.is_2d() == True
    assert coord_2d.is_3d() == False

    coord_2d_neg = Coordinate(-1, -2)
    assert coord_2d_neg.get_x() == -1
    assert coord_2d_neg.get_y() == -2
    assert coord_2d_neg.is_2d() == True
    assert coord_2d_neg.is_3d() == False

    # Test 3D coordinates
    coord_3d = Coordinate(1, 2, 3)
    assert coord_3d.get_x() == 1
    assert coord_3d.get_y() == 2
    assert coord_3d.get_z() == 3
    assert coord_3d.is_2d() == False
    assert coord_3d.is_3d() == True

    coord_3d_neg = Coordinate(-1, -2, -3)
    assert coord_3d_neg.get_x() == -1
    assert coord_3d_neg.get_y() == -2
    assert coord_3d_neg.get_z() == -3
    assert coord_3d_neg.is_2d() == False
    assert coord_3d_neg.is_3d() == True

    # Test coordinates with zero values
    coord_2d_zero = Coordinate(0, 0)
    assert coord_2d_zero.get_x() == 0
    assert coord_2d_zero.get_y() == 0   

    coord_3d_zero = Coordinate(0, 0, 0)
    assert coord_3d_zero.get_x() == 0
    assert coord_3d_zero.get_y() == 0
    assert coord_3d_zero.get_z() == 0

    coord_2d_pos_neg = Coordinate(1, -2)
    assert coord_2d_pos_neg.get_x() == 1
    assert coord_2d_pos_neg.get_y() == -2
    assert coord_2d_pos_neg.is_2d() == True
    assert coord_2d_pos_neg.is_3d() == False

    coord_3d_pos_neg = Coordinate(1, -2, 3)
    assert coord_3d_pos_neg.get_x() == 1
    assert coord_3d_pos_neg.get_y() == -2
    assert coord_3d_pos_neg.get_z() == 3
    assert coord_3d_pos_neg.is_2d() == False
    assert coord_3d_pos_neg.is_3d() == True

test_Coordinate()


def dist_origin(coord):
    """
    Signature: Coordinate -> number
    Purpose: Returns the distance of the coordinate from the origin
    Design Idea: Use the distance formulas for 2D and 3D coordinates
    """
    if coord.is_2d():
        return (coord.get_x()**2 + coord.get_y()**2)**0.5
    else:
        return (coord.get_x()**2 + coord.get_y()**2 + coord.get_z()**2)**0.5

def test_dist_origin():
    """
    Define a function to test the dist_origin function.
    Test several coordinates, both 2D and 3D.
    Test coordinates with negative and positive values.
    Test coordinates with zero values.
    """

    # Test 2D coordinates
    coord_2d = Coordinate(3, 4)
    assert dist_origin(coord_2d) == 5.0

    coord_2d_neg = Coordinate(-3, -4)
    assert dist_origin(coord_2d_neg) == 5.0

    coord_2d_zero = Coordinate(0, 0)
    assert dist_origin(coord_2d_zero) == 0.0

    # Test 3D coordinates
    coord_3d = Coordinate(1, 2, 2)
    assert dist_origin(coord_3d) == 3.0

    coord_3d_neg = Coordinate(-1, -2, -2)
    assert dist_origin(coord_3d_neg) == 3.0

test_dist_origin()
