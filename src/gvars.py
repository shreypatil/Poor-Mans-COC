import math
import sys,tty,termios
from colorama import Fore


spawn_point_art = {'J': '🅙 ',
                    'K': '🅚 ',
                    'L': '🅛 '}

spawn_point_loc = {'J': (40, 40),
                    'K': (5, 36),
                    'L': (45, 6)}



def euc_distance(pos1, pos2) :
    return float(math.sqrt(pow(pos1[0] - pos2[0], 2) + pow(pos1[1] - pos2[1], 2)))


def mv_distance(pos1, pos2) :
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


class Getch:       
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch
        

win_meassage = Fore.GREEN + """
\t ██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗██╗███╗░░██╗
\t ╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██║████╗░██║
\t ░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║██╔██╗██║
\t ░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║██║╚████║
\t ░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░██║██║░╚███║
\t ░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝\n""" + Fore.RESET



lose_meassage = Fore.RED + """
\t██╗░░░██╗░█████╗░██╗░░░██╗  ██╗░░░░░░█████╗░░██████╗███████╗
\t╚██╗░██╔╝██╔══██╗██║░░░██║  ██║░░░░░██╔══██╗██╔════╝██╔════╝
\t░╚████╔╝░██║░░██║██║░░░██║  ██║░░░░░██║░░██║╚█████╗░█████╗░░
\t░░╚██╔╝░░██║░░██║██║░░░██║  ██║░░░░░██║░░██║░╚═══██╗██╔══╝░░
\t░░░██║░░░╚█████╔╝╚██████╔╝  ███████╗╚█████╔╝██████╔╝███████╗
\t░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚══════╝░╚════╝░╚═════╝░╚══════╝\n""" + Fore.RESET


intr_meassage = Fore.MAGENTA + """
\t█▀▀ ▄▀█ █▀▄▀█ █▀▀   █ █▄░█ ▀█▀ █▀▀ █▀█ █▀█ █░█ █▀█ ▀█▀ █▀▀ █▀▄
\t█▄█ █▀█ █░▀░█ ██▄   █ █░▀█ ░█░ ██▄ █▀▄ █▀▄ █▄█ █▀▀ ░█░ ██▄ █▄▀\n""" + Fore.RESET