def right_triangle_area(base, height):
    # base and height are positive integers
    # Purpose: Calculate the area of a right triangle
    # Signature: number number -> number
    return 0.5 * base * height

def test_rt_area():
    # Test right triangles with positive integer 
    # bases and heights
    # Test several right triangles with 
    # different bases and heights
    # Test right triangles with equal bases 
    # and heights
    assert right_triangle_area(3,4)==6, \
           "test_rt_area: Test case 0 failed"
    assert right_triangle_area(5,12)==30, \
           "test_rt_area: Test case 1 failed"
    #assert right_triangle_area(8.5,14.3)==60.775, \
    #       "test_rt_area: Test case 2 failed"
    assert abs((right_triangle_area(8.5,14.3)-60.775))<0.001, \
           "test_rt_area: Test case 2 failed"
    assert right_triangle_area(7,24)==84, \
           "test_rt_area: Test case 3 failed"
    assert right_triangle_area(10,10)==50, \
           "test_rt_area: Test case 4 failed"
    assert right_triangle_area(1,1)==0.5, \
           "test_rt_area: Test case 5 failed"
    
test_rt_area()
