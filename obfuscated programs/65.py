import collections 	
class Node :	
   def __init__ (O0O0O0O000O00000O ,O0OOOOOOOOOOOO0OO ):	
      O0O0O0O000O00000O .left =None 	
      O0O0O0O000O00000O .right =None 	
      O0O0O0O000O00000O .data =O0OOOOOOOOOOOO0OO 	
   def PrintTree (O0O000O00OOOOO0OO ):	
       if O0O000O00OOOOO0OO .left :	
           O0O000O00OOOOO0OO .left .PrintTree ()	
       print (O0O000O00OOOOO0OO .data ,end =' '),	
       if O0O000O00OOOOO0OO .right :	
           O0O000O00OOOOO0OO .right .PrintTree ()	
class Solution :	
    ""	
    def invertTree (O0000OOOOO0OO00OO ,OOO00O000O00O000O ):	
        if not OOO00O000O00O000O :	
            return OOO00O000O00O000O 	
        OOOO0000OOOOOO00O =collections .deque ()	
        OOOO0000OOOOOO00O .append (OOO00O000O00O000O )	
        while len (OOOO0000OOOOOO00O ):	
            OOOO00OOO000OOO0O =OOOO0000OOOOOO00O .popleft ()	
            OOOO00OOO000OOO0O .left ,OOOO00OOO000OOO0O .right =OOOO00OOO000OOO0O .right ,OOOO00OOO000OOO0O .left 	
            if OOOO00OOO000OOO0O .left is not None :	
                OOOO0000OOOOOO00O .append (OOOO00OOO000OOO0O .left )	
            if OOOO00OOO000OOO0O .right is not None :	
                OOOO0000OOOOOO00O .append (OOOO00OOO000OOO0O .right )	
        return OOO00O000O00O000O 	
if __name__ =='__main__':	
    '''
                10                                              10
              /    \                                          /    \           
            20      30              ========>>              30      20           
           /         \                                      /        \
          40          50                                  50          40 
    '''	
    Tree =Node (10 )	
    Tree .left =Node (20 )	
    Tree .right =Node (30 )	
    Tree .left .left =Node (40 )	
    Tree .right .right =Node (50 )	
    print ('Initial Tree :',end =' ')	
    Tree .PrintTree ()	
    Solution ().invertTree (root =Tree )	
    print ('\nInverted Tree :',end =' ')	
    Tree .PrintTree ()