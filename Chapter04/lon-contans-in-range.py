"""
Template for a function on a range
def f_on_range(rng ...):
 if len(rng) == 0:
  return <base case value>
 else:
  return <combine f_on_number(rng[0]) f_on_range(rng[1:])>

def test_f_on_range():
 Signature: -> None
 Purpose: Test f_on_range 
 Design Idea: 

 assert f_on_range([L ...]) == ..., "Test case 0 failed"
 ...
"""

def lon_contains_in_range(lst, x, rng):
    """
    Signature: (listof number) number range -> Boolean throws Exception
    Purpose: Determine if list elements in the given index range contain x
    Design Idea: Travese the given index range and check if x is equal to 
                 any of the corresponding list elements when the interval
                 is not empty and only contains valid indexes into the list.
    """
    if len(rng) == 0:
        return False
    elif (rng[0] < 0) or (rng[len(rng)-1] > len(lst)-1):
        raise ValueError("Range contains invalid indexes into the list.")
    else:
        return ((lst[rng[0]]==x) or (lon_contains_in_range(lst, x, rng[1:])))

def test_lon_contains_in_range():
    """
    Signature: -> None
    Purpose: Test lon_contains_in_range function
    Design Idea: Test the empty and nonempty ranges
                 Test empty and non empty lists
                 Tests lists that contain the searched element in the range
                 Test list that does not contain the element in the range
    """
    assert lon_contains_in_range([], 1, range(0, 0)) == False
    assert lon_contains_in_range([1, 2, 3, 4], 1, range(0, 0)) == False
    assert lon_contains_in_range([1, 2, 3, 4], 1, range(0, 1)) == True
    assert lon_contains_in_range([1, 2, 3, 4], 2, range(0, 1)) == False
    assert lon_contains_in_range([1, 2, 3, 4], 2, range(0, 4)) == True
    assert lon_contains_in_range([1, 2, 3, 4], 5, range(0, 3)) == False
    assert lon_contains_in_range([1, 2, 3, 4], 1, range(0, 4)) == True
    assert lon_contains_in_range([1, 2, 3, 4], 2, range(0, 2)) == True
    assert lon_contains_in_range([1, 2, 3, 4], -1, range(0, 4)) == False

test_lon_contains_in_range()