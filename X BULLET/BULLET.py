import os, requests, threading, colorama, sys, time, asyncio, pystyle, random, string, dhooks, websocket, json, webbrowser, httpx, base64, datetime, discord
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from dhooks import Webhook
from json import dumps
from websocket import WebSocket
from json import loads
from colorama import Fore, Back, Style
from concurrent.futures import ThreadPoolExecutor
import discum
import ctypes
import urlopen
from discord.ext import commands
from utilities import bulletreq
from utilities.__pyadd__.__pycache17__.__bulletreq715x__ import bulletx

version = "1.00.01"

def clear():
    os.system('cls')

tkncount = ('tokens.txt')
count = 0
tukans = open(tkncount, 'r')
for line in tukans:
    count = count + 1

def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text

def mainHeader(token):
    return {
        "authorization": token,
        "accept": "*/*",
        'accept-encoding': 'gzip, deflate, br',
        "accept-language": "en-GB",
        "content-length": "90",
        "content-type": "application/json",
        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        "origin": "https://discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }

colorama.init()

def idscraper():
    clear()
    os.system("title X BULLET ID SCRAPER")
    tukan = Write.Input("[TOKEN] Discord Account Token » ", Colors.purple_to_blue, interval=0.000)
    guildd = Write.Input("[SERVER] Server ID » ", Colors.purple_to_blue, interval=0.000)
    chann = Write.Input("[CHANNEL] Channel ID » ", Colors.purple_to_blue, interval=0.000)
    bot = discum.Client(tukan)

    def closefetching(resp,guildid):
        if bot.gateway.finishedMemberFetching(guildid):
            enmembersfetched = len(bot.gateway.session.guild(guildid).members)
        print(str(enmembersfetched))
        bot.gateway.removeCommand({'function':closefetching, 'params':{'guildid':guildid}})
        bot.gateway.close()

    def getmembers(guildid,channelid):
            bot.gateway.fetchMembers(guildid, channelid, keep='all',wait=1)
            bot.gateway.command({'function':closefetching,'params':{'guildid':guildid}})
            bot.gateway.run()
            bot.gateway.resetSession()
            return bot.gateway.session.guild(guildid).members

    members = getmembers(guildd, chann)
    memberids = []

    for memberId in members:
        memberids.append(memberId)

    clear()

    with open('data/memberids.txt','w') as ids:
        for element in memberids:
            ids.write(element + '\n')    

    Write.Print("[SUCCESS] Sucessfully scraped member ids", Colors.purple_to_blue, interval=0.000)

    time.sleep(1)
    exitt()

def leaver():
        clear()
        os.system("title X BULLET SERVER LEAVER")
        token = open("tokens.txt", "r").read().splitlines()

        ID = Write.Input("[SERVER] Server ID » ", Colors.purple_to_blue, interval=0.000)

        apilink = "https://discord.com/api/v9/users/@me/guilds/" + str(ID)

        with open('tokens.txt', 'r') as handle:
            tokens = handle.readlines()
            for i in tokens:
                token = i.rstrip()
                headers = {
                    'Authorization': token,
                    "content-length": "0",
                    "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                    "origin": "https://discord.com",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                    "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                    "x-debug-options": "bugReporterEnabled",
                    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
                }
                requests.delete(apilink, headers=headers)
                time.sleep(0.01)
                exitt()


def webhookspam():
    os.system("title X BULLET WEBHOOK SPAMMER")
    clear()
    webhookk = Write.Input("[WEBHOOK] Webhook to Spam » ", Colors.purple_to_blue, interval=0.000)
    hook = Webhook(webhookk)
    message = Write.Input("[MESSAGE] Message to Spam » ", Colors.purple_to_blue, interval=0.000)
    start2 = Write.Input("[START] Press ENTER to Start!", Colors.purple_to_blue, interval=0.000)
    while True:
        hook.send(message)
        Write.Print(f"[SUCCESS] Successfully Sent Message » {message}\n", Colors.purple_to_blue, interval=0.000)

def webhookdel():
    clear()
    os.system("title X BULLET WEBHOOK DELETER")
    webhook5 = Write.Input("[WEBHOOK] Enter Webhook to Delete » ", Colors.purple_to_blue, interval=0.000)
    deletehook = requests.delete(webhook5)
    the = requests.get(webhook5)
    if the.status_code == 404:
      Write.Print("[SUCESS] Webhook Deleted", Colors.purple_to_blue, interval=0.000)
    exitt()

def title2():
    system = os.name
    if system == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(f"X BULLET CHANNEL RAIDER - FREE VERSION")
    elif system == 'posix':
        sys.stdout.write(f"X BULLET CHANNEL RAIDER - FREE VERSION")
    else:
        pass

def raider():
    clear()
    title2()
    channel7 = Write.Input("[CHANNEL] Channel ID » ", Colors.purple_to_blue, interval=0.000)
    mess7 = Write.Input("[MESSAGE] Message » ", Colors.purple_to_blue, interval=0.000)
    delay7 = ("0")

    tokens = open("tokens.txt", "r").read().splitlines()


    def spam(token, channel7, mess7):
        url = 'https://discord.com/api/v9/channels/'+channel7+'/messages'
        data = {"content": mess7}
        header = {"authorization": token}

        while True:
            time.sleep(0.0001)
            r = requests.post(url, data=data, headers=header)
            print(Fore.WHITE + "[" + Fore.MAGENTA + ">" + Fore.WHITE + "] » Successfully Sent message")



    def thread():
        channel_id = channel7
        text = mess7
        for token in tokens:
            time.sleep(int(delay7))
            threading.Thread(target=spam, args=(token, channel_id, text)).start()


    start = input(Fore.WHITE + "[" + Fore.MAGENTA + ">" + Fore.WHITE + "] » X BULLET is ready press ENTER to start")
    start = thread()
    start = thread()
    start = thread()
    start = thread()
    start = thread()
    start = thread()
    start = thread()
    start = thread()


def discord():
    webbrowser.open("https://discord.com/channels/@me")
    Write.Print("[USERNAME] » KADIUM#0002", Colors.purple_to_blue, interval=0.000)
    time.sleep(10)
    clear()
    menu()


def tokenchecker():
    os.system("title X BULLET TOKEN CHECKER")
    clear()
    tkn2 = Write.Input("[TOKEN] Token to Check » ", Colors.purple_to_blue, interval=0.000)
    headers = {
        "Accept": "*/*",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Alt-Used": "discord.com",
        "Authorization": tkn2,
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Cookie": "__dcfduid=8ae3ca90b4d911ec998447df76ccab6d; __sdcfduid=8ae3ca91b4d911ec998447df76ccab6d07a29d8ce7d96383bcbf0ff12d2f61052dd1691af72d9101442df895f59aa340; OptanonConsent=isIABGlobal=false&datestamp=Tue+Sep+20+2022+15%3A55%3A24+GMT%2B0200+(hora+de+verano+de+Europa+central)&version=6.33.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1&AwaitingReconsent=false&geolocation=ES%3BMD; __stripe_mid=1798dff8-2674-4521-a787-81918eb7db2006dc53; OptanonAlertBoxClosed=2022-04-15T16:00:46.081Z; _ga=GA1.2.313716522.1650038446; _gcl_au=1.1.1755047829.1662931666; _gid=GA1.2.778764533.1663618168; locale=es-ES; __cfruid=fa5768ee3134221f82348c02f7ffe0ae3544848a-1663682124",
        "Host": "discord.com",
        "Origin": "https://discord.com",
        "Referer": "https://discord.com/channels/@me",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
        "X-Debug-Options": "bugReporterEnabled",
        "X-Discord-Locale": "es-ES",
        "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlcy1FUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwNS4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwNS4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA1LjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6Imh0dHBzOi8vd3d3Lmdvb2dsZS5jb20vIiwicmVmZXJyaW5nX2RvbWFpbiI6Ind3dy5nb29nbGUuY29tIiwic2VhcmNoX2VuZ2luZSI6Imdvb2dsZSIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxNDc2MTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }
    response2 = httpx.get("https://discord.com/api/v9/users/@me", headers=headers)
    if response2.status_code == 200:
        Write.Print(f"[WORKING] Token {tkn2} is working", Colors.green_to_blue, interval=0.000)
    else:
        Write.Print(f"[INVALID] Token {tkn2} is not working", Colors.red_to_blue, interval=0.000)
    exitt()


def webhookchecker():
    os.system("title X BULLET WEBHOOK CHECKER")
    clear()
    webhook29 = Write.Input("[WEBHOOK] Enter Webhook to check » ", Colors.purple_to_blue, interval=0.000)
    w = requests.get(webhook29)
    if w.status_code == 200:
        Write.Print("[WORKING] Webhook Is Working", Colors.green_to_blue, interval=0.000)
        exitt()
    else:
            Write.Print("[INVALID] Webhook is not Working", Colors.red_to_blue, interval=0.000)
    exitt()

clear()
os.system("title X BULLET LOGIN")
try:
    with open('data/logins.json') as f:
        config = json.load(f)
except:
    with open('data/logins.json', 'w') as f:
        Write.Print("\n[>] Login into X BULLET ", Colors.purple_to_blue, interval=0.000)
        login = Write.Input("\n[>] Enter a Username » ", Colors.purple_to_blue, interval=0.000)
        json.dump({"Login": login}, f, indent=4)
    Write.Input(f"\nSuccessfully logged in as {login} Press ENTER to Continue", Colors.purple_to_blue, interval=0.000)
    pass
with open('data/logins.json') as f:
    config = json.load(f)
    login = config.get('Login')

def title():
    system = os.name
    if system == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(f"X BULLET-FREE VERSION    |    Made by KADIUM#0074    |    Tokens: [{count}]   |   Username: {login}  |   Version: {version}")
    elif system == 'posix':
        sys.stdout.write(f"X BULLET- FREE VERSION    |    Made by KADIUM#0074    |    Tokens: [{count}]")
    else:
        pass

def nitrogen():
        clear()
        count1 = 0
        os.system("title X BULLET NITRO GEN")
        nitroge = Write.Input("[WEBHOOK] Webhook » ", Colors.purple_to_blue, interval=0.000)
        hook4 = Webhook(nitroge)
        while True:
            code1 = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(24))
            hook4.send("https://discord.com/billing/promotions/" + code1)
            Write.Print("\n[SUCCESS] » Generated Nitro ", Colors.purple_to_blue, interval=0.000)

def invitejoiner():
    os.system("title X BULLET INVITE JOINER")
    clear()
    print(Fore.WHITE + "[" + Fore.MAGENTA + "!" + Fore.WHITE + "] » Invite Joiner is in a paid version of x bullet")
    open2 = input(Fore.WHITE + "[" + Fore.MAGENTA + ">" + Fore.WHITE + "] » Would you like to contact the dev y/n » ")
    if open2 == "y":
        webbrowser.open("https://discord.com/channels/@me")
        Write.Print("Username: KADIUM#0074", Colors.purple_to_blue, interval=0.000)
        exitt()
    if open2 == "n":
        exitt()



def tokenyear():
    os.system("title X BULLET TOKEN YEAR CHECKER")
    clear()
    print(Fore.WHITE + "[" + Fore.MAGENTA + ">" + Fore.WHITE + "] » Make Sure the Tokens are in email:password:token format")
    Write.Input("\n Press ENTER to Start", Colors.purple_to_blue, interval=0.000)


    for token in open("tokens.txt").read().splitlines():


        only_token = token.split(":")[2]


        userid_base64 = only_token.split(".")[0] + "=="
        userid = base64.b64decode(userid_base64).decode("utf-8")


        usertmiestamp_binary = bin(int(userid))[:-22]
        creationdate_unix = int(usertmiestamp_binary, 2) + 1420070400000

    
        year = datetime.datetime.fromtimestamp(creationdate_unix/1000).strftime('%Y')

    
        with open("output/" + year + ".txt", 'a') as f:
            f.write(token + "\n")

  
        print(f"{userid_base64} - {year}")

    Write.Input("\n Finished..  Wrote into output/year.txt", Colors.purple_to_blue, interval=0.000)
    

def botpanel():
    clear()
    os.system("title X BULLET DISCORD BOT PANELS")
    print(Fore.WHITE + "[" + Fore.MAGENTA + "!" + Fore.WHITE + "] » X BULLET Discord Bots Command's are not avabile yet..")
    exitt()

colorama.init()

def menu():
    clear()
    print("")
    title()
    Write.Print(f"                          ██╗  ██╗    ██████╗ ██╗   ██╗██╗     ██╗     ███████╗████████╗\n", Colors.purple_to_blue, interval=0.000)
    Write.Print(f"                          ╚██╗██╔╝    ██╔══██╗██║   ██║██║     ██║     ██╔════╝╚══██╔══╝\n", Colors.purple_to_blue, interval=0.000)
    Write.Print(f"                           ╚███╔╝     ██████╔╝██║   ██║██║     ██║     █████╗     ██║   \n", Colors.purple_to_blue, interval=0.000)
    Write.Print(f"                           ██╔██╗     ██╔══██╗██║   ██║██║     ██║     ██╔══╝     ██║   \n", Colors.purple_to_blue, interval=0.000)
    Write.Print(f"                          ██╔╝ ██╗    ██████╔╝╚██████╔╝███████╗███████╗███████╗   ██║   \n", Colors.purple_to_blue, interval=0.000)
    Write.Print(f"                          ╚═╝  ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝   \n", Colors.purple_to_blue, interval=0.000)
    Write.Print(f"════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n", Colors.purple_to_blue, interval=0.000)   
    Write.Print(f"                                    Tokens Loaded » {count} // Logged in as {login}\n", Colors.purple_to_blue, interval=0.000)
    Write.Print(f'════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n', Colors.purple_to_blue, interval=0.000)    
    Write.Print(f"\n[01] » X BULLET Channel Raider\n", Colors.purple_to_blue, interval=0.000)
    Write.Print(f"[02] » X BULLET Webhook Spammer\n", Colors.purple_to_blue, interval=0.000)
    Write.Print(f"[03] » X BULLET Server Leaver\n", Colors.purple_to_blue, interval=0.000)
    Write.Print(f"[04] » X BULLET Member ID Scraper\n", Colors.purple_to_blue, interval=0.000)
    Write.Print(f"[05] » X BULLET Webhook Deleter\n", Colors.purple_to_blue, interval=0.000)
    Write.Print(f"[06] » X BULLET Webhook Checker\n", Colors.purple_to_blue, interval=0.000)
    Write.Print(f"[07] » X BULLET Token Checker\n", Colors.purple_to_blue, interval=0.000)
    Write.Print(f"[08] » X BULLET Nitro Promo Gen\n", Colors.purple_to_blue, interval=0.000)
    Write.Print(f"[09] » X BULLET Token Year Checker\n", Colors.purple_to_blue, interval=0.000)
    Write.Print(f"[10] » X BULLET Invite Joiner\n", Colors.purple_to_blue, interval=0.000)
    Write.Print(f"[00] » X BULLET DEV's Discord\n", Colors.purple_to_blue, interval=0.000)
    Write.Print(f"[99] » X BULLET Discord Bot Panel\n", Colors.purple_to_blue, interval=0.000)
    choose = Write.Input("[INPUT] » X BULLET Choose » ", Colors.purple_to_blue, interval=0.000)

    if choose == ("1"):
        raider()
    if choose == ("2"):
        webhookspam()
    if choose == ("3"):
        leaver()
    if choose == ("0"):
        discord()
    if choose == ("4"):
        idscraper()
    if choose == ("5"):
        webhookdel()
    if choose == ("6"):
        webhookchecker()  
    if choose == ("7"):
        tokenchecker()
    if choose == ("8"):
        nitrogen()
    if choose == ("9"):
        tokenyear()
    if choose == ("10"):
        invitejoiner()
    if choose == ("99"):
        botpanel()

def exitt():
    Write.Input("\nPress Enter to go back...", Colors.purple_to_blue, interval=0.000)
    clear()
    menu()
menu()

System.Size(120,30)