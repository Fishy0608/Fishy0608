# Fade was proudly coded by Rdimo (https://github.com/Rdimo).
# Fade Nuker under the GNU General Public Liscense v2 (1991).

import requests
import Fade
from colorama import Fore

from util.plugins.common import clear, print_slow, getheaders, THIS_VERSION

def StatusChanger(token, Status):
    #change status 
    CustomStatus = {"custom_status": {"text": Status}} #{"text": Status, "emoji_name": "☢"} if you want to add an emoji to the status
    try:
        r = requests.patch("https://discord.com/api/v8/users/@me/settings", headers=getheaders(token), json=CustomStatus)
        print_slow(f"\n{Fore.GREEN}Status changed to {Fore.WHITE}{Status}{Fore.GREEN} ")
    except Exception as e:
        print(f"{Fore.RED}Error:\n{e}\nOccured while trying to change the status :/")
    print("Enter anything to continue. . . ", end="")
    input()
    Fade.main()