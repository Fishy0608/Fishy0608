# Fade was proudly coded by Rdimo (https://github.com/Rdimo).
# Fade Nuker under the GNU General Public Liscense v2 (1991).

import undetected_chromedriver as uc
import os
import Fade
from time import sleep
from selenium import webdriver
from colorama import Fore

from util.plugins.common import clear, print_slow, getheaders, THIS_VERSION

def TokenLogin(token):
    print(f"{Fore.GREEN}Checking Chromedriver. . .")
    sleep(0.5)
    if os.path.exists(os.getcwd()+"\\chromedriver.exe"):
        print("Chromedriver already exists, continuing. . .")
        sleep(0.5)
    else:
        try:
            print(f"{Fore.RED}Chromedriver not found! Installing it for you")
            uc.install()
        except Exception as e:
            print(f"{Fore.RED}Failed to download driver. . .\nError: {e}")
            print(f"if this keeps happening go to https://github.com/Rdimo/Fade-Nuker#8-log-into-an-account and install a chromedriver manually")
            sleep(5)
            Fade.main()
    try:
        opts = webdriver.ChromeOptions()
        opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        opts.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=opts)
        script = """
                function login(token) {
                setInterval(() => {
                document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
                }, 50);
                setTimeout(() => {
                location.reload();
                }, 1000);
                }
               """
        driver.get("https://discordapp.com/login")
        driver.execute_script(script+f'\nlogin("{token}")')
        Fade.main()
    except Exception as e:
        print(f"{Fore.RED}Sorry Fade had trouble loggin in to the account\ncontact rdimo#6969 if this keeps happening")
        print(f"Ignoring error: {e}")
        sleep(5)
        Fade.main()