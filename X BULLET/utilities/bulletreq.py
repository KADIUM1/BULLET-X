import os, requests, threading, colorama, sys, time, asyncio, pystyle, random, string, dhooks, websocket, json, webbrowser
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from dhooks import Webhook
from json import dumps
from websocket import WebSocket
from json import loads
from colorama import Fore, Back, Style
from concurrent.futures import ThreadPoolExecutor
try:
    import requests
except:
    os.system("pip install requests")
    import requests
try:
    import threading
except:
    os.system("pip install threading")
    import threading
try:
    import colorama
except:
    os.system("pip install colorama")
    import colorama
    from colorama import Fore, Back, Style
try:
    import dhooks
except:
    os.system("pip install dhooks")
    import dhooks
    from dhooks import Webhook
try:
    import pystyle
except:
    os.system("pip install pystyle")
    import pystyle
    from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
try:
    import json
except:
    os.system("pip install json")
try: 
    import random
except:
    os.system("pip install random")
try:
    import string
except:
    os.system("pip install string")
try: 
    import webbrowser
except:
    os.system("pip install webbrowser")
try:
    import httpx
except:
    os.system("pip install httpx")
try:
    import time
except:
    os.system("pip install time")
try:
    import os
except:
    os.system("pip install os")
try:
    import urlopen
except:
    os.system("pip install urlopen")