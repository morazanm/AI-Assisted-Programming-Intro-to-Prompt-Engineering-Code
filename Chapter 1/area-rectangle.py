def area_of_rectangle(length, width):
    return length * width

def test_area_of_rectangle():
    assert area_of_rectangle(4,3)==12, \
    "test_area_of_rectangle: Test case 0 failed"
    assert area_of_rectangle(1,5)==5, \
    "test_area_of_rectangle: Test case 1 failed"
    assert area_of_rectangle(2,2)==4, \
    "test_area_of_rectangle: Test case 2 failed"
    assert area_of_rectangle(5,10)==50, "test_area_of_rectangle: Test case 3 failed"
    assert area_of_rectangle(2,3)==6, "test_area_of_rectangle: Test case 4 failed"
    assert area_of_rectangle(7,8)==56, "test_area_of_rectangle: Test case 5 failed"
    assert area_of_rectangle(0,10)==0, "test_area_of_rectangle: Test case 6 failed"
    assert area_of_rectangle(5,0)==0, "test_area_of_rectangle: Test case 7 failed"

test_area_of_rectangle()