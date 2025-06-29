
def factorial(n):
    """
    Write a function to compute the nth Fibonacci number
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
def test_factorial():
    """
    Test that factorial computes Fibonacci numbers
    """
    assert factorial(0) == 0
    assert factorial(1) == 1
    assert factorial(2) == 1
    assert factorial(3) == 2
    assert factorial(4) == 3
    assert factorial(5) == 5
    assert factorial(6) == 8
    assert factorial(7) == 13
    assert factorial(8) == 21
    assert factorial(9) == 34
    assert factorial(10) == 55

test_factorial()
