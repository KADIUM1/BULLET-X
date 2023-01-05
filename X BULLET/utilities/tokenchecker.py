import os, requests, httpx
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System


def tokenchecker():
    os.system("title X BULLET TOKEN CHECKER")
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