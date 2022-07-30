class Node :	
  def __init__ (OO0OO0O0O0OOO0O0O ,O0O00O0O0O0O0O0OO ):	
    OO0OO0O0O0OOO0O0O .data =O0O00O0O0O0O0O0OO ;	
    OO0OO0O0O0OOO0O0O .next =None ;	
class CreateList :	
  def __init__ (O0OOOOOOO000OO000 ):	
    O0OOOOOOO000OO000 .head =Node (None );	
    O0OOOOOOO000OO000 .tail =Node (None );	
    O0OOOOOOO000OO000 .head .next =O0OOOOOOO000OO000 .tail ;	
    O0OOOOOOO000OO000 .tail .next =O0OOOOOOO000OO000 .head ;	
  def add (O00000OO00OO0OO0O ,O000OO00OO0OOO0O0 ):	
    O0OO0OO00O0O00O0O =Node (O000OO00OO0OOO0O0 );	
    if O00000OO00OO0OO0O .head .data is None :	
      O00000OO00OO0OO0O .head =O0OO0OO00O0O00O0O ;	
      O00000OO00OO0OO0O .tail =O0OO0OO00O0O00O0O ;	
      O0OO0OO00O0O00O0O .next =O00000OO00OO0OO0O .head ;	
    else :	
      O00000OO00OO0OO0O .tail .next =O0OO0OO00O0O00O0O ;	
      O00000OO00OO0OO0O .tail =O0OO0OO00O0O00O0O ;	
      O00000OO00OO0OO0O .tail .next =O00000OO00OO0OO0O .head ;	
  def removeDuplicate (O0O000O0OO0OO00O0 ):	
    OOO0O00000O0OO00O =O0O000O0OO0OO00O0 .head ;	
    if (O0O000O0OO0OO00O0 .head ==None ):	
      print ("List is empty");	
    else :	
      while (True ):	
        OO0O0O000000OO0OO =OOO0O00000O0OO00O ;	
        O00OO0OOOOO000O0O =OOO0O00000O0OO00O .next ;	
        while (O00OO0OOOOO000O0O !=O0O000O0OO0OO00O0 .head ):	
          if (OOO0O00000O0OO00O .data ==O00OO0OOOOO000O0O .data ):	
            OO0O0O000000OO0OO .next =O00OO0OOOOO000O0O .next ;	
          else :	
            OO0O0O000000OO0OO =O00OO0OOOOO000O0O ;	
          O00OO0OOOOO000O0O =O00OO0OOOOO000O0O .next ;	
        OOO0O00000O0OO00O =OOO0O00000O0OO00O .next ;	
        if (OOO0O00000O0OO00O .next ==O0O000O0OO0OO00O0 .head ):	
          break ;	
  def display (OOO0O0000OO0000O0 ):	
    O0O0000O000O0OOO0 =OOO0O0000OO0000O0 .head ;	
    if OOO0O0000OO0000O0 .head is None :	
      print ("List is empty");	
      return ;	
    else :	
      print (O0O0000O000O0OOO0 .data );	
      while (O0O0000O000O0OOO0 .next !=OOO0O0000OO0000O0 .head ):	
        O0O0000O000O0OOO0 =O0O0000O000O0OOO0 .next ;	
        print (O0O0000O000O0OOO0 .data );	
    print ("\n");	
class CircularLinkedList :	
  cl =CreateList ();	
  cl .add (1 );	
  cl .add (2 );	
  cl .add (3 );	
  cl .add (2 );	
  cl .add (2 );	
  cl .add (4 );	
  print ("Originals list: ");	
  cl .display ();	
  cl .removeDuplicate ();	
  print ("List after removing duplicates: ");	
  cl .display ();