global maximum 
def _O0O0O00OOOO0OOOO0 (O00O0000OOO00OO00 ,OOOOOO00OOOO0O0OO ):
    global maximum 
    if OOOOOO00OOOO0O0OO ==1 :
        return 1 
    OO0000OO00O000OOO =1 

    for OO0OOOO0OO000000O in range (1 ,OOOOOO00OOOO0O0OO ):
        OOO000O00OOO00OO0 =_O0O0O00OOOO0OOOO0 (O00O0000OOO00OO00 ,OO0OOOO0OO000000O )
        if O00O0000OOO00OO00 [OO0OOOO0OO000000O -1 ]<O00O0000OOO00OO00 [OOOOOO00OOOO0O0OO -1 ]and OOO000O00OOO00OO0 +1 >OO0000OO00O000OOO :
            OO0000OO00O000OOO =OOO000O00OOO00OO0 +1 
    maximum =max (maximum ,OO0000OO00O000OOO )
    return OO0000OO00O000OOO 
def lis (OOOOO00OOOO0O0O00 ):
    global maximum 
    O0O00000OOO0OOO00 =len (OOOOO00OOOO0O0O00 )
    maximum =1 
    _O0O0O00OOOO0OOOO0 (OOOOO00OOOO0O0O00 ,O0O00000OOO0OOO00 )
    return maximum 
arr =[10 ,22 ,9 ,33 ,21 ,50 ,41 ,60 ]
n =len (arr )
print ("Length of lis is ",lis (arr ))