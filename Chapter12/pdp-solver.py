
   
def removeFrom(this, that):
   """
   Signature: (listof natnum) (listof natnun) -> (listof natnum)
   Purpose: For each element in this remove an equal element from that
   Assume: For each element in this, there is a corresponding element in that
   Desig Idea:
     Use structural recursion on this
     if this is empty return that
     else recursively process the rest of this and rmX(this[0],that)
   """
   def rmX(elem, lst):
       """
       Signature: natnum (listof natnun) -> (listof natnum)
       Purpose: Remove the first instance of elem from lst
       Assume: There is at least one instance of elem in lst
       Desig Idea:
         Use structural recursion on lst
         if elem equals lst[0] return lst[1:]
         else return [lst[0]] + result of recursively processing elem and the rest of lst
       """
       if (elem == lst[0]):
          return lst[1:]
       else:
          return [lst[0]] + rmX(elem, lst[1:])
   if this == []:
      return that
   else:
      return removeFrom(this[1:], rmX(this[0], that))

def viable(have, needed):
  """
  Signature: (listof natnum) (listof natnum) natnum -> Boolean
  Purpose: Determine if given distance is a viable position
  Design Idea:
    Use structural recursion on a list
    return (needed == []) or ((needed[0] in have) and (viable(have.remove(needed[0]), needed[1:])))
  """
  return not needed or (needed[0] in have and viable(removeFrom([needed[0]], have), needed[1:]))


        
def findPositions(upds, ppos):
  """
  Signature: (listof natnum) (listof natnum) -> (listof natnum)
  Purpose: Find positions for restriction enzymes
  Design Idea:
    if upds is empty return ppos
    pp1 = max of upds
    neededDs1 = differences between pp1 and the elements in ppos
    # try first possibility
    if viable(upds, neededDs1)
      new_upds1 = use removeFrom(neededDs1,upsd)
      psol1 = recursively process new_upds1 and [pp1]+ppos
    if psol1 != None return psol1
    # try second possibility
    pp2 = max(ppos)-pos1
    neededDs2 = differences between pp2 and the elements in ppos
    if viable(upds, neededDs2)
      new_upds2 = use removeFrom(neededDs2,upsd)
      psol2 = recursively process new_upds2 and [pp1]+ppos
    if psol2 != None return psol2 else return None
  """
  if not upds:
     return ppos

  pos1 = max(upds)
  needed1 = [abs(pos1 - p) for p in ppos]

  if viable(upds, needed1):
     new_upds1 = removeFrom(needed1, upds)
     new_ppos1 = [pos1] + ppos
     psol1 = findPositions(new_upds1, new_ppos1)
     if psol1 is not None:
        return psol1

  pos2 = abs(pos1 - max(ppos))
  needed2 = [abs(pos2 - p) for p in ppos]

  if viable(upds, needed2):
     new_upds2 = removeFrom(needed2, upds)
     new_ppos2 = [pos2] + ppos
     psol2 = findPositions(new_upds2, new_ppos2)
     if psol2 is not None:
        return psol2

  return None
  

def pdp_solver(pdigest):
    """
    Signature: (listof natnum) -> (listof natnum) or None
    Purpose: Find possible restriction enzyme positions using the given partial digest
    Assume: pdigest is not empty
    Design Idea:
      Find max in pdigest
      Remove max from pdigest
      Call findPositions with pdigest and [0, max of pdigest] and sort the result if not None
    """
    if not pdigest:
        return None
    max_digest = max(pdigest)
    remaining_digest = pdigest.copy()
    remaining_digest.remove(max_digest)
    positions = findPositions(remaining_digest, [0, max_digest])
    if positions is not None:
        return sorted(positions)
    else:
        return None
    
def test_pdp_solver():
   """
   Signature:  -> None
   Purpose: Test pdp_solver
   Design Idea:
     Generate lists of random natural numbers of 
       lengths 2,3,5,8,10
     Name the lists L3, L3, L5, L8, and L10
     Generate corresponding lists of absolute value of 
       differences between every pair of numbers for each list
     Name these lists PDP3, PDP3, PDP5, PDP8, and PDP10
     Generate a solution using pdp_solver for each PDP list named SOL1, SOL3, SOL5, SOL8, and SOL10
     Generate corresponding lists of absolute value of differences between every pair of numbers for each SOL list
     Use assert statements to that corresponding SOL lists and PDP are equivalent
   """
   import random

   def generate_random_list(length, lower=0, upper=20):
       return sorted(random.sample(range(lower, upper), length))

   def generate_pdp(lst):
       pdp = []
       for i in range(len(lst)):
           for j in range(i + 1, len(lst)):
               pdp.append(abs(lst[j] - lst[i]))
       return sorted(pdp)

   lengths = [2, 3, 5, 8, 10]
   for length in lengths:
       original_list = generate_random_list(length)
       pdp = generate_pdp(original_list)
       solution = pdp_solver(pdp)
       if solution is not None:
           solution_pdp = generate_pdp(solution)
           assert sorted(pdp) == sorted(solution_pdp), f"Test failed for length {length}: {pdp} != {solution_pdp}"
       else:
           print(f"No solution found for PDP: {pdp}")
   print("All tests passed!")

test_pdp_solver()




