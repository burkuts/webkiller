import sys
import requests
from colorama import Fore

def __start__():
        try:
                
                print(Fore.RED+" [!] Lütfen Alan Adı Girin")
                inp = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"WEBKILLER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"TraceRoute"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")
                result = requests.get('https://api.hackertarget.com/mtr/?q=' + inp).text
                print(result)
                try:
                        input(Fore.RED+" [!] "+Fore.GREEN+"Menüye Dön (Enter Tuşuna Basınız)...) ")
                except:
                        print("")
                        sys.exit()  
        except:
                print("\nÇıkış :)")
                
        
