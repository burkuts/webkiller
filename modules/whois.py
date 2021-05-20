import sys
import requests
from colorama import Fore


def __start__():
        try:
                print(Fore.RED+"\n [!] Lütfen Alan Adını/İP Adresini Girin\n")
                inp = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"WEBKILLER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Whois"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")
                result = requests.get('http://api.hackertarget.com/whois/?q=' + inp).text
                
                print(Fore.BLUE+result)
                try:
                        input(Fore.RED+" [!] "+Fore.GREEN+"Menüye Dön (Enter Tuşuna Bas...) ")
                except:
                        print("")
                        sys.exit()  
        except:
                print("\nÇıkış :)")