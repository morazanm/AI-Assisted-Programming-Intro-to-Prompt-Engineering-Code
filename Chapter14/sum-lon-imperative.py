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
        Design Idea: 
           Use a while-loop to traverse the list.
            If the list is empty, return the accumulator.
            Otherwise, add the first number to the accumulator and
            update the traversal variable to process the rest of the list.
        Accumulator Invariant:
          acc = sum of the numbers in the processed part of lst (i.e., L-lst)
        """
        # Initialize local variables
        a_lon = lst  # a_lon traverses lst
        sum = acc    # sum accumulates the sum of processed elements
        # Accumulator Invariant:
        # sum == sum of the numbers in the processed part of a_lon (i.e., L - a_lon)
        # { sum == sum(L - a_lon) }
        while a_lon != []:
            # { sum == sum(L - a_lon) }
            sum = sum + a_lon[0]
            # { sum == sum(L - a_lon[1:]) }
            a_lon = a_lon[1:]
            # { sum == sum(L - a_lon) }
        # { a_lon == [] and sum == sum(L) }
        return sum
        # Termination Argument: The loop halts because with each iteration, a_lon becomes shorter by one element.
        # Since a_lon is initialized to a finite list, eventually a_lon becomes empty and the loop condition fails.
 return sum_helper(L, 0)  

def test_sum_lon():
    """
    Test function for sum_list
    Test empty list, single element, multiple elements,,
        positive and negative numbers, and zero.
    Test a list of length 2000
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
    assert sum_lon(list(range(2000))) == 1999000, "Test case 9 failed"

test_sum_lon()