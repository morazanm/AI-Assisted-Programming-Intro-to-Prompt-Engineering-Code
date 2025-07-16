def swap(L, i, j):
    """
    Signature: (listof X) natnum natnum -> None
    Purpose: Swap L[i] and L[j]
    Design idea: Use a temporary variable to store L[i]
                 Mutate L[i] to be L[j]
                 Mutate l[j] to be the temporary variable
    Assumption: i and j are valid indices into L, L[i]==I, and L[j]==J
    Document the correctness of the mutations using Hoare logic.
    Write an assertion as a comment before and after each mutation.
    Do not include assert statements in the code.
    """
    # L[i] == I, L[j] == J
    temp = L[i]  # Store L[i] in a temporary variable
    # L[i] == I, L[j] == J, temp == I
    L[i] = L[j]  # Set L[i] to L[j]
    # L[i] == J, L[j] == J, temp == I
    L[j] = temp  # Set L[j] to the temporary variable
    # L[j] == I, L[i] == J

def test_swap():
    """
    Signature: () -> None
    Purpose: Test the swap function with various cases.
    Design idea: Use different types of (listof X) and different 
                 valid indices to show the effect is achieved.
    Include fail test strings, "Test case n failed", starting at n==0
    """
    # Test case 0: Swap two integers
    L = [1, 2, 3]
    swap(L, 0, 1)
    assert L == [2, 1, 3], "Test case 0 failed"
    # Test case 1: Swap two strings
    L = ["apple", "banana", "cherry"]
    swap(L, 0, 2)
    assert L == ["cherry", "banana", "apple"], "Test case 1 failed"
    # Test case 2: Swap elements in a list with mixed types
    L = [1, "two", 3.0]
    swap(L, 1, 2)
    assert L == [1, 3.0, "two"], "Test case 2 failed"
    # Test case 3: Swap the same element (should remain unchanged)
    L = [5, 6, 7]
    swap(L, 1, 1)
    assert L == [5, 6, 7], "Test case 3 failed"

    # Test case 4: Swap first and last elements in a longer list
    L = [10, 20, 30, 40, 50]
    swap(L, 0, 4)
    assert L == [50, 20, 30, 40, 10], "Test case 4 failed"

test_swap()


    