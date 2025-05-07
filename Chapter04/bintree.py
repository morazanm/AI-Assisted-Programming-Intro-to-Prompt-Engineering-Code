"""
Data Definitions
A (nodeof X), nodeX, is an object with an X, and two bintreeX.
It offers the following methods:
  1. getx() returns the value of x
  2. getleft() returns the left subtree
  3. getright() returns the right subtree

A (bintreeof X), bintreeX, is either:
  1. None
  2. nodeX

Template for a function on a nodeX:
    def f_on_node(nd ...):
        Signature: nodeX ... -> ...
        Purpose:
        Design Idea:
        return <combine f_on_x(nd.getx())
                        f_on_bintreeof_X(nd.getleft())
                        f_on_bintreeof_X(nd.getright())>

Template for a function on a bintreeX:
    def f_on_bintreeof_X(bt ...):
        Signature: bintreeX ... -> ...
        Purpose:
        Design Idea:
        if bt == None:
            return <base case value>
        else:
            return f_on_node(bt)
"""
class Node:
    def __init__(self, x, left, right):
        self.x = x
        self.left = left
        self.right = right

    def getx(self):
        return self.x
    
    def getleft(self):
        return self.left
    
    def getright(self):
        return self.right
    
def test_node():
    """
    Signature: () -> None
    Purpose: Test the Node class.
    Design Idea: Create several nodes and test its methods.
    """
    # leafs at level 2
    leaf1 = Node(1, None, None)
    leaf2 = Node(2, None, None)
    leaf3 = Node(3, None, None)
    leaf4 = Node(4, None, None)
    # interior nodes at level 1
    intn5 = Node(5, leaf1, leaf2)
    intn6 = Node(6, leaf3, leaf4)
    # root interior node at level 0
    rootn = Node(7, intn5, intn6)
    assert leaf1.getx() == 1, "Test 0 failed"
    assert leaf1.getleft() == None, "Test 1 failed"
    assert leaf1.getright() == None, "Test 2 failed"
    assert rootn.getx() == 7, "Test 3 failed"
    assert rootn.getleft() == intn5, "Test 4 failed"
    assert rootn.getright() == intn6, "Test 5 failed"
    assert rootn.getleft().getx() == 5, "Test 6 failed"
    assert rootn.getleft().getleft() == leaf1, "Test 7 failed"
    assert rootn.getleft().getright() == leaf2, "Test 8 failed"
    assert rootn.getright().getx() == 6, "Test 9 failed"
    assert rootn.getright().getleft() == leaf3, "Test 10 failed"

test_node()



def nodeContains(x, n):
    """
    Signature: X nodex -> bool
    Purpose: returns True if n contains x, False otherwise.
    Design Idea: Return True if x is equal to node value or x is in one of the subtrees.
    """
    return n.getx() == x or \
           bintreeContains(x, n.getleft()) or \
           bintreeContains(x, n.getright())

def bintreeContains(x, bt):
    """
    Signature: X bintreex -> bool
    Purpose: returns True if bt contains x, False otherwise.
    Design Idea: Return True if bt is not None and either x is equal to the value of bt or x is in one of the subtrees.
    """
    return bt != None and nodeContains(x, bt)

def test_bintreeContains():
    """
    Signature: () -> None
    Purpose: Test the bintreeContains function.
    Design Idea: Create empty and nonempty bintrees and test searching for different values.
    """
    # Test empty bintree
    assert bintreeContains(1, None) == False, "Test 1 failed"
    # Test nonempty bintree
    bt = Node(1, Node(2, None, None), Node(3, None, None))
    assert bintreeContains(1, bt) == True, "Test 2 failed"
    assert bintreeContains(2, bt) == True, "Test 3 failed"
    assert bintreeContains(3, bt) == True, "Test 4 failed"
    assert bintreeContains(4, bt) == False, "Test 5 failed"
    # Test nested bintrees
    bt2 = Node(4, Node(5, None, None), Node(6, None, None))
    bt3 = Node(7, bt, bt2)
    assert bintreeContains(2, bt3) == True, "Test 6 failed"
    assert bintreeContains(4, bt3) == True, "Test 7 failed" 
    assert bintreeContains(31, bt3) == False, "Test 8 failed"
    assert bintreeContains(-3, bt2) == False, "Test 9 failed"
    assert bintreeContains(-3, bt3) == False, "Test 10 failed"

test_bintreeContains()




    
