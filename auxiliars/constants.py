#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Constantes generales del sistema"""

import os

# Directories
tlds_json = os.path.dirname(os.path.abspath(__file__)) \
            + os.sep + 'tlds.json'

result_txt = os.path.dirname(os.path.abspath(__file__))\
            + os.sep + 'result.txt'

reports = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\
          + os.sep + 'reports' + os.sep

# Generic
separator = "[*] {0} [*]".format('-' * 100)
ct = "application/dns-message"
dnssec = {
    'elevenpaths': {
        'url': 'https://doh-beta.e-paths.com/dns-query',
        'malware_ip': '18.194.105.161'},
    'couldfare': {
        'server': '1.1.1.3',
        'malware_ip': '184.168.221.61'}}


# URLs
url_update = 'https://data.iana.org/TLD/tlds-alpha-by-domain.txt'
url_bdns = 'https://bdns.io/r/'


b = """

___________                   ________          __                 __   
\__    ___/__.__.______   ____\______ \   _____/  |_  ____   _____/  |_ 
  |    | <   |  |\____ \ /  _ \|    |  \_/ __ \   __\/ __ \_/ ___\   __|
  |    |  \___  ||  |_> >  <_> )    `   \  ___/|  | \  ___/\  \___|  |  
  |____|  / ____||   __/ \____/_______  /\___  >__|  \___  >\___  >__|  
          \/     |__|                 \/     \/          \/     \/      

Typosquatting Detect and Analyze
By ElevenPaths https://www.elevenpaths.com/
Usage: python3 ./typodetect.py

"""

warning = """
[*] The creation and testing process of any mutation is very slow.
[*] You can go to drink a coffee or take a nap.
"""

