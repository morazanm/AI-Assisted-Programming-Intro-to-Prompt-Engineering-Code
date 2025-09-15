"""
A bucket is an interface that offers the following 
services:
- bucket: Signature: natnum -> bucket
          Purpose:builds an empty bucket of the given size
          Design Idea:
            size = the given number
            numElems = 0
            data = a list with size Nones
- add: Signature: number -> None
       Purpose:adds a given number to the end of the 
               bucket. This is an in-place operation
       Assume: data is not full
       Effect: the bucket contains the given number as the
               last added number in data
        Design Idea:
         data[numElems] = number
         Increase numElems by 1
- dump: Signature: (listof number) natnum -> None
        Purpose: mutates the given list to contain the 
                 numbers in the bucket. The bucket numbers
                 are placed in the list starting at the 
                 given index. When a bucket number is 
                 copied to the given list, it is mutated
                 to be None.
                 This is an in-place operation
        Assume: The bucket elements fit in the given list 
                starting at the given index
        Effect: the given list contains the bucket's 
                numbers starting at the given index and
                the bucket is empty.
        Design Idea:
          For each element in the bucket's data 
          up to numElems-1:
            Copy the element to the given list at the  
              current index
            Mutate the bucket's element to be None
            Increment the index
          Make the number of elements in the bucket 0
Implement a bucket class.  
Include a signature, a purpose statement, and a design  
  idea for each method as comments  under the method's 
  header.
"""
class Bucket:
  def __init__(self, size):
    """
    Signature: natnum -> bucket
    Purpose: builds an empty bucket of the given size
    Design Idea:
      size = the given number
      numElems = 0
      data = a list with size Nones
    """
    self.size = size
    self.numElems = 0
    self.data = [None] * size

  def add(self, number):
    """
    Signature: number -> None
    Purpose: adds a given number to the end of the 
             bucket. This is an in-place operation
    Assume: data is not full
    Effect: the bucket contains the given number as the
            last added number in data and the number of
            elements is increased by 1
    Design Idea:
      data[numElems] = number
      Increase numElems by 1
    """
    self.data[self.numElems] = number
    self.numElems += 1

  def dump(self, lst, index):
        """
        Signature: (listof number) natnum -> None
        Purpose: mutates the given list to contain the 
                numbers in the bucket. The bucket numbers
                are placed in the list starting at the 
                given index. When a bucket number is 
                copied to the given list, it is mutated
                to be None.
                This is an in-place operation
        Assume: The bucket elements fit in the given list 
                starting at the given index
        Effect: the bucket's numbers are copied to the
                    given list starting at the given index and
                    the bucket is emptied.
        Design Idea:
          For each element in the bucket's data 
          up to numElems-1:
            Copy the element to the given list at the  
              current index
            Mutate the bucket's element to be None
            Increment the index
          Make the number of elements in the bucket 0
        """
        """
        Preconditions:
          - self.data[0:numElems] = [N0, N1, ..., N_{numElems-1}]
          - lst is a list with length at least index + numElems
        Loop invariant at the start of iteration i (0 ≤ i ≤ numElems):
          - data[0:i) = [None, ..., None] (the first i-1 elements have been copied and set to None)
          - data[i:numElems) = [N_i, ..., N_{numElems-1}] (the remaining elements to be copied)
          - lst[index : index + i) = [N0, ..., N_{i-1}] (the first i-1 elements have been copied to lst)
          - lst[index + i :] is unchanged
        At the start of iteration i:
          - data[i] = N_i (not yet copied)
          - lst[index + i] is unchanged
        After the body of iteration i:
          - data[0:i+1) = [None, ..., None]
          - data[i+1:numElems) = [N_{i+1}, ..., N_{numElems-1}]
          - lst[index : index + i + 1) = [N0, ..., N_i]
        After the loop (i = numElems):
          - data[0:numElems) = [None, ..., None]
          - lst[index : index + numElems) = [N0, N1, ..., N_{numElems-1}]
        """
        for i in range(self.numElems):
          # At the start of iteration i:
          #   data[0:i) = [None, ..., None]
          #   data[i] = N_i
          #   data[i+1:numElems) = [N_{i+1}, ..., N_{numElems-1}]
          #   lst[index : index + i) = [N0, ..., N_{i-1}]
          #   lst[index + i] is unchanged
          lst[index] = self.data[i]
          self.data[i] = None
          index += 1
          # After iteration i:
          #   data[0:i+1) = [None, ..., None]
          #   data[i+1:numElems) = [N_{i+1}, ..., N_{numElems-1}]
          #   lst[index : index + i + 1) = [N0, ..., N_i]
        # After the loop (i = numElems):
        #   data[0:numElems) = [None, ..., None]
        #   lst[index : index + numElems) = [N0, N1, ..., N_{numElems-1}]
        self.numElems = 0

