# -*- coding: utf-8 -*-
try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests,bhottool
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system("pip2 install bhottool")
    time.sleep(1)
    os.system('python2 bhot.py')
reload(sys)
sys.setdefaultencoding('utf8')
os.system("clear")


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
		
		

##### LOGO #####
logo="""
\033[1;96m ------------------------
 \033[1;32m < OFFICIAL CODER SoHag >
 \033[1;96m   
  ____        _   _             
 / ___|  ___ | | | | __ _  __ _ 
 \___ \ / _ \| |_| |/ _` |/ _` |
  ___) | (_) |  _  | (_| | (_| |
 |____/ \___/|_| |_|\__,_|\__, |
                          |___/ 

\033[1:96m 
\033[1;92m 
\033[1;91m 
\033[1;92m 
\033[1;91m 
           \033[1;93m   
            \033[1;92m
            \033[1;91m   ######...#######..##.....##....###.....######..
 .##....##.##.....##.##.....##...##.##...##....##.
 .##.......##.....##.##.....##..##...##..##.......
 ..######..##.....##.#########.##.....##.##...####
 .......##.##.....##.##.....##.#########.##....##.
 .##....##.##.....##.##.....##.##.....##.##....##.
 ..######...#######..##.....##.##.....##..######..


          \033[1;92m  
           \033[1;91m                                           
\033[1;93m        IT'S NOT JUST A NAME, IT'S A BRAND
\033[1;97m--------------------------------------------------
\033[1;95m
 AUTHOR     : N S SoHag Chowdhury 
 FACEBOOK   : FACEBOOK.COM/NsSoHagChowdhury
 YOUTUBE    : YOUTUBE.COM/Md SoHag Chowdhury 
 GITHUB     : GITHUB.COM/BangladeshSpecialForce52
\033[1;32m
--------------------------------------------------
                                """

cusr = "SoHaglovehacker"
cpwd = "SoHagBSF-52"
def u():
    os.system("clear")
    print(logo)
    usr=raw_input(" TOOL USERNAME : ")
    if usr == cusr:
        p()
    else:
        os.system("clear")
        print(logo)
        print(" TOOL USERNAME : "+usr+" (wrong)")
        time.sleep(1)
        os.system('xdg-open https://www.youtube.com/Md SoHag Chowdhury ')
        u()
def p():
    os.system("clear")
    print(logo)
    print(" TOOL USERNAME : SoHaglovehacker(correct)")
    pwd=raw_input(" TOOL PASSWORD : ")
    if pwd == cpwd:
        z()
    else:
        os.system("clear")
        print(logo)
        print(" TOOL USERNAME : SoHaglovehacker(correct)")
        print(" TOOL PASSWORD : "+pwd+" (wrong)")
        time.sleep(1)
        os.system('xdg-open https://www.facebook.com/groups/818781448293333/?ref=share.  ')
        p()
    
def z():
    os.system("clear")  
    print(logo)
    print(" TOOL USERNAME : SoHaglovehacker (correct)")
    print(" TOOL PASSWORD : SoHagBSF-52 (correct)")
    print(" \033[1;92mLogin Successfull\033[0m")
    jalan("\033[1;93mPlease Wait 2 Minutes, All Packages Are Chacking.....")
  
    time.sleep(1)
    os.system("python2 .README.md")
if __name__=="__main__":
    u()
