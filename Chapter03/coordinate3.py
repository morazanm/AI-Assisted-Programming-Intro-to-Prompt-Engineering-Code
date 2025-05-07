"""
A Coordinate is either
 - A Coordinate2D object
 - A Coordinate3D object

A Coordinate2D has two numbers and its interface offers these services:
 - get the x coordinate
 - get the y coordinate
 - compute the distance to the origin

A Coordinate3D has three numbers and its interface offers these services:
 - get the x coordinate
 - get the y coordinate
 - get the z coordinate
 - compute the distance to the origin
"""

class Coordinate2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_to_origin(self):
        return (self.x**2 + self.y**2)**0.5 

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

    def distance_to_origin(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    
def distance_to_origin(coordinate):
    """
    Signature: Coordinate -> number
    Purpose: Compute the distance to the origin of a coordinate
    Design Idea: Use the Coordinate interface to compute the distance to the origin
    """
    return coordinate.distance_to_origin()

def test_distance_to_origin():
    """
    Signature: () -> None
    Purpose: Test the distance_to_origin function
    Design Idea: Create Coordinate2D and Coordinate3D objects and test the distance_to_origin function
                 Test coordinates that contain zero, positive, and negative values
    """
    # Test Coordinate2D
    coord2d = Coordinate2D(3, 4)
    assert distance_to_origin(coord2d) == 5.0, "Test 0 failed for distance to origin"
    coord2d = Coordinate2D(0, 0)
    assert distance_to_origin(coord2d) == 0.0, "Test 1 failed for distance to origin"
    coord2d = Coordinate2D(-3, -4)
    assert distance_to_origin(coord2d) == 5.0, "Test 2 failed for distance to origin"
    
    # Test Coordinate3D
    coord3d = Coordinate3D(1, 2, 2)
    assert distance_to_origin(coord3d) == 3.0, "Test 3 failed for distance to origin"
    coord3d = Coordinate3D(0, 0, 0)
    assert distance_to_origin(coord3d) == 0.0, "Test 4 failed for distance to origin"
    coord3d = Coordinate3D(-1, -2, -2)
    assert distance_to_origin(coord3d) == 3.0, "Test 5 failed for distance to origin"

test_distance_to_origin()
