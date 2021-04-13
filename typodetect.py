#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" script principal del sistema"""

import os

from colorama import Fore
from colorama import Style

from files.txt_file import files_txt
from files.json_file import files_json
from auxiliars.worker import process
from auxiliars.update import updating
from auxiliars.screen import screen_print
from auxiliars.constants import b
from auxiliars.constants import warning
from auxiliars.arguments import arguments
from auxiliars.generator import generator
from auxiliars.constants import separator
from auxiliars.normalization import normalization


def main():

    args = arguments()
    if args[1].upper() == 'Y':
        updating()

    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.GREEN + Style.BRIGHT + b)
    print(Fore.RED + Style.BRIGHT + separator)
    print(Fore.RED + Style.BRIGHT + warning)
    print(Fore.RED + Style.BRIGHT + separator)
    print(Fore.RESET + Style.RESET_ALL)
    parts = normalization(args[0])
    print(Fore.GREEN + Style.BRIGHT + '[*]  Creating mutations')
    print(Fore.GREEN + Style.BRIGHT + separator)
    print(Fore.RESET + Style.RESET_ALL)
    possibilities = generator(parts)
    print('\n' + Fore.GREEN + Style.BRIGHT + '[*]  Testing if '
          + str(len(possibilities)) + ' mutations exist')
    print(Fore.GREEN + Style.BRIGHT + separator)
    print(Fore.RESET + Style.RESET_ALL)

    result = process(args[3], possibilities, args[4])

    i = 0
    while i < (len(list(result.keys()))):
        result[str(i)] = result.pop(list(result.keys())[0])
        i += 1

    screen_print(args[0], len(possibilities), result, args[4])

    if args[2].upper() == 'TXT':
        files_txt(result, args[0], len(possibilities))
    else:
        files_json(result, args[0])


if __name__ == '__main__':
    main()
