import colorama
from colorama import Fore, Back, Style
import os
import time

def clear():
    os.system("cls") 



def draw_tree(light):
    print(f"{Fore.GREEN}                   {light}*{Back.YELLOW}")
    print(f"{Fore.GREEN}                  ***")
    print(f"{Fore.GREEN}                 *{Fore.RED}o{Fore.GREEN}***")
    print(f"{Fore.GREEN}               *****{Fore.CYAN}0{Fore.GREEN}***{light}*{Back.RESET}")
    print(f"{Fore.GREEN}              {light}*{Back.RESET}***{Fore.YELLOW}^{Fore.GREEN}*******")
    print(f"{Fore.GREEN}            ***{Fore.CYAN}0{Fore.GREEN}******{Fore.BLUE}Q{Fore.GREEN}*****")
    print(f"{Fore.GREEN}         *****{Fore.YELLOW}^{Fore.GREEN}**********{Fore.CYAN}0{Fore.GREEN}*****")
    print(f"{Fore.GREEN}             ***{Fore.RED}o{Fore.GREEN}****{light}*{Back.RESET}*****")
    print(f"{Fore.GREEN}            ******{Fore.RED}o{Fore.GREEN}*****{Fore.BLUE}Q{Fore.GREEN}***")
    print(f"{Fore.GREEN}          *****{Fore.YELLOW}^{Fore.GREEN}******{light}*{Back.RESET}*******")
    print(f"{Fore.GREEN}       *****{Fore.CYAN}0{Fore.GREEN}*****{Fore.YELLOW}^{Fore.GREEN}*****{Fore.BLUE}Q{Fore.GREEN}********")
    print(f"{Fore.GREEN}    *******{Fore.YELLOW}^{Fore.GREEN}*****{light}*{Back.RESET}******{Fore.YELLOW}^{Fore.GREEN}***********")
    print(f"{Fore.GREEN}        ********{Fore.YELLOW}^{Fore.GREEN}**********{Fore.CYAN}0{Fore.GREEN}****")
    print(f"{Fore.GREEN}      ***{light}*{Back.RESET}*{Fore.RED}o{Fore.GREEN}******{Fore.YELLOW}^{Fore.GREEN}********{Fore.BLUE}Q{Fore.GREEN}******")
    print(f"{Fore.GREEN}        ********{Fore.CYAN}0{Fore.GREEN}*******{Fore.BLUE}Q{Fore.GREEN}*******")
    print(f"{Fore.GREEN}      ***********8******{light}*{Back.RESET}**********")
    print(f"{Fore.GREEN}    ******{Fore.CYAN}0{Fore.GREEN}*******{Fore.YELLOW}^{Fore.GREEN}*******{Fore.RED}o{Fore.GREEN}********")
    print(f"{Fore.GREEN}***{light}*{Back.RESET}**{Fore.RED}o{Fore.GREEN}******{Fore.BLUE}Q{Fore.GREEN}*********{Fore.RED}o{Fore.GREEN}*******{Fore.YELLOW}^{Fore.GREEN}***{light}*{Back.RESET}****")
    print(f"                {light}{Back.BLACK}{Fore.WHITE}|||||||||")
    print(f"                {light}{Back.BLACK}{Fore.WHITE}|||||||||")



colorama.init(autoreset =True)

for x in range(100):
    clear()
    if x % 2 ==0:
        draw_tree(Back.YELLOW)
    else:
        draw_tree(Back.MAGENTA)

    time.sleep(1)