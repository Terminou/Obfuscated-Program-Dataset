MAX =1000 
tree =[0 ]*(4 *MAX )
arr =[0 ]*MAX 
def gcd (O00OO0O0OO00OO0O0 :int ,OOOO0OOO000O0OO00 :int ):
    if O00OO0O0OO00OO0O0 ==0 :
        return OOOO0OOO000O0OO00 
    return gcd (OOOO0OOO000O0OO00 %O00OO0O0OO00OO0O0 ,O00OO0O0OO00OO0O0 )
def lcm (OOO0000OOOOO0O0OO :int ,O000O00O00O000O00 :int ):
    return (OOO0000OOOOO0O0OO *O000O00O00O000O00 )//gcd (OOO0000OOOOO0O0OO ,O000O00O00O000O00 )
def build (O0OOOO0OOOO0OO0O0 :int ,OOOO0000000OO0O0O :int ,O0OO000000O00OOOO :int ):
    if OOOO0000000OO0O0O ==O0OO000000O00OOOO :
        tree [O0OOOO0OOOO0OO0O0 ]=arr [OOOO0000000OO0O0O ]
        return 
    O0OO0OO000O0O000O =(OOOO0000000OO0O0O +O0OO000000O00OOOO )//2 
    build (2 *O0OOOO0OOOO0OO0O0 ,OOOO0000000OO0O0O ,O0OO0OO000O0O000O )
    build (2 *O0OOOO0OOOO0OO0O0 +1 ,O0OO0OO000O0O000O +1 ,O0OO000000O00OOOO )
    O0O000000O00000OO =tree [2 *O0OOOO0OOOO0OO0O0 ]
    OO0000O0OO0O00OOO =tree [2 *O0OOOO0OOOO0OO0O0 +1 ]
    tree [O0OOOO0OOOO0OO0O0 ]=lcm (O0O000000O00000OO ,OO0000O0OO0O00OOO )
def query (OOOOO0OOO0O0OOOO0 :int ,OO00O00OOO0O0OOOO :int ,O00OOOO0000OOOOO0 :int ,OO0OO00OOOO0OO00O :int ,OO000OO00O000O0OO :int ):
    if O00OOOO0000OOOOO0 <OO0OO00OOOO0OO00O or OO00O00OOO0O0OOOO >OO000OO00O000O0OO :
        return 1 
    if OO0OO00OOOO0OO00O <=OO00O00OOO0O0OOOO and OO000OO00O000O0OO >=O00OOOO0000OOOOO0 :
        return tree [OOOOO0OOO0O0OOOO0 ]
    OOOOOO0OO00000O00 =(OO00O00OOO0O0OOOO +O00OOOO0000OOOOO0 )//2 
    O0O00OOO0OOO00000 =query (2 *OOOOO0OOO0O0OOOO0 ,OO00O00OOO0O0OOOO ,OOOOOO0OO00000O00 ,OO0OO00OOOO0OO00O ,OO000OO00O000O0OO )
    O000O0OOO000000O0 =query (2 *OOOOO0OOO0O0OOOO0 +1 ,OOOOOO0OO00000O00 +1 ,O00OOOO0000OOOOO0 ,OO0OO00OOOO0OO00O ,OO000OO00O000O0OO )
    return lcm (O0O00OOO0OOO00000 ,O000O0OOO000000O0 )
if __name__ =="__main__":
    arr [0 ]=5 
    arr [1 ]=7 
    arr [2 ]=5 
    arr [3 ]=2 
    arr [4 ]=10 
    arr [5 ]=12 
    arr [6 ]=11 
    arr [7 ]=17 
    arr [8 ]=14 
    arr [9 ]=1 
    arr [10 ]=44 
    build (1 ,0 ,10 )
    print (query (1 ,0 ,10 ,2 ,5 ))
    print (query (1 ,0 ,10 ,5 ,10 ))
    print (query (1 ,0 ,10 ,0 ,10 ))
