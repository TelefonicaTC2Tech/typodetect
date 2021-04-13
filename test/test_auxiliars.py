#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from io import StringIO
from unittest.mock import patch

from auxiliars.screen import screen_print
from auxiliars.generator import generator
from auxiliars.blockchain import blockchain
from auxiliars.normalization import normalization


class TestTypoDetect(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.parts = {}
        self.domain = 'elevenpaths.com'
        self.stdout = 'sys.stdout'
        self.possibilities = []

    def test_normalization(self):
        domain = [self.domain, 'lab.elevenpaths.com',
                  'elevenpaths.tech', 'lab.elevenpaths.tech',
                  'elevenpaths.com.bb', 'lab.elevenpaths.edu.bb',
                  'elevenpaths.gratis.es', 'lab.elevenpaths.gratis.es',
                  'elevenpaths.dk', 'elevenpaths',
                  'csa.lab.elevenpaths.team', 'csa.lab.elevenpaths.team.co']
        result = [{'domain': 'elevenpaths', 'tld': 'com',
                   'tld_2': '', 'subdomain': ''},
                  {'domain': 'elevenpaths', 'tld': 'com',
                   'tld_2': '', 'subdomain': 'lab'},
                  {'domain': 'elevenpaths', 'tld': 'tech',
                   'tld_2': '', 'subdomain': ''},
                  {'domain': 'elevenpaths', 'tld': 'tech',
                   'tld_2': '', 'subdomain': 'lab'},
                  {'domain': 'elevenpaths', 'tld': 'com',
                   'tld_2': 'bb', 'subdomain': ''},
                  {'domain': 'elevenpaths', 'tld': 'edu',
                   'tld_2': 'bb', 'subdomain': 'lab'},
                  {'domain': 'elevenpaths', 'tld': 'gratis',
                   'tld_2': 'es', 'subdomain': ''},
                  {'domain': 'elevenpaths', 'tld': 'gratis',
                   'tld_2': 'es', 'subdomain': 'lab'},
                  {'domain': 'elevenpaths', 'tld': 'dk',
                   'tld_2': '', 'subdomain': ''},
                  {'domain': '', 'tld': '', 'tld_2': '', 'subdomain': ''},
                  {'domain': 'elevenpaths', 'tld': 'team',
                   'tld_2': '', 'subdomain': 'csa.lab'},
                  {'domain': 'elevenpaths', 'tld': 'team',
                   'tld_2': 'co', 'subdomain': 'csa.lab'}
                  ]

        for dom in domain:
            self.assertEqual(normalization(dom), result[domain.index(dom)])

    def test_generator(self):
        parts = {'domain': 'elevenpaths', 'tld': 'com',
                 'tld_2': '', 'subdomain': ''}
        result = ['3elevenpaths.arpa', '3elevenpaths.arpa.ac',
                  '3elevenpaths.arpa.ad', '3elevenpaths.arpa.ae',
                  '3elevenpaths.arpa.af', '3elevenpaths.arpa.ag',
                  '3elevenpaths.arpa.ai', '3elevenpaths.arpa.al',
                  '3elevenpaths.arpa.am', '3elevenpaths.arpa.ao']

        resp = generator(parts)

        print('Genero ' + str(len(resp)) + ' mutaciones')
        self.assertEqual(resp[0:10], result)

    def test_blockchain(self):
        possibilities = [self.domain, 'lab.elevenpaths.com',
                         'elevenpaths.com.bb', 'lab.elevenpaths.edu.bb',
                         'csa.lab.elevenpaths.team',
                         'csa.lab.elevenpaths.team.co']
        result = ['csa.lab.elevenpaths.bit', 'csa.lab.elevenpaths.emc',
                  'csa.lab.elevenpaths.coin', 'csa.lab.elevenpaths.lib',
                  'csa.lab.elevenpaths.bazar', 'csa.lab.elevenpaths.bbs',
                  'csa.lab.elevenpaths.chan', 'csa.lab.elevenpaths.cyb',
                  'csa.lab.elevenpaths.dyn', 'csa.lab.elevenpaths.geek',
                  'csa.lab.elevenpaths.gopher', 'csa.lab.elevenpaths.indy',
                  'csa.lab.elevenpaths.libre', 'csa.lab.elevenpaths.neo',
                  'csa.lab.elevenpaths.null', 'csa.lab.elevenpaths.o',
                  'csa.lab.elevenpaths.oss', 'csa.lab.elevenpaths.oz',
                  'csa.lab.elevenpaths.parody', 'csa.lab.elevenpaths.pirate',
                  'csa.lab.elevenpaths.ku', 'csa.lab.elevenpaths.te',
                  'csa.lab.elevenpaths.ti', 'csa.lab.elevenpaths.uu',
                  'csa.lab.elevenpaths.team.bit',
                  'csa.lab.elevenpaths.team.emc',
                  'csa.lab.elevenpaths.team.coin',
                  'csa.lab.elevenpaths.team.lib',
                  'csa.lab.elevenpaths.team.bazar',
                  'csa.lab.elevenpaths.team.bbs',
                  'csa.lab.elevenpaths.team.chan',
                  'csa.lab.elevenpaths.team.cyb',
                  'csa.lab.elevenpaths.team.dyn',
                  'csa.lab.elevenpaths.team.geek',
                  'csa.lab.elevenpaths.team.gopher',
                  'csa.lab.elevenpaths.team.indy',
                  'csa.lab.elevenpaths.team.libre',
                  'csa.lab.elevenpaths.team.neo',
                  'csa.lab.elevenpaths.team.null',
                  'csa.lab.elevenpaths.team.o',
                  'csa.lab.elevenpaths.team.oss',
                  'csa.lab.elevenpaths.team.oz',
                  'csa.lab.elevenpaths.team.parody',
                  'csa.lab.elevenpaths.team.pirate',
                  'csa.lab.elevenpaths.team.ku',
                  'csa.lab.elevenpaths.team.te',
                  'csa.lab.elevenpaths.team.ti',
                  'csa.lab.elevenpaths.team.uu',
                  'elevenpaths.bit', 'elevenpaths.emc', 'elevenpaths.coin',
                  'elevenpaths.lib', 'elevenpaths.bazar', 'elevenpaths.bbs',
                  'elevenpaths.chan', 'elevenpaths.cyb', 'elevenpaths.dyn',
                  'elevenpaths.geek', 'elevenpaths.gopher',
                  'elevenpaths.indy', 'elevenpaths.libre',
                  'elevenpaths.neo', 'elevenpaths.null', 'elevenpaths.o',
                  'elevenpaths.oss', 'elevenpaths.oz', 'elevenpaths.parody',
                  'elevenpaths.pirate', 'elevenpaths.ku', 'elevenpaths.te',
                  'elevenpaths.ti', 'elevenpaths.uu', 'lab.elevenpaths.bit',
                  'lab.elevenpaths.emc', 'lab.elevenpaths.coin',
                  'lab.elevenpaths.lib', 'lab.elevenpaths.bazar',
                  'lab.elevenpaths.bbs', 'lab.elevenpaths.chan',
                  'lab.elevenpaths.cyb', 'lab.elevenpaths.dyn',
                  'lab.elevenpaths.geek', 'lab.elevenpaths.gopher',
                  'lab.elevenpaths.indy', 'lab.elevenpaths.libre',
                  'lab.elevenpaths.neo', 'lab.elevenpaths.null',
                  'lab.elevenpaths.o', 'lab.elevenpaths.oss',
                  'lab.elevenpaths.oz', 'lab.elevenpaths.parody',
                  'lab.elevenpaths.pirate', 'lab.elevenpaths.ku',
                  'lab.elevenpaths.te', 'lab.elevenpaths.ti',
                  'lab.elevenpaths.uu']

        self.assertEqual(blockchain(possibilities), result)

    def test_screen_print(self):
        mutations = 3

        result = {
            0: {
                'report_DoH': 'Good',
                'domain': 'elevenpaths.com',
                'A': ['52.212.36.140'],
                'MX': ['elevenpaths-com.mail.protection.outlook.com.']},
            1: {
                'report_DoH': 'Malware',
                'domain': 'northnovacable.ca',
                'A': '',
                'MX': ''},
            2: {
                'report_DoH': '',
                'domain': 'eagletv.coin',
                'A': ['192.243.100.192'],
                'MX': ''}}

        out = "\x1b[32m\x1b[1m\n\n___________                   ________  " \
              "        __                 __ " \
              "  \n\__    ___/__.__.______   ____\______ \   _____/  |_  __" \
              "__   _____/  |_" \
              " \n  |    | <   |  |\____ \ /  _ \|    |  \_/ __ \   __\/ _" \
              "_ \_/ ___\   __|" \
              "\n  |    |  \___  ||  |_> >  <_> )    `   \  ___/|  | \  _" \
              "__/\  \___|  |" \
              "  \n  |____|  / ____||   __/ \____/_______  /\___  >__|  \_" \
              "__  >\___  >__|" \
              "  \n          \/     |__|                 \/     \/         " \
              " \/     \/      " \
              "\n\nTyposquatting Detect and Analyze" \
              "\nBy ElevenPaths https://www.elevenpaths.com/" \
              "\nUsage: python3 ./typodetect.py" \
              "\n\n\n" \
              "\x1b[32m\x1b[1m[*] ---------------------------------------" \
              "-----------------------------------------------------------" \
              "-- [*]" \
              "\n\x1b[31m\x1b[1m[*]	IANA Database updated:  Last " \
              "Updated Tue Jan 19 07:07:01 2021 UTC" \
              "\n\x1b[34m\x1b[1m[*] Inicial Domain:  elevenpaths.com" \
              "\n\x1b[34m\x1b[1m\t[*] Register type A: 52.212.36.140" \
              "\n\x1b[34m\x1b[1m\t[*] Register type MX: elevenpaths-com." \
              "mail.protection.outlook.com." \
              "\n\x1b[32m\x1b[1m[*] -------------------------------------" \
              "----------------------------------------------------------" \
              "----- [*]" \
              "\n\n\n\n\x1b[32m\x1b[1m[*] ---------------------------------" \
              "------------------------------------------------------------" \
              "------- [*]" \
              "\n\x1b[32m\x1b[1m[*] We detected 3 possibles domains mutation" \
              "s of elevenpaths.com" \
              "\n\x1b[32m\x1b[1m[*] Of which 3 domains resolved to an A or" \
              " MX record for ElevenPaths" \
              "\n\x1b[32m\x1b[1m[*] ----------------------------------------" \
              "------------------------------------------------------------" \
              " [*]" \
              "\n" \
              "\n\x1b[31m\x1b[22m\t[*] Detected domain:  northnovacable.ca" \
              "\n\x1b[31m\x1b[22m\t\t[*] DNS over HTTPS of ElevenPaths" \
              " report this domain is Malware" \
              "\n\x1b[31m\x1b[22m[*] --------------------------------------" \
              "------------------------------------------------------------" \
              "-- [*]" \
              "\n\x1b[33m\x1b[22m\t[*] Detected domain:  eagletv.coin" \
              "\n\x1b[33m\x1b[22m\t\t[*] Register type A: 192.243.100.192" \
              "\n\x1b[33m\x1b[22m[*] --------------------------------------" \
              "-------------------------------------------------------------" \
              "- [*]" \
              "\n\x1b[36m\x1b[22m[*] -------------------------------------" \
              "-----------------------------------------------------------" \
              "---- [*]" \
              "\n\x1b[36m\x1b[22m[*] If the report is in " \
              "\x1b[31m\x1b[1mred\x1b[36m\x1b[22m, it is a domain marked as" \
              " malware in the DoH" \
              "\n\x1b[36m\x1b[22m[*] If the report is in " \
              "\x1b[33m\x1b[1myellow\x1b[36m\x1b[22m, it is a domain" \
              " detected in the Blockchain DNS" \
              "\n\x1b[36m\x1b[22m[*] ----------------------------------" \
              "------------------------------------------------------" \
              "------------ [*]\n"

        with patch(self.stdout, new=StringIO()) as screen_out:
            screen_print(self.domain, mutations, result, 1)
            self.assertEqual(screen_out.getvalue(), out)


if __name__ == "__main__":
    unittest.main()
