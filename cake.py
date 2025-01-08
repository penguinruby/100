import colorama
from colorama import Fore, Back, Style
import os
import time

def clear():
    os.system("cls") 



def draw_tree(light):
    print(f"{Fore.GREEN}                        {light}^{Back.YELLOW}")
    print(f"{Fore.RED}                       *0*")
    print(f"{Fore.RED}                       *0*")
    print(f"{Fore.RED}                       *0*")
    print(f"{Fore.RED}                       *0*")
    print(f"{Fore.RED}                       ***")
    print(f"{Fore.RED}              {light} {Back.RESET}        ***       {light} {Back.RESET}")
    print(f"{Fore.MAGENTA}              ||||{Fore.RED}l{Fore.MAGENTA}|||||||||{Fore.RED}l{Fore.MAGENTA}|||||")
    print(f"{Fore.GREEN}              **********{Fore.RED}o{Fore.GREEN}*********")
    print(f"{Fore.GREEN}              ****************{Fore.RED}o{Fore.GREEN}***")
    print(f"{Fore.CYAN}        **{Fore.GREEN}o{Fore.CYAN}******************************")
    print(f"{Fore.BLUE}        ||||||||||{Fore.RED}I{Fore.BLUE}||||||||||||{Fore.RED}I{Fore.BLUE}|||||{Fore.RED}I{Fore.BLUE}|||")
    print(f"{Fore.CYAN}        ********{Fore.GREEN}o{Fore.CYAN} *************{Fore.GREEN}o{Fore.CYAN}*********")
    print(f"{Fore.BLUE}        ||{Fore.RED}!{Fore.BLUE}|||||{Fore.RED}!{Fore.BLUE}||||||{Fore.RED}!{Fore.BLUE}|||||||||||{Fore.RED}!{Fore.BLUE}|||||")

    print(f"{Fore.BLUE}    Happy    Birthday    to   old       tin")
   



colorama.init(autoreset =True)

for x in range(100):
    clear()
    if x % 2 ==0:
        draw_tree(Back.YELLOW)
    else:
        draw_tree(Back.RED)

    time.sleep(1)