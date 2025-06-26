def fact(n):
    """
    Signature natnum -> natnum
    Purpose: Compute n!
    Design Idea:: Use an accumulator to compute n!
    """
    def factAcc(k, acc):
        """
        Signature natnum natnum -> natnum
        Purpose: Compute n! with accumulator
        Design Idea: Use tail recursion to accumulate the result
        Accumulator Invariant:
          acc = (n-k)!
        """
        if k == 0:
            return acc
        else:
            return factAcc(k - 1, k * acc)

    return factAcc(n, 1)

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

