import os
import requests
import json
from colorama import Fore
import sys

def __start__():
        
        print (Fore.RED+"\n [!] Alan Adını/İP Adresini Girin\n")

        website = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"WEBKILLER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Reverse_IP"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")

        mysite = {"remoteAddress":website}

        link = requests.post("https://domains.yougetsignal.com/domains.php" , mysite)

        source = json.loads(link.content)

        print(source)


        for data in source["domainArray"]:
                print(" "+data[0]+"\n")

        try:

                input(Fore.RED+" [!] "+Fore.GREEN+"Menüye dön (Enter Tuşuna Basın...) ")
        except:
                print("")
                sys.exit()