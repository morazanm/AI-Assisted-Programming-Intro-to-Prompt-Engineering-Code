def fact(n):
    """
    Signature natnum -> natnum
    Purpose: Compute n!
    Design Idea:: Use an accumulator to compute n!
    """
    def factWhile():
        """
        Signature natnum natnum -> natnum
        Purpose: Compute n! with accumulator
        Design Idea: Use tail recursion to accumulate the result
        Loop Invariant:
          acc = (n-k)! and k >= 0
        """
        k = n
        acc = 1
        # Loop Invariant: acc = (n-k)! and k >= 0
        while k > 0:
            # acc = (n-k)! and k > 0
            acc = acc * k
            # acc = (n-k+1)! = (n-(k-1))! and k > 0
            k = k - 1
            # acc = (n-k)! and k >= 0
        # acc = (n-k)! and k >= 0 and k <= 0
        # ==> k = 0
        # ==> acc = n!
        return acc
        # Termination Argument:
        #   k starts at n. It is decreased by 1 each loop iteration 
        #   until it reaches 0 and the loop terminates

    return factWhile()

def test_fact():
    """
    Signature: -> None
    Purpose: Test the fact function
    Design Idea: Test with several values of n
    """
    assert fact(0) == 1, "Test case 0 failed"
    assert fact(1) == 1, "Test case 1 failed"
    assert fact(5) == 120, "Test case 2 failed"
    assert fact(10) == 3628800, "Test case 3 failed"

test_fact()