def Fibonacci_Series (OOOO0O00O0000OO00 ):	
    if OOOO0O00O0000OO00 <0 :	
        print ("Oops!")	
    elif OOOO0O00O0000OO00 ==0 :	
        return (0 )	
    elif OOOO0O00O0000OO00 ==1 :	
        return (1 )	
    else :	
        return (Fibonacci_Series (OOOO0O00O0000OO00 -1 )+Fibonacci_Series (OOOO0O00O0000OO00 -2 ))	
print ("Result: ",Fibonacci_Series (12 ))