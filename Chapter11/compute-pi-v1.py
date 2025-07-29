import math
import decimal

dplaces = 50
decimal.getcontext().prec = dplaces
"""
Data Definition
A natural number, natnum, is either:
  1. 0
  2. n+1, where n is a natnum

Template for a function on a natnum

def f_on_natnum(n, ...)
    Signature: natnum ... -> ...
    Purpose: 
    Design Idea:
    if (n == 0):
        return < base case value >
    else :
        return < combine n f_on_natnum (n -1 , ...)

def test_f_on_natnum ():
    Signature: -> None
    Purpose: Test f_on_natnum
    Design idea:
    assert f_on_natnum (0 , ...)==... , " Test 0 failed "
    assert f_on_natnum (1 , ...)==... , " Test 1 failed "
    assert f_on_natnum (2 , ...)==... , " Test 2 failed "
    .
    .
    .
test_f_on_natnum ()
"""

def ChudnovskySeries(f, asum, bsum, k):
    """
    Signature: (natnum -> decimal.Decimal) natnum -> (decimal.Decimal, decimal.Decimal)
    Purpose: Returns the approximations for the A and B series
             for the Chudnovsky algorithm to compute pi
    Design Idea:
      Represent numbers using decimal.Decimal
      Add the terms of the series produced by f
      Use structural recurion on k to compute the sum
      Structure the code using the template for a function on a natnum
      if k is 0 return (asum, bsum)
      else set ak = comupute f(k)
           set prevtuple = recursively process f, asum, bsum, and k-1
           return (asum+(ak*prevtuple[0]), bsum+(prevtuple[1]*ak))
      Accumulator Invariants:
        asum = SUM_{i=0}^{k} A_i
        bsum = SUM_{i=0}^{k} B_i
    """
    if k == 0:
        # asum = A0 and bsum = B0
        return (asum, bsum)
    else:
        ak = f(k)
        prevtuple = ChudnovskySeries(f, asum, bsum, k - 1)
        # asum = SUM_{i=0}^{k-1} A_i AND bsum = SUM_{i=0}^{k-1} B_i
        return (asum + (ak * prevtuple[0]), bsum + (prevtuple[1] * ak))

def computePi(iterations):
    """
    Signature: natnum -> decimal.Decimal
    Purpose: Approximate the value of pi
    Design Idea:
       Represent numbers using decimal.Decimal
       Use the following variables and function:
         numerator = 426880*sqrt(10005)
         afactor = 13591409
         bfactor = 545140134
         f = lambda k: (24 * (6*k - 5) * (2*k - 1) * (6*k - 1))/(640320**3 * k**3)
         AB = ChudnovskySeries(f,1,0,iterations) is the tuple for the
           approximation for A and B of the Chudnovsky series
       return numerator/(afactor*AB[0] + bfactor*AB[1])
    Do not locally define ChudnovskySeries
    """
    numerator = decimal.Decimal(426880) * decimal.Decimal(math.sqrt(10005))
    afactor = decimal.Decimal(13591409)
    bfactor = decimal.Decimal(545140134)
    f = lambda k: (24 * (6*k - 5) * (2*k - 1) * (6*k - 1)) / \
    (decimal.Decimal(640320**3) * decimal.Decimal(k**3))
    AB = ChudnovskySeries(f, \
                          decimal.Decimal(1), \
                          decimal.Decimal(0), \
                          iterations)
    return numerator / (afactor * AB[0] + bfactor * AB[1])

def test_computePi():
    """
    Signature: -> None
    Purpose: Test computePi
    Design Idea:
      Define Pi as a Decimal('3.14159265358979323846264338327950288419716939937510')
      define a tolerance equal to 10**-15
      Use iterations = multiples of 50 in [1, 1000]
      Include fail test strings "Test n failed" where n is the input to computePi.
    """
    Pi = decimal.Decimal('3.14159265358979323846264338327950288419716939937510')
    tolerance = decimal.Decimal(10) ** -10
    for n in range(0, 1000, 50):
        computed_pi = computePi(n)
        assert abs(computed_pi - Pi) < tolerance, f"Test {n} failed"

test_computePi() 

