import queue 
class Graph :
    def __init__ (O00O00O0OOOOO000O ,O0000000OO00OOO00 ):
        O00O00O0OOOOO000O .V =O0000000OO00OOO00 ;
        O00O00O0OOOOO000O .l =[[]for O0000O00000OO0O0O in range (O0000000OO00OOO00 )]
    def addedge (OOO000OOO0O0O00O0 ,O00O0OO0OOOOO0OO0 ,O000OO0O00OO00000 ):
        OOO000OOO0O0O00O0 .l [O00O0OO0OOOOO0OO0 ].append (O000OO0O00OO00000 );
        OOO000OOO0O0O00O0 .l [O000OO0O00OO00000 ].append (O00O0OO0OOOOO0OO0 );
    def bfs (O0O0OO00O00OO00O0 ,O0O0000OOO00OOOO0 ,OOOO00000O00OOOOO ):
        O000OO0OO0OOOOO0O =[0 ]*O0O0OO00O00OO00O0 .V 
        OO0OOO0000O000000 =queue .Queue ()
        O000OO0OO0OOOOO0O [O0O0000OOO00OOOO0 ]=1 
        OO0OOO0000O000000 .put (O0O0000OOO00OOOO0 )
        while (not OO0OOO0000O000000 .empty ()):
            OOOOO0OOO00OOOOOO =OO0OOO0000O000000 .queue [0 ]
            OO0OOO0000O000000 .get ()
            OO00O000O0OOOO00O =0 
            while OO00O000O0OOOO00O <len (O0O0OO00O00OO00O0 .l [OOOOO0OOO00OOOOOO ]):
                if (not O000OO0OO0OOOOO0O [O0O0OO00O00OO00O0 .l [OOOOO0OOO00OOOOOO ][OO00O000O0OOOO00O ]]):
                    O000OO0OO0OOOOO0O [O0O0OO00O00OO00O0 .l [OOOOO0OOO00OOOOOO ][OO00O000O0OOOO00O ]]=O000OO0OO0OOOOO0O [OOOOO0OOO00OOOOOO ]+1 
                    OO0OOO0000O000000 .put (O0O0OO00O00OO00O0 .l [OOOOO0OOO00OOOOOO ][OO00O000O0OOOO00O ])
                if (O0O0OO00O00OO00O0 .l [OOOOO0OOO00OOOOOO ][OO00O000O0OOOO00O ]==OOOO00000O00OOOOO ):
                    return O000OO0OO0OOOOO0O [O0O0OO00O00OO00O0 .l [OOOOO0OOO00OOOOOO ][OO00O000O0OOOO00O ]]-1 
                OO00O000O0OOOO00O +=1 
def SieveOfEratosthenes (OOO0000OO0OO0OO0O ):
    O00O0OO00OOO000OO =9999 
    O0O0OO0O00OOO0O00 =[True ]*(O00O0OO00OOO000OO +1 )
    OOO00OO0O0000O000 =2 
    while OOO00OO0O0000O000 *OOO00OO0O0000O000 <=O00O0OO00OOO000OO :
        if (O0O0OO0O00OOO0O00 [OOO00OO0O0000O000 ]==True ):
            for OOO00O0OO00O00O0O in range (OOO00OO0O0000O000 *OOO00OO0O0000O000 ,O00O0OO00OOO000OO +1 ,OOO00OO0O0000O000 ):
                O0O0OO0O00OOO0O00 [OOO00O0OO00O00O0O ]=False 
        OOO00OO0O0000O000 +=1 
    for OOO00OO0O0000O000 in range (1000 ,O00O0OO00OOO000OO +1 ):
        if (O0O0OO0O00OOO0O00 [OOO00OO0O0000O000 ]):
            OOO0000OO0OO0OO0O .append (OOO00OO0O0000O000 )
def compare (OOO0O0000OO00OO00 ,OOO0O00OO0O000O0O ):
    O00OO0OOO00OO00O0 =str (OOO0O0000OO00OO00 )
    O00OO0OO000OO0OO0 =str (OOO0O00OO0O000O0O )
    O0O0O0000OO0O0000 =0 
    if (O00OO0OOO00OO00O0 [0 ]!=O00OO0OO000OO0OO0 [0 ]):
        O0O0O0000OO0O0000 +=1 
    if (O00OO0OOO00OO00O0 [1 ]!=O00OO0OO000OO0OO0 [1 ]):
        O0O0O0000OO0O0000 +=1 
    if (O00OO0OOO00OO00O0 [2 ]!=O00OO0OO000OO0OO0 [2 ]):
        O0O0O0000OO0O0000 +=1 
    if (O00OO0OOO00OO00O0 [3 ]!=O00OO0OO000OO0OO0 [3 ]):
        O0O0O0000OO0O0000 +=1 
    return (O0O0O0000OO0O0000 ==1 )
def shortestPath (OO0OOO00OOO000OOO ,O0OOO0O00000O000O ):
    O000OOOOOOOOO0O00 =[]
    SieveOfEratosthenes (O000OOOOOOOOO0O00 )
    O0OOOO0OO00000OOO =Graph (len (O000OOOOOOOOO0O00 ))
    for O0O00OOO000O000O0 in range (len (O000OOOOOOOOO0O00 )):
        for OOO0OO0O0OOOO0OO0 in range (O0O00OOO000O000O0 +1 ,len (O000OOOOOOOOO0O00 )):
            if (compare (O000OOOOOOOOO0O00 [O0O00OOO000O000O0 ],O000OOOOOOOOO0O00 [OOO0OO0O0OOOO0OO0 ])):
                O0OOOO0OO00000OOO .addedge (O0O00OOO000O000O0 ,OOO0OO0O0OOOO0OO0 )
    O0000OOOOO0O000OO ,OOO0OOO0O0OOO0O00 =None ,None 
    for OOO0OO0O0OOOO0OO0 in range (len (O000OOOOOOOOO0O00 )):
        if (O000OOOOOOOOO0O00 [OOO0OO0O0OOOO0OO0 ]==OO0OOO00OOO000OOO ):
            O0000OOOOO0O000OO =OOO0OO0O0OOOO0OO0 
    for OOO0OO0O0OOOO0OO0 in range (len (O000OOOOOOOOO0O00 )):
        if (O000OOOOOOOOO0O00 [OOO0OO0O0OOOO0OO0 ]==O0OOO0O00000O000O ):
            OOO0OOO0O0OOO0O00 =OOO0OO0O0OOOO0OO0 
    return O0OOOO0OO00000OOO .bfs (O0000OOOOO0O000OO ,OOO0OOO0O0OOO0O00 )
if __name__ =='__main__':
    num1 =1033 
    num2 =8179 
    print (shortestPath (num1 ,num2 ))