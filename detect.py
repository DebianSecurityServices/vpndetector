import os
import json
import urllib.request as urllib2
import sys


sys.ps1 = '\033[94m'


print(sys.ps1)

os.system('clear || cls')


print('''

████████╗██╗  ██╗███████╗██████╗ ███████╗██████╗ ██╗ █████╗ ███╗   ██╗
╚══██╔══╝██║  ██║██╔════╝██╔══██╗██╔════╝██╔══██╗██║██╔══██╗████╗  ██║
   ██║   ███████║█████╗  ██║  ██║█████╗  ██████╔╝██║███████║██╔██╗ ██║
   ██║   ██╔══██║██╔══╝  ██║  ██║██╔══╝  ██╔══██╗██║██╔══██║██║╚██╗██║
   ██║   ██║  ██║███████╗██████╔╝███████╗██████╔╝██║██║  ██║██║ ╚████║
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                      

                                  
                                                                        
''')

def hello():
    ip = input("""┌─[DebianSec@IP:~# 
└──╼Enter IP Address: """)
    url = f"https://ipqualityscore.com/api/json/ip/EjOM79qU69INQWrjJahbPiS51wGZUBfn/{ip}?strictness=0&allow_public_access_points=true&fast=true&lighter_penalties=true&mobile=true"
    response = urllib2.urlopen(url)
    data = response.read()
    values = json.loads(data)
    
    
    print("Host: ", end="")
    print(values['host'])
    print("Proxy: ", end="")
    print(values['proxy'])
    print("VPN: ", end="")
    print(values['vpn'])
    print("Tor: ", end="")
    print(values['tor'])
    print("Active VPN: ", end="")
    print(values['active_vpn'])
    print("Active Tor: ", end="")
    print(values['active_tor'])
    print("Bot Status: ", end="")
    print(values['bot_status'])
    
    os.system('pause')
    
hello()
