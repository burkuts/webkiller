import sys
import requests
from colorama import Fore

def __start__():
    try:
        print(Fore.LIGHTBLACK_EX+"\n [!] PORT Tarayıcı ! ! !")
        print(Fore.MAGENTA+"\n [!] Lütfen İP/Alan Adı Girin\n")
        inp = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"WEBKILLER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Port-Tarayıcı"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")
        result = requests.get('https://api.hackertarget.com/nmap/?q=' + inp).text
        print(Fore.YELLOW+result)
        try:

            input(Fore.RED+" [!] "+Fore.GREEN+"Menüye dön (Enter tuşuna basın...) ")
        except:
            print("")
            sys.exit()  
        
    except:
        print("\nÇıkış :)")
