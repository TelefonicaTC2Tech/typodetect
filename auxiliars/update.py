"""Script para actualizar los TLD"""
import json
import urllib.request

from colorama import Fore
from colorama import Style
from auxiliars.constants import tlds_json
from auxiliars.constants import separator
from auxiliars.constants import url_update


def updating():
    with open(tlds_json, encoding='utf-8') as file:
        options = json.load(file)
    try:
        for new_tld in urllib.request.urlopen(url_update).readlines():
            new_tld = new_tld.decode('utf-8').strip('\n')
            if new_tld == options["updated"]:
                print(Fore.GREEN + Style.BRIGHT + separator)
                print('[*] TLD DataBase is update')
                print(Fore.GREEN + Style.BRIGHT + separator)
                break
            elif 'Last Updated ' in new_tld:
                options['updated'] = new_tld
            else:
                i = 0
                for sections in list(options['tld'].keys()):
                    if new_tld.lower() not in options['tld'][sections]:
                        i += 1
                if i == len(list(options['tld'].keys())):
                    options['tld']['updated'].append(new_tld.lower())

        new_options = json.dumps(options, ensure_ascii=False)
        with open(tlds_json, 'w') as file:
            file.write(new_options)

    except:
        print(Fore.RED + Style.BRIGHT + '[*] Update TLDś DataBase failed.')

