from colorama import init, Style, Fore
from random import randint
import os
import requests
ip_address = []
useless = []
randomL = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 0 1 2 3 4 5 6 7 8 9".split(" ")

init(autoreset=True)

def proxy(proxyList):
    idx = randint(0, len(ip_address) -1)
    currentProxy = {"http": ip_address[idx], "https": ip_address[idx]}
    return currentProxy

def generateCode(amount, type, save):
    codes = []
    i = 0
    if type == "classic": typeX = 16
    if type == "boost": typeX = 24
    while i < int(amount):
        s = ""
        j = 0
        while j < typeX:
            s += str(randomL[randint(0,len(randomL)-1)])
            j+=1
        if s not in useless:
            codes.append(f"{s}")
        else: amount += 1
        i+=1
    return codes


def checkCode(code, savefile):
    current = proxy(ip_address)
    r = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}", timeout=3,proxies=current)
    if r.status_code == 404:
        return print(f"{Fore.BLACK}{Style.BRIGHT}[{Fore.RED}{Style.NORMAL}>{Fore.BLACK}{Style.BRIGHT}]{Fore.YELLOW}{Style.BRIGHT} {code} {Fore.BLACK} - Invalid Code")
        useless.append(code)
    elif r.status_code == 200:
        return print(f"{Fore.BLACK}{Style.BRIGHT}[{Fore.GREEN}{Style.NORMAL}>{Fore.BLACK}{Style.BRIGHT}]{Fore.YELLOW}{Style.BRIGHT} {code} {Fore.BLACK} - Working Code")
        with open(savefile, "w") as f:
            f.write(f"https://discord.gift/{code}\n")
    elif r.status_code == 429:
        return print(f"{Fore.BLACK}{Style.BRIGHT}[{Fore.YELLOW}{Style.NORMAL}>{Fore.BLACK}{Style.BRIGHT}]{Fore.YELLOW}{Style.BRIGHT} {proxyList[idx]} {Fore.BLACK} - Proxy rate limited")
        current = proxy(ip_address)
        checkCode(code, savefile)


os.system("cls")
print(f"""{Fore.BLUE}{Style.BRIGHT}
                                                                          
             _____            ____  _____   ______         _____            _____    
             |\    \   _____  |    ||\    \ |\     \    ___|\    \      ____|\    \   
             | |    | /    /| |    | \\    \| \     \  /    /\    \    /     /\    \  
             \/     / |    || |    |  \|    \  \     ||    |  |____|  /     /  \    \ 
             /     /_  \   \/ |    |   |     \  |    ||    |    ____ |     |    |    |
            |     // \  \   \ |    |   |      \ |    ||    |   |    ||     |    |    |
            |    |/   \ |    ||    |   |    |\ \|    ||    |   |_,  ||\     \  /    /|
            |\ ___/\   \|   /||____|   |____||\_____/||\ ___\___/  /|| \_____\/____/ |
            | |   | \______/ ||    |   |    |/ \|   ||| |   /____ / | \ |    ||    | /
             \|___|/\ |    | ||____|   |____|   |___|/ \|___|    | /   \|____||____|/ 
                \(   \|____|/   \(       \(       )/     \( |____|/       \(    )/    
                 '      )/       '        '       '       '   )/           '    '     
                        '                                     '                       
                                    {Fore.RED}Desgined by: kute#0069
                                    OpenSource Project
                                    Code: https://github.com/xxxx/xxxx
""")
steps = 0
while steps < 4:
    x = input(f"{Fore.BLACK}{Style.BRIGHT}[{Fore.RED}{Style.NORMAL}~{Fore.BLACK}{Style.BRIGHT}] Amount of codes to generate.\n    {Fore.WHITE}")
    steps += 1
    y = input(f"{Fore.BLACK}{Style.BRIGHT}[{Fore.RED}{Style.NORMAL}~{Fore.BLACK}{Style.BRIGHT}] Write the filename to save nitro hits, this gonna generate or use an existing file (default = hits.txt).\n    {Fore.WHITE}")
    steps += 1
    z = input(f"{Fore.BLACK}{Style.BRIGHT}[{Fore.RED}{Style.NORMAL}~{Fore.BLACK}{Style.BRIGHT}] Select nitro type to be generated, boost/classic (classic is 16 digits and boost is 24 digits).\n    {Fore.WHITE}")
    steps += 1
    p = input(f"{Fore.BLACK}{Style.BRIGHT}[{Fore.RED}{Style.NORMAL}~{Fore.BLACK}{Style.BRIGHT}] Select proxy file (you need to have one, Default = proxy.txt).\n    {Fore.WHITE}")
    steps += 1
    if y == "" or y == None:
        y = "hits.txt"

    if z == "" or z == None:
        z = "classic"
    if p == "" or p == None:
        p = "proxy.txt"
    if os.path.exists('config.txt') == False:
        with open('config.txt', "w") as f:
            f.write(f"config_amount: {x}\nconfig_file: {y}\nconfig_type: {z}\nconfig_proxy: {p}")
    if os.path.exists(y) == False:
        with open(y, "w") as f:
            print()
    dn = generateCode(x,z,y)
    with open(p, "r") as f:
        ip_address = [line.rstrip() for line in f]
    for i in dn:
        print(checkCode(i, y))