"""
A (listof X) is either:
  1. []
  2. [X] + (listof X)

Template for a function on a (listof X):

  def f_of_listof_X(lst ...):
    Signature: (listof X) ... -> ...
    Purpose: 
    Design Idea: 
    if lst == []:
        return base_case_value
    else:
        return combine...(f_on_X lst[0])...f_of_listof_X(lst[1:])... 

  def test_f_of_listof_X():
    Signature: -> None
    Purpose: Test f_of_listof_X function
    Design Idea: 

    assert f_of_listof_X([L ...]) == ..., "Test case 0 failed"

test_f_of_listof_X()

Alternative template for a function on a (listof X):

  def f_of_listof_X(lst ...):
    Signature: (listof X) ... -> ...
    Purpose: 
    Design Idea: 

    res = base_case_value
    for x in lst:
        res = combine...f_on_X(x)...res
    return res
"""

def sum_lon(lst):
 """
 Signature: (listof number) -> number
 Purpose: Return the sum of all numbers in the list.
 Design Idea: If the list is empty, return 0. Otherwise, return the first element plus the sum of the rest of the list.
 """
 if lst == []:
     return 0
 else:
     return lst[0] + sum_lon(lst[1:])  # Recursive call with the rest of the list
    
def test_sum_lon():
    """
    Test function for sum_list
    Test empty list, single element, multiple elements,,
        positive and negative numbers, and zero.
    """
    assert sum_lon([]) == 0, "Test case 0 failed"
    assert sum_lon([1]) == 1, "Test case 1 failed"
    assert sum_lon([1, 2]) == 3, "Test case 2 failed"
    assert sum_lon([1, 2, 3]) == 6, "Test case 3 failed"
    assert sum_lon([1, -2, 3]) == 2, "Test case 4 failed"
    assert sum_lon([-1, -2, -3]) == -6, "Test case 5 failed"
    assert sum_lon([0, 0, 0]) == 0, "Test case 6 failed"
    assert sum_lon([1, -1, 0]) == 0, "Test case 7 failed"
    assert sum_lon([1, 2, 3, 4, 5]) == 15, "Test case 8 failed"

test_sum_lon()

def lst_avg(lst):
 """
 Signature: (listof number) -> number
 Purpose: Compute the average of the given list.
 Design Idea: Use the sum_list and length functions to compute the average.
 Assumption: the given list is not empty.
 """
 return sum_lon(lst) / len(lst)

def test_lst_avg():
    """
    Test function for lst_avg
    Test empty list, single element, multiple elements,,
        positive and negative numbers, and zero.
    """
    assert lst_avg([1]) == 1, "Test case 0 failed"
    assert lst_avg([1, 2]) == 1.5, "Test case 1 failed"
    assert lst_avg([1, 2, 3]) == 2, "Test case 2 failed"
    assert lst_avg([1, -2, 3]) == 0.6666666666666666, "Test case 3 failed"
    assert lst_avg([-1, -2, -3]) == -2, "Test case 4 failed"
    assert lst_avg([0, 0, 0]) == 0, "Test case 5 failed"
    assert lst_avg([1, -1, 0]) == 0, "Test case 6 failed"
    assert lst_avg([1, 2, 3, 4, 5]) == 3, "Test case 7 failed"

test_lst_avg()