def debucketize(lst,buckets):
  """
  Signature: (listof natnum) (listof bucket) -> None
  Purpose: Collect the numbers from the buckets back 
           into the list in order.
  Effect: The list elements are mutated to contain
          all the numbers from the buckets in order.
  Assume: The list is large enough to hold all
          the numbers in the buckets.
          buckets[i]_init = [Ni0,Ni1,...,Nim],
          where each Nij is a positive integer and
          all other bucket values are None.
  Design Idea:
    lst_index = 0
    For each bucket from 0 to 9:
      blen = number of elements in the bucket
      Call dump on the bucket to place its numbers 
        into lst starting at the current index.
      Update the index by adding blen.
    Loop invariant:
      lst[0:lst_index-1]= bucket[0]_init + ... + bucket[k-1]_init, 
        where k is the index of the next bucket to process
    Design the loop to maintain the loop invariant.
    Include Hoare Logic assertion to show the loop 
      invariant holds
  """
  # Hoare Logic assertion (before loop):
  # { lst[0:lst_index-1] = [] }
  lst_index = 0
  for bucket in buckets:
    # Hoare Logic assertion (at loop head):
    # { lst[0:lst_index-1] = bucket[0]_init + ... + bucket[k-1]_init }
    blen = bucket.numElems
    bucket.dump(lst, lst_index)
    lst_index += blen
    # Hoare Logic assertion (after iteration):
    # { lst[0:lst_index-1] = bucket[0]_init + ... + bucket[k]_init }
  # Hoare Logic assertion (after loop):
  # { lst[0:lst_index-1] = bucket[0]_init + ... + bucket[9]_init }

