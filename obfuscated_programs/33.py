# Python3 program to find minimum
# sum of two numbers formed from
# all digits in a given array.
from queue import PriorityQueue
 
# Returns sum of two numbers formed
# from all digits in a[]
def solve(a):
     
    # min Heap
    pq = PriorityQueue()
     
    # To store the 2 numbers
    # formed by array elements to
    # minimize the required sum
    num1 = ""
    num2 = ""
 
    # Adding elements in
    # Priority Queue
    for x in a:
        pq.put(x)
 
    # Checking if the priority
    # queue is non empty
    while not pq.empty():
        num1 += str(pq.get())
        if not pq.empty():
            num2 += str(pq.get())   
 
    # The required sum calculated
    sum = int(num1) + int(num2)
     
    return sum
     
# Driver code
if __name__=="__main__":
     
    arr = [ 6, 8, 4, 5, 2, 3 ]
    print("The required sum is ", solve(arr))