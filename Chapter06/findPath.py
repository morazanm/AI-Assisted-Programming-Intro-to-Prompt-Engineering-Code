"""
A node name, nn, is a string of length 1

A node is a tuple, (nn, (listof nn)), with a node name and a list of node names for its neighbors.

A graph is a list of nodes with no duplicates.

A path is a (listof nn).
"""



def findPath(grph, start, end):
    """
    Signature: graph nn nn -> path
    Purpose: Find a path from start to end in the graph.
    Design Idea: Find a path from start to end through any neighbor of start.
    """

    def getNode(name):
        """
        Signature: nn -> node
        Purpose: Find the node with the given name in the grph.
        Design Idea: Iterate through the grph to find the node with the matching name.
        Assumption: graph contains a node with the given name.
        """
        for node in grph:
            if node[0] == name:
                return node
            
    def findPathFromAny(neighs):
        """
        Signature: (listof nn) -> path
        Purpose: Find a path from start to end through any neighbor in neighs.
        Design Idea: If the solution is not trivial, try
                 to find a path from the first node
                 name in neighs. If successful, return
                 this path. Otherwise, recursively
                 try to find a path from any other
                 node name in neighs. If unsuccessful,
                 return the empty path. Otherwise,
                 return the found path.
        """
        if neighs == []:
            return []
        elif neighs[0] == end:
            return [end]
        else:
            possiblePath = findPathHelper(getNode(neighs[0]))
            if possiblePath != []:
                return possiblePath
            else:
                return findPathFromAny(neighs[1:])
    
    def findPathHelper(aNode):
        """
        Signature: node -> path
        Purpose: Find a path to end from any neighbor of aNode.
        Design Idea: Try to find a path from aNode to end.  
                     If successful, add aNodes's name to 
                     the front of the path. Otherwise, return 
                     the empty path.
        """
        if aNode[0] == end:
            return [aNode[0]]
        else:
            possiblePath = findPathFromAny(aNode[1])
            if possiblePath == []:
                return []
            else:
                return [aNode[0]] + findPathFromAny(aNode[1])
        
    if start == end:
        return [start]
    else:
        return findPathHelper(getNode(start[0]))
    """
     Termination argument: 
      The accumulator is exploited to prevent
      revisiting any nodes. Therefore, the 
      program never gets caught repeatedly
      exploring nodes in a cycle and always
      terminates.
    """

def test_findPath():
    """
    Signature: () -> None
    Purpose: Test the findPath function.
    Design Idea: Use several graphs to test the function.
    """
    graph = [('a', ['b', 'd', 'f']),
             ('b', ['c']),
             ('c', ['a']),
             ('d', ['e']),
             ('e', ['d']),
             ('f', [])]
    
    assert findPath(graph, 'f', 'a') == [], "Test case 0 failed"
    assert findPath(graph, 'f', 'f') == ['f'], "Test case 1 failed"
    assert findPath(graph, 'c', 'a') == ['c', 'a'], "Test case 2 failed"
    assert findPath(graph, 'a', 'c') == ['a', 'b', 'c'], "Test case 3 failed"
    #assert findPath(graph, 'b', 'e') == ['b', 'c', 'a', 'd', 'e'], "Test case 4 failed"
    #assert findPath(graph, 'b', 'f') == ['b', 'c', 'a', 'f'], "Test case 5 failed"

test_findPath()


def findPath2(grph, start, end):
    """
    Signature: graph nn nn -> path
    Purpose: Find a path from start to end in the graph.
    Design Idea: Find a path from start to end through any neighbor of start.
                 Initially, no nodes are visited.
    """

    def getNode(name):
        """
        Signature: nn -> node
        Purpose: Find the node with the given name in the grph.
        Design Idea: Iterate through the grph to find the node with the matching name.
        Assumption: graph contains a node with the given name.
        """
        for node in grph:
            if node[0] == name:
                return node

    def findPathFromAny(neighs, visited):
        """
        Signature: (listof nn) (listof nn) -> path
        Purpose: Find a pathe from any given neighbor to end.
        Design Idea: Try to find a path from the first unexplored neighbor of neighs.
                     If successful, add the neighbor's name to the front of the path.
                     Otherwise, try the next unexplored neighbor
        Accumulator Invariant:
          visited = the list of node names that have been visited so far
        """
        if neighs == []:
            return []
        elif neighs[0] == end:
            return [neighs[0]]
        else:
            if neighs[0] in visited:
                return findPathFromAny(neighs[1:], visited)
            else:
                possiblePath = findPathHelper(getNode(neighs[0]), visited)
                if possiblePath != []:
                    return possiblePath
                else:
                    return findPathFromAny(neighs[1:], visited + [neighs[0]])

    def findPathHelper(aNode, visited):
        """
        Signature: node (listof nn) -> path
        Purpose: Find a path to end from any neighbor of aNode.
        Deign Idea: Try to find a path from the first unexplored neighbor of aNode.
                    If successful, add aNodes's name to the front of the path.
                    Otherwise, try the next unexplored neighbor
        Accumulator Invariant:
          visited = the list of node names that have been visited so far
        """
        if aNode[0] == end:
            return [aNode[0]]
        else:
            possiblePath = findPathFromAny(aNode[1],visited + [aNode[0]])
            if possiblePath == []:
                return []
            else:
                return [aNode[0]] + possiblePath
    return findPathHelper(getNode(start), [])

def test_findPath2():
    """
    Signature: () -> None
    Purpose: Test the findPath function.
    Design Idea: Use several graphs to test the function.
    """
    graph = [('a', ['b', 'd', 'f']),
             ('b', ['c']),
             ('c', ['a']),
             ('d', ['e']),
             ('e', ['d']),
             ('f', [])]
    
    assert findPath2(graph, 'f', 'a') == [], "Test case 0 failed"
    assert findPath2(graph, 'f', 'f') == ['f'], "Test case 1 failed"
    assert findPath2(graph, 'c', 'a') == ['c', 'a'], "Test case 2 failed"
    assert findPath2(graph, 'a', 'c') == ['a', 'b', 'c'], "Test case 3 failed"
    assert findPath2(graph, 'b', 'e') == ['b', 'c', 'a', 'd', 'e'], "Test case 4 failed"
    assert findPath2(graph, 'b', 'f') == ['b', 'c', 'a', 'f'], "Test case 5 failed"

test_findPath2()

