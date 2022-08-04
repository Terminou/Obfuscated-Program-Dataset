import hashlib #line:4
def hash_file (O0OOO00O00000OO0O ):#line:6
   ""#line:8
   O00OOOOOOOOO0O0O0 =hashlib .sha1 ()#line:11
   with open (O0OOO00O00000OO0O ,'rb')as O000O0OO00O0OOO00 :#line:14
       OO0O0000OOO0000OO =0 #line:17
       while OO0O0000OOO0000OO !=b'':#line:18
           OO0O0000OOO0000OO =O000O0OO00O0OOO00 .read (1024 )#line:20
           O00OOOOOOOOO0O0O0 .update (OO0O0000OOO0000OO )#line:21
   return O00OOOOOOOOO0O0O0 .hexdigest ()#line:24
message =hash_file ("track1.mp3")#line:26
print (message )