def test_debucketize():
  """
  Signature:  -> None
  Purpose:  Test the debucketize function
  Design Idea:
   Generate 3 lists of positive integers: lst1, lst2, and lst3
   Based on the largest number in each generated list, generate a random digit positions: k1, k2, k3
   slst1, slst2, slst3 = lst1,lst2,lst3 sorted by k1,k2,k3 least significant digit
   Add the elements of lst1, lst2, and lst3 to different lists of buckets: buckets1, buckets2, and buckets3
   For lst1, lst2, and lst3 and buckets1, buckets2, and buckets2:
      Call debucketize with a list and the corresponding list of buckets
      Use an assert-statement to validate that list equals 
        the corresponding slist
  """
  import random

  lst1 = [170, 45, 75, 90, 802, 24, 2, 66]
  k1 = random.randint(0, 2)  # max number is 802 which has 3 digits
  dlist1 = sorted(lst1, key=lambda x: (x // (10 ** k1)) % 10)

  lst2 = [3, 6, 9, 12, 15, 18, 21]
  k2 = random.randint(0, 1)  # max number is 21 which has 2 digits
  dlist2 = sorted(lst2, key=lambda x: (x // (10 ** k2)) % 10)

  lst3 = [1234, 5678, 91011, 1213, 1415]
  k3 = random.randint(0, 4)  # max number is 91011 which has 5 digits
  dlist3 = sorted(lst3, key=lambda x: (x // (10 ** k3)) % 10)

  buckets1 = [Bucket(len(lst1)) for _ in range(10)]
  for number in lst1:
      digit = (number // (10 ** k1)) % 10
      buckets1[digit].add(number)
  
  buckets2 = [Bucket(len(lst2)) for _ in range(10)]
  for number in lst2:
      digit = (number // (10 ** k2)) % 10
      buckets2[digit].add(number)

  buckets3 = [Bucket(len(lst3)) for _ in range(10)]
  for number in lst3:
      digit = (number // (10 ** k3)) % 10
      buckets3[digit].add(number)

  debucketize(lst1, buckets1)
  assert lst1 == dlist1, f"Test failed for lst1 with k={k1}"

  debucketize(lst2, buckets2)
  assert lst2 == dlist2, f"Test failed for lst2 with k={k2}"

  debucketize(lst3, buckets3)
  assert lst3 == dlist3, f"Test failed for lst3 with k={k3}"

test_debucketize()

def bucketize(lst, buckets, k):
    """
    Signature: (listof positive-int) (listof bucket) natnum -> None
    Purpose: Place each number in lst into the appropriate bucket based on its k-th least significant digit
    Effect: The buckets are mutated to contain the numbers from lst maintaining their relative order in the buckets
    Design Idea:
      For each number in lst:
        Determine the k-th least significant digit
        Place the number in the corresponding bucket
    Loop invariant:
      buckets[i] = all processed numbers in lst whose k-th least significant digit is i in the same order as they appear in lst
    Design the loop to maintain the loop invariant
    Write Hoare Logic assertion to show the loop invariant holds
    """
    # Hoare Logic assertion (before loop):
    # { For all i in 0..9, buckets[i] contains all processed numbers in lst whose k-th least significant digit is i, in order }
    for number in lst:
      # Hoare Logic assertion (at loop head):
      # { For all i in 0..9, buckets[i] contains all numbers in lst[0:p] whose k-th least significant digit is i, in order }
      digit = (number // (10 ** k)) % 10
      buckets[digit].add(number)
      # Hoare Logic assertion (after iteration):
      # { For all i in 0..9, buckets[i] contains all numbers in lst[0:p+1] whose k-th least significant digit is i, in order }
      # where p is the current index in lst
    # Hoare Logic assertion (after loop):
    # { For all i in 0..9, buckets[i] contains all numbers in lst whose k-th least significant digit is i, in order }

def test_bucketize():
    """
    Signature:  -> None
    Purpose: Test the bucketize function
    Design Idea:
      Create several lists of positive integers of 
        different lengths and digit counts.
      Compute a random natural number, k, for each list that is less that or equal to the length of the max number in the list
      For each list and correspondng random number, create an expected list of 10 buckets, where each numbber in the list is placed in the bucket corresponding to its k-th least significant digit
      For each list of positive integers:
        Place the positive ints in the buckets using 
          the digit at the random number position
        Compute an expected list of buckets
        Compute the actual list of buckets by removing the None values from each bucket's data
        Use an assert-statement to validate that the 
          actual list of buckets equals the expected 
          list of buckets
    """
    import random

    lst1 = [170, 45, 75, 90, 802, 24, 2, 66]
    k1 = random.randint(0, 2)  # max number is 802 which has 3 digits
    expected_buckets1 = [[] for _ in range(10)]
    for number in lst1:
        digit = (number // (10 ** k1)) % 10
        expected_buckets1[digit].append(number)

    lst2 = [3, 6, 9, 12, 15, 18, 21]
    k2 = random.randint(0, 1)  # max number is 21 which has 2 digits
    expected_buckets2 = [[] for _ in range(10)]
    for number in lst2:
        digit = (number // (10 ** k2)) % 10
        expected_buckets2[digit].append(number)

    lst3 = [1234, 5678, 91011, 1213, 1415]
    k3 = random.randint(0, 4)  # max number is 91011 which has 5 digits
    expected_buckets3 = [[] for _ in range(10)]
    for number in lst3:
        digit = (number // (10 ** k3)) % 10
        expected_buckets3[digit].append(number)

    buckets1 = [Bucket(len(lst1)) for _ in range(10)]
    bucketize(lst1, buckets1, k1)
    actual_buckets1 = [bucket.data[:bucket.numElems] for bucket in buckets1]
    assert actual_buckets1 == expected_buckets1, f"Test failed for lst1 with k={k1}"

    buckets2 = [Bucket(len(lst2)) for _ in range(10)]
    bucketize(lst2, buckets2, k2)
    actual_buckets2 = [bucket.data[:bucket.numElems] for bucket in buckets2]
    assert actual_buckets2 == expected_buckets2, f"Test failed for lst2 with k={k2}"

    buckets3 = [Bucket(len(lst3)) for _ in range(10)]
    bucketize(lst3, buckets3, k3)
    actual_buckets3 = [bucket.data[:bucket.numElems] for bucket in buckets3]
    assert actual_buckets3 == expected_buckets3, f"Test failed for lst3 with k={k3}"

test_bucketize()

def radixSort(lst):
    """
    Signature: (listof postive-int) -> None
    Purpose: Sort the given list in-place
    Effect: The list elements are placed in non-decreasing 
            order
    Design Idea:
      iters = length of the largest number in lst
      Create 10 buckets for the digits 0-9
      let k iterate over [0..iters-1]
        Call bucketize with lst, buckets, and k to places 
          digits in buckets
        Call debucketize with lst and buckets to place 
          numbers back into lst
    Loop invariant:
      For all i < j, 
       if digits_k(L[i]) < digits_k(L[j]), then i < j
      where:
       digits_k(n) = the k least significant digits of n
    Design the loop to maintain the loop invariant
    Include Hoare Logic assertion to show the loop  
      invariant holds
    Do not locally define bucketize and debucketize
    """
    iters = max(len(str(x)) for x in lst)
    buckets = [Bucket(len(lst)) for _ in range(10)]

    for k in range(iters):
        bucketize(lst, buckets, k)
        debucketize(lst, buckets)

def test_radixSort():
    """
    Signature:  -> None
    Purpose:  Test the radixSort function
    Design Idea:
      Create several lists of positive integers of 
        different lengths and digit counts.
      For each list:
        Create a sorted version of the list using Python's 
          built-in sort
        Call radixSort on the list
        Use an assert-statement to validate that the 
          sorted list equals the list sorted with Python's 
          built-in sort
    """
    lst1 = [170, 45, 75, 90, 802, 24, 2, 66]
    expected1 = sorted(lst1)
    radixSort(lst1)
    assert lst1 == expected1, f"Test failed for lst1"

    lst2 = [3, 6, 9, 12, 15, 18, 21]
    expected2 = sorted(lst2)
    radixSort(lst2)
    assert lst2 == expected2, f"Test failed for lst2"

    lst3 = [1234, 5678, 91011, 1213, 1415]
    expected3 = sorted(lst3)
    radixSort(lst3)
    assert lst3 == expected3, f"Test failed for lst3"

test_radixSort()
