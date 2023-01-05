from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import os
import time



def start5():
    os.system("title PRESS ENTER")
    bullet = r'''

██╗  ██╗    ██████╗ ██╗   ██╗██╗     ██╗     ███████╗████████╗
╚██╗██╔╝    ██╔══██╗██║   ██║██║     ██║     ██╔════╝╚══██╔══╝
 ╚███╔╝     ██████╔╝██║   ██║██║     ██║     █████╗     ██║   
 ██╔██╗     ██╔══██╗██║   ██║██║     ██║     ██╔══╝     ██║   
██╔╝ ██╗    ██████╔╝╚██████╔╝███████╗███████╗███████╗   ██║   
╚═╝  ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝   
                                                                       
'''
    System.Size(120,30)
    System.Clear()
    Anime.Fade(Center.Center(bullet), Colors.purple_to_blue, Colorate.Vertical, interval=0.030, enter=True)
