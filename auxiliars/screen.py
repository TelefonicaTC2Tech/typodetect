#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from colorama import Fore
from colorama import Style
from auxiliars.banner import banner
from auxiliars.constants import separator


def screen_print(origin, mutations, result, doh):
    os.system('cls' if os.name == 'nt' else 'clear')
    banner(origin)
    doh_server = ''
    if doh == 1:
        doh_server = 'ElevenPaths'
    elif doh == 2:
        doh_server = 'Cloudfare'
    print(Fore.GREEN + Style.BRIGHT + separator)
    print(Fore.GREEN + Style.BRIGHT + '[*] We detected ' + str(mutations) +
          ' possibles domains mutations of ' + origin)
    print(Fore.GREEN + Style.BRIGHT + '[*] Of which '
          + str(len(list(result.keys()))) +
          ' domains resolved to an A or MX record for ' + doh_server)
    print(Fore.GREEN + Style.BRIGHT + separator)
    print('')
    malware = 0

    for threat in list(result.keys()):
        if result[threat]['report_DoH'] == 'Malware':
            print(Fore.RED + Style.NORMAL + '\t[*] Detected domain:  '
                  + result[threat]['domain'])
            print(Fore.RED + Style.NORMAL +
                  '\t\t[*] DNS over HTTPS of ElevenPaths'
                  ' report this domain is Malware')
            print(Fore.RED + Style.NORMAL + separator)
            malware = 1
        elif result[threat]['report_DoH'] == '':
            print(Fore.YELLOW + Style.NORMAL + '\t[*] Detected domain:  '
                  + result[threat]['domain'])
            for a_ip in result[threat]['A']:
                print(Fore.YELLOW + Style.NORMAL +
                      '\t\t[*] Register type A: ' + a_ip)
            print(Fore.YELLOW + Style.NORMAL + separator)

    if malware == 0:
        print(Fore.CYAN + Style.NORMAL + separator)
        print(Fore.CYAN + Style.NORMAL + '[*] No mutation of the domain '
              + origin + ' reported as malware was detected in ' +
              doh_server + '\'s DNS')
        print(Fore.CYAN + Style.NORMAL + separator)

    print(Fore.CYAN + Style.NORMAL + separator)
    print(Fore.CYAN + Style.NORMAL + '[*] If the report is in ' + Fore.RED
          + Style.BRIGHT + 'red' + Fore.CYAN + Style.NORMAL +
          ', it is a domain marked as malware in the DoH')
    print(Fore.CYAN + Style.NORMAL + '[*] If the report is in ' + Fore.YELLOW
          + Style.BRIGHT + 'yellow' + Fore.CYAN + Style.NORMAL +
          ', it is a domain detected in the Blockchain DNS')
    print(Fore.CYAN + Style.NORMAL + separator)
