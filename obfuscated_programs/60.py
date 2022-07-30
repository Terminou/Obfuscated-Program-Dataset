class Node :	
    def __init__ (OOOOO0O00OO0O000O ,OO00O0O0O0O0OO0OO ):	
        OOOOO0O00OO0O000O .data =OO00O0O0O0O0OO0OO ;	
        OOOOO0O00OO0O000O .previous =None ;	
        OOOOO0O00OO0O000O .next =None ;	
class MinMax :	
    def __init__ (O000000OO00OOO0O0 ):	
        O000000OO00OOO0O0 .head =None ;	
        O000000OO00OOO0O0 .tail =None ;	
    def addNode (OO0OO00O0OO0OO000 ,O000OOO00OOOO00OO ):	
        OO0000O00OOO0O0OO =Node (O000OOO00OOOO00OO );	
        if (OO0OO00O0OO0OO000 .head ==None ):	
            OO0OO00O0OO0OO000 .head =OO0OO00O0OO0OO000 .tail =OO0000O00OOO0O0OO ;	
            OO0OO00O0OO0OO000 .head .previous =None ;	
            OO0OO00O0OO0OO000 .tail .next =None ;	
        else :	
            OO0OO00O0OO0OO000 .tail .next =OO0000O00OOO0O0OO ;	
            OO0000O00OOO0O0OO .previous =OO0OO00O0OO0OO000 .tail ;	
            OO0OO00O0OO0OO000 .tail =OO0000O00OOO0O0OO ;	
            OO0OO00O0OO0OO000 .tail .next =None ;	
    def minimumNode (O0OO00000OO00O0O0 ):	
        OOO00O000OO0OO00O =O0OO00000OO00O0O0 .head ;	
        if (O0OO00000OO00O0O0 .head ==None ):	
            print ("List is empty");	
            return 0 ;	
        else :	
            O00OOOO0OOOO000OO =O0OO00000OO00O0O0 .head .data ;	
            while (OOO00O000OO0OO00O !=None ):	
                if (O00OOOO0OOOO000OO >OOO00O000OO0OO00O .data ):	
                    O00OOOO0OOOO000OO =OOO00O000OO0OO00O .data ;	
                OOO00O000OO0OO00O =OOO00O000OO0OO00O .next ;	
        return O00OOOO0OOOO000OO ;	
    def maximumNode (O00O0OO0OOO0000O0 ):	
        OOOO0OOOOO0O0OO0O =O00O0OO0OOO0000O0 .head ;	
        if (O00O0OO0OOO0000O0 .head ==None ):	
            print ("List is empty");	
            return 0 ;	
        else :	
            O0O0O0O00OOO0OOOO =O00O0OO0OOO0000O0 .head .data ;	
            while (OOOO0OOOOO0O0OO0O !=None ):	
                if (OOOO0OOOOO0O0OO0O .data >O0O0O0O00OOO0OOOO ):	
                    O0O0O0O00OOO0OOOO =OOOO0OOOOO0O0OO0O .data ;	
                OOOO0OOOOO0O0OO0O =OOOO0OOOOO0O0OO0O .next ;	
        return O0O0O0O00OOO0OOOO ;	
dList =MinMax ();	
dList .addNode (5 );	
dList .addNode (7 );	
dList .addNode (9 );	
dList .addNode (1 );	
dList .addNode (2 );	
print ("Minimum value node in the list: "+str (dList .minimumNode ()));	
print ("Maximum value node in the list: "+str (dList .maximumNode ()));