def calculateLength (O00O0000OOOO00OOO ):	
    O00O0O0O0000OOOO0 =0 ;	
    while (O00O0000OOOO00OOO !=0 ):	
        O00O0O0O0000OOOO0 =O00O0O0O0000OOOO0 +1 ;	
        O00O0000OOOO00OOO =O00O0000OOOO00OOO //10 ;	
    return O00O0O0O0000OOOO0 ;	
def sumOfDigits (OOO0O0OOO00O000O0 ):	
    OOO00OO0OO000OO00 =OOO0OOO00O0O0OOO0 =0 ;	
    O0OOO00OOOOO0000O =calculateLength (OOO0O0OOO00O000O0 );	
    while (OOO0O0OOO00O000O0 >0 ):	
        OOO00OO0OO000OO00 =OOO0O0OOO00O000O0 %10 ;	
        OOO0OOO00O0O0OOO0 =OOO0OOO00O0O0OOO0 +(OOO00OO0OO000OO00 **O0OOO00OOOOO0000O );	
        OOO0O0OOO00O000O0 =OOO0O0OOO00O000O0 //10 ;	
        O0OOO00OOOOO0000O =O0OOO00OOOOO0000O -1 ;	
    return OOO0OOO00O0O0OOO0 ;	
result =0 ;	
print ("Disarium numbers between 1 and 100 are");	
for i in range (1 ,101 ):	
    result =sumOfDigits (i );	
    if (result ==i ):	
        print (i ),