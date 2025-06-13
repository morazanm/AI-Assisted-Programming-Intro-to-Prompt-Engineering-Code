import time

def fib(n):
    """
    Signature: natnum -> natnum
    Purpose: Returns the nth Fibonacci number
    Design Idea: If n<2, return n; otherwise, return the sum of the two preceding Fibonacci numbers.
    """
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
    """
    Termination argument: A recursive call is only made when n >= 2. 
    The recurive calls, respectively, decrement n by 1 and by 2.
    Eventually, n becomes less than 2, and the function terminates.
    """

def test_fib():
    """
    Signature: () -> None
    Purpose: Test the fib function with various cases
    Design Idea: Test with base cases and larger natnums
    """
    assert fib(0) == 0, "Test case 0 failed"
    assert fib(1) == 1, "Test case 1 failed"
    assert fib(2) == 1, "Test case 2 failed"
    assert fib(3) == 2, "Test case 3 failed"
    assert fib(4) == 3, "Test case 4 failed"
    assert fib(5) == 5, "Test case 5 failed"
    assert fib(10) == 55, "Test case 6 failed"
    start_time = time.process_time()
    assert fib(40) == 102334155, "Test case 7 failed"
    end_time = time.process_time()
    print(f"fib(40): {end_time - start_time:.4f} seconds")
test_fib()

def fibAcc(k):
    """
    Signature: natnum -> natnum
    Purpose: Returns the nth Fibonacci number using tail recursion
    Design Idea: Use accumulators to store the current Fibonacci number and the previous one.
    """
    def fib_helper(i, fibi, fibi1):
        """
        Signature: natnum, natnum, natnum -> natnum
        Purpose: Compute the ith Fibonacci number
        Design Idea: Inrement i until it equals k, updating the accumulator at each step.
        Accumulator Invariants:
          fibi = ith Fibonacci number
          fibi1 = (i-1)th Fibonacci number
        Assumption: k >= 2
        """
        if i == k:
            return fibi
        else:
            return fib_helper(i+1, fibi+fibi1, fibi)
    if k<2:
        return k
    else:
        return fib_helper(2, 1, 1)

def test_fibAcc():
    """
    Signature: () -> None
    Purpose: Test the fibAcc function with various cases
    Design Idea: Test with base cases and larger natnums
    """
    assert fibAcc(0) == 0, "Test case 0 failed"
    assert fibAcc(1) == 1, "Test case 1 failed"
    assert fibAcc(2) == 1, "Test case 2 failed"
    assert fibAcc(3) == 2, "Test case 3 failed"
    assert fibAcc(4) == 3, "Test case 4 failed"
    assert fibAcc(5) == 5, "Test case 5 failed"
    assert fibAcc(10) == 55, "Test case 6 failed"
    start_time = time.process_time()
    assert fibAcc(40) == 102334155, "Test case 7 failed"
    end_time = time.process_time()
    print(f"fibAcc(40): {end_time - start_time:.4f} seconds")
test_fibAcc()
