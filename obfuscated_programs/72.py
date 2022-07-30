class Node :
    def __init__ (O0000OOO00O0OOOOO ,OO0000OO0O000OO0O ):
        O0000OOO00O0OOOOO .data =OO0000OO0O000OO0O 
        O0000OOO00O0OOOOO .left =None 
        O0000OOO00O0OOOOO .right =None 
def printLevelOrder (OOOO0000000O0OO00 ):
    O0OOO0OOO0O0O0OO0 =height (OOOO0000000O0OO00 )
    for OOO0O0OO0OO0OO0OO in range (1 ,O0OOO0OOO0O0O0OO0 +1 ):
        printCurrentLevel (OOOO0000000O0OO00 ,OOO0O0OO0OO0OO0OO )
def printCurrentLevel (O00O0O000OOO00OO0 ,O00O00OOOOO00O000 ):
    if O00O0O000OOO00OO0 is None :
        return 
    if O00O00OOOOO00O000 ==1 :
        print (O00O0O000OOO00OO0 .data ,end =" ")
    elif O00O00OOOOO00O000 >1 :
        printCurrentLevel (O00O0O000OOO00OO0 .left ,O00O00OOOOO00O000 -1 )
        printCurrentLevel (O00O0O000OOO00OO0 .right ,O00O00OOOOO00O000 -1 )

def height (O00OO00OOOOO0O0OO ):
    if O00OO00OOOOO0O0OO is None :
        return 0 
    else :
        O0O0OOO000000000O =height (O00OO00OOOOO0O0OO .left )
        OO00O00O00O00OOOO =height (O00OO00OOOOO0O0OO .right )
        if O0O0OOO000000000O >OO00O00O00O00OOOO :
            return O0O0OOO000000000O +1 
        else :
            return OO00O00O00O00OOOO +1 
root =Node (1 )
root .left =Node (2 )
root .right =Node (3 )
root .left .left =Node (4 )
root .left .right =Node (5 )
print ("Level order traversal of binary tree is -")
printLevelOrder (root )