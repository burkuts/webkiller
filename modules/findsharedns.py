import sys
import requests
from colorama import Fore

def __start__():

        try:
                print(Fore.RED+"\n [!] Lütfen İP/Alan Adı Girin\n")
                inp = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"WEBKILLER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"DNS-Bulucu"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")
                result = requests.get('https://api.hackertarget.com/findshareddns/?q=' + inp).text
                print(Fore.BLUE+result)
                try:
                        input(Fore.RED+" [!] "+Fore.GREEN+"Menüye dön (Enter tuşuna basın...) ")
                except:
                        print("")
                        sys.exit()  
                
        except:
                print("\nÇıkış :)")


