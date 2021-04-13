#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from colorama import Fore
from colorama import Style
from querys.udp import dns_udp
from auxiliars.constants import b
from auxiliars.constants import tlds_json
from auxiliars.constants import separator


def banner(domain):
    with open(tlds_json) as file:
        options = json.load(file)

    print(Fore.GREEN + Style.BRIGHT + b)
    print(Fore.GREEN + Style.BRIGHT + separator)
    print(Fore.RED + Style.BRIGHT +
          '[*]\tIANA Database updated: ' + options['updated'].rsplit(',')[-1])

    origin = dns_udp(domain, 0)
    if origin != {}:
        print(Fore.BLUE + Style.BRIGHT + '[*] Inicial Domain:  '
              + origin[0]['domain'])
        for a_ip in origin[0]['A']:
            print(Fore.BLUE + Style.BRIGHT +
                  '\t[*] Register type A: ' + a_ip)
        for mx_ip in origin[0]['MX']:
            if mx_ip != '':
                print(Fore.BLUE + Style.BRIGHT +
                      '\t[*] Register type MX: ' + mx_ip)

        print(Fore.GREEN + Style.BRIGHT + separator)
        print('\n\n')
    else:
        print(Fore.BLUE + Style.BRIGHT + '[*] Dominio ' + domain
              + ' does not exist')

