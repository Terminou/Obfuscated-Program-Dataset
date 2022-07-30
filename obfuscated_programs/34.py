# Python3 program to find minimum number of
# steps needed to convert a number x into y
# with two operations allowed :
# (1) multiplication with 2
# (2) subtraction with 1.
import queue
 
# A node of BFS traversal
 
 
class node:
    def __init__(self, val, level):
        self.val = val
        self.level = level
 
# Returns minimum number of operations
# needed to convert x into y using BFS
 
 
def minOperations(x, y):
 
    # To keep track of visited numbers
    # in BFS.
    visit = set()
 
    # Create a queue and enqueue x into it.
    q = queue.Queue()
    n = node(x, 0)
    q.put(n)
 
    # Do BFS starting from x
    while (not q.empty()):
 
        # Remove an item from queue
        t = q.get()
 
        # If the removed item is target
        # number y, return its level
        if (t.val == y):
            return t.level
 
        # Mark dequeued number as visited
        visit.add(t.val)
 
        # If we can reach y in one more step
        if (t.val * 2 == y or t.val - 1 == y):
            return t.level+1
 
        # Insert children of t if not visited
        # already
        if (t.val * 2 not in visit):
            n.val = t.val * 2
            n.level = t.level + 1
            q.put(n)
        if (t.val - 1 >= 0 and t.val - 1 not in visit):
            n.val = t.val - 1
            n.level = t.level + 1
            q.put(n)
 
 
# Driver code
if __name__ == '__main__':
 
    x = 4
    y = 7
    print(minOperations(x, y))