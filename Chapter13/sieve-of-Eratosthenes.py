def findPrimes(n):
    """
    Signature: natnum -> (listof natnum)
    Purpose: Find the primes less than or equal to the given natnum
    Design Idea:
      Do not locally define sieve 
      Return the call to sieve with the list of integers in [2..n] and the empty list
    """
    def sieve(lst, acc):
        """
        Signature: (listof natnum) (listof natnum) -> (listof natnum)
        Purpose: Sieve the primes from lst, accumulating them in acc
        Accumulator Invariant:
          acc = if lst is empty list of all primes <= n 
                else list of all primes <= lst[0] <= n
        Design Idea:
          If lst is empty return acc
          else return the result of recursively processing lst without the multiples of the first element and the first of lst added to acc
        """
        if not lst:
            return acc
        else:
            # Sieve out multiples of the first element
            first = lst[0]
            rest = [x for x in lst if x % first != 0]
            return sieve(rest, acc + [first])
    return sieve(list(range(2, n + 1)), [])

def test_findPrimes():
    """
    Signature:  -> None
    Purpose: Test the findPrimes function
    Design Idea:
      Test using various random natnums greater than 1
      For each random natnum, create a list of expected primes
      Use assert to validate findPrimes
      Include failed test strings: "Test n failed" starting with n = 0
    """
    test_cases = [
        (10, [2, 3, 5, 7]),
        (20, [2, 3, 5, 7, 11, 13, 17, 19]),
        (30, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]),
        (50, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]),
        (1, []), # Edge case: no primes less than or equal to 1
        (2, [2]), # Edge case: only prime is 2
    ]
    for i, (n, expected) in enumerate(test_cases):
        result = findPrimes(n)
        assert result == expected, f"Test {i} failed: expected {expected}, got {result}"

test_findPrimes()
