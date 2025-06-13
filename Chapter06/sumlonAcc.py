def sum_lon(L):
 """
 Signature: (listof number) -> number
 Purpose: Return the sum of all numbers in the list.
 Design Idea: Use an accumulator to compute the sum of the list.
 """
 def sum_helper(lst, acc):
        """
        Signature: (listof number) number -> number
        Purpose: To compute of the sum of lst by accumulating the sum of the processed part of the list.
        Design Idea: If the lst is empty return the accumulator.
                    Otherwise, add the first number to the accumator and
                    recurisvely process the rest of the list.
        Accumulator Invariant:
          acc = sum of the numbers in the processed part of lst (i.e., L-lst)
        """
        if lst == []:
            return acc
        else:
            return sum_helper(lst[1:], acc + lst[0])
 return sum_helper(L, 0)  

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