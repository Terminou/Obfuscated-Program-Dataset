class Node :	
    def __init__ (O000OOOOOOO0OO0O0 ,OOOO0O0OOO00OOOO0 ):	
       O000OOOOOOO0OO0O0 .data =OOOO0O0OOO00OOOO0 	
       O000OOOOOOO0OO0O0 .next =None 	
class LinkedList :	
    def __init__ (OO0000OO0O000OOOO ):	
        OO0000OO0O000OOOO .head =None 	
        OO0000OO0O000OOOO .last_node =None 	
    def append (OOOO00OOO000000OO ,O0O0OO0OO000OO000 ):	
        if OOOO00OOO000000OO .last_node is None :	
            OOOO00OOO000000OO .head =Node (O0O0OO0OO000OO000 )	
            OOOO00OOO000000OO .last_node =OOOO00OOO000000OO .head 	
        else :	
            OOOO00OOO000000OO .last_node .next =Node (O0O0OO0OO000OO000 )	
            OOOO00OOO000000OO .last_node =OOOO00OOO000000OO .last_node .next 	
    def display (O0O0O0000OO0OO00O ):	
        O000000OO0000OO0O =O0O0O0000OO0OO00O .head 	
        while O000000OO0000OO0O is not None :	
            print (O000000OO0000OO0O .data ,end =' ')	
            O000000OO0000OO0O =O000000OO0000OO0O .next 	
a_llist =LinkedList ()	
n =int (input ('How many elements would you like to add? '))	
for i in range (n ):	
    data =int (input ('Enter data item: '))	
    a_llist .append (data )	
print ('The linked list: ',end ='')	
a_llist .display ()