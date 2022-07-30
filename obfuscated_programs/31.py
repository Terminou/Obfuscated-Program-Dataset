# Python3 program to convert a tree
# into its sum tree
 
# Node definition
class node:
     
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
 
# Convert a given tree to a tree where
# every node contains sum of values of
# nodes in left and right subtrees
# in the original tree
def toSumTree(Node) :
     
    # Base case
    if(Node == None) :
        return 0
 
    # Store the old value
    old_val = Node.data
 
    # Recursively call for left and
    # right subtrees and store the sum as
    # new value of this node
    Node.data = toSumTree(Node.left) + \
                toSumTree(Node.right)
 
    # Return the sum of values of nodes
    # in left and right subtrees and
    # old_value of this node
    return Node.data + old_val
 
# A utility function to print
# inorder traversal of a Binary Tree
def printInorder(Node) :
    if (Node == None) :
        return
    printInorder(Node.left)
    print(Node.data, end = " ")
    printInorder(Node.right)
     
# Utility function to create a new Binary Tree node
def newNode(data) :
    temp = node(0)
    temp.data = data
    temp.left = None
    temp.right = None
     
    return temp