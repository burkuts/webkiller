import requests
import os
import sys
import ipapi
from colorama import Fore

def __start__():
    print(Fore.RED+"\n [!] İP Adresi Girin")
    print(Fore.RED+"\n [/] Veya Enter Tuşuna Basın :))) \n")
    
    site = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"WEBKILLER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"IP-Lokasyonu"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")
    source = ipapi.location(ip=site, key=None, field=None)
    try:
        print(Fore.GREEN+" [!]"+Fore.RED+" Bilgilerinizi Görün")
        print (Fore.GREEN+" [!]"+Fore.BLUE+" İP = "+ source["ip"])
        print (Fore.GREEN+" [!]"+Fore.BLUE+" Şehir = " + source["city"])
        print (Fore.GREEN+" [!]"+Fore.BLUE+" Bölge = "+ source["region"])
        print (Fore.GREEN+" [!]"+Fore.BLUE+" Ülke Kimliği = "+source["country"])
        print (Fore.GREEN+" [!]"+Fore.BLUE+" Ülke = "+ source["country_name"])
        print (Fore.GREEN+" [!]"+Fore.BLUE+" Arama Kodu = "+source["country_calling_code"])
        print (Fore.GREEN+" [!]"+Fore.BLUE+" Dil = "+source["languages"])
        print (Fore.GREEN+" [!]"+Fore.BLUE+" org = "+ source["org"])
        try:
            input(Fore.RED+" [!] "+Fore.GREEN+"Menüye dön (Enter tuşuna basın...) ")
        except:
            print("")
            sys.exit()  
    except:
        print(Fore.RED+"Üzgünüz Lütfen İP Adresini Girin")

