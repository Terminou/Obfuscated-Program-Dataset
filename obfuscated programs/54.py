class BinaryTreeNode :	
  def __init__ (OOO00OO0OOOOOO0OO ,O0O0OOOO000OO0OO0 ):	
    OOO00OO0OOOOOO0OO .data =O0O0OOOO000OO0OO0 	
    OOO00OO0OOOOOO0OO .leftChild =None 	
    OOO00OO0OOOOOO0OO .rightChild =None 	
def insert (OO0000000000OO0OO ,OOOO0OOOO00OOO000 ):	
    if OO0000000000OO0OO is None :	
        OO0000000000OO0OO =BinaryTreeNode (OOOO0OOOO00OOO000 )	
        return OO0000000000OO0OO 	
    if OOOO0OOOO00OOO000 <OO0000000000OO0OO .data :	
        OO0000000000OO0OO .leftChild =insert (OO0000000000OO0OO .leftChild ,OOOO0OOOO00OOO000 )	
    else :	
        OO0000000000OO0OO .rightChild =insert (OO0000000000OO0OO .rightChild ,OOOO0OOOO00OOO000 )	
    return OO0000000000OO0OO 	
def postorder (OOOO000O00O0OOOO0 ):	
        if OOOO000O00O0OOOO0 ==None :	
            return 	
        postorder (OOOO000O00O0OOOO0 .leftChild )	
        postorder (OOOO000O00O0OOOO0 .rightChild )	
        print (OOOO000O00O0OOOO0 .data )	
root =insert (None ,15 )	
insert (root ,10 )	
insert (root ,25 )	
insert (root ,6 )	
insert (root ,14 )	
insert (root ,20 )	
insert (root ,60 )	
print ("Printing values of binary tree in postorder Traversal.")	
postorder (root )