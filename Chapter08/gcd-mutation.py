def gcd_helper(larger, smaller, rng):
    """
    Signature : natnum≥1 natnum≥1 range -> natnum≥1
    Purpose : Compute the gcd of a and b
    Design idea : Find gcd by processing rng right to left using a while loop.
    Assumption: larger ≥ smaller
    """
    r = rng
    # INV: rng-r has no divisors of larger and smaller 
    while not(smaller%r[0]==0 and larger%r[0]==0):
        # rng-r has no divisors of larger and smaller and r[0] is not a divisor of both larger and smaller
        r = r[1:]
        # rng-r has no divisors of larger and smaller
    # rng-r has no divisors of both larger and smaller and r[0] is a divisor of both larger and smaller
    return r[0]  

def gcd(a, b):
    """
    Signature : natnum≥1 natnum≥1 -> natnum≥1
    Purpose : Compute the gcd of a and b
    Design idea : Find gcd of a and b in [1..min(a,b)].
    """
    return gcd_helper(max(a, b), min(a, b) ,range (min(a , b ), 0, -1))


def test_gcd():
    """
    Signature : -> None
    Purpose : Test gcd function
    Design idea :   Test with several pairs of numbers that :
                    have and do not have 1 as their gcd
                    have the smaller number as the first argument
                    have the larger number as the first argument
    """

    assert gcd(12,15) == 3 , " Test case 0 failed "
    assert gcd(18,6) == 6 , " Test case 1 failed "
    assert gcd(45,60) == 15 , " Test case 2 failed "
    assert gcd(23,17) == 1 , " Test case 3 failed "
    assert gcd(1,8) == 1 , " Test case 4 failed "
    assert gcd(1,1) == 1 , " Test case 5 failed "
    assert gcd(101135853,45014640) == 177 , \
           "Test case 6 failed "

test_gcd ()